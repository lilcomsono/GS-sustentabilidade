"""SERS 2026.2: simulação energética de iluminação e ar-condicionado.

Execute: python calculos.py
O programa imprime a análise, grava dados/resultados.json e gera dashboard.html.
Usa apenas a biblioteca padrão. Sensores e medições reais não estão implementados.
"""
from decimal import Decimal
from pathlib import Path
import argparse
import html
import json

BASE = Path(__file__).resolve().parent
D = Decimal


def br(valor, casas=1):
    """Número no padrão brasileiro, arredondado somente para apresentação."""
    if valor is None:
        return "não aplicável"
    return f"{float(valor):,.{casas}f}".replace(",", "_").replace(".", ",").replace("_", ".")


def calcular(p):
    """Calcula o balanço mensal simplificado; recebe as premissas como dicionário."""
    def n(chave):
        valor = D(str(p[chave]))
        if valor < 0:
            raise ValueError(f"Premissa negativa: {chave}")
        return valor

    dias = n("dias_letivos_mes")
    horas_luz = n("horas_iluminacao_dia") * dias
    horas_ar = n("horas_ar_dia") * dias
    if dias == 0 or n("tarifa_rs_kwh") == 0:
        raise ValueError("Dias letivos e tarifa devem ser maiores que zero.")
    if n("desempenho_solar") > 1:
        raise ValueError("Desempenho solar deve estar entre 0 e 1.")
    luz_atual = n("potencia_fluorescente_w") * n("quantidade_luminarias") * horas_luz / 1000
    luz_led = n("potencia_led_w") * n("quantidade_luminarias") * horas_luz / 1000
    ar = n("potencia_ar_w") * n("quantidade_ar") * horas_ar / 1000
    demanda_atual = luz_atual + ar
    if demanda_atual <= 0 or luz_led + ar <= 0:
        raise ValueError("A demanda deve ser maior que zero.")
    demanda_led = luz_led + ar
    geracao = n("potencia_solar_kwp") * n("horas_sol_pleno_dia") * n("dias_solar_considerados_mes") * n("desempenho_solar")
    tarifa = n("tarifa_rs_kwh")
    investimento_led = n("quantidade_luminarias") * n("custo_luminaria_instalada_rs")
    investimento_solar = n("potencia_solar_kwp") * n("custo_solar_rs_kwp")
    manut_led = investimento_led * n("reserva_manutencao_led_percentual_ano") / 12
    manut_solar = investimento_solar * n("reserva_manutencao_solar_percentual_ano") / 12
    custo_referencia = demanda_atual * tarifa

    def cenario(nome, demanda, solar, investimento, manutencao):
        # Balanço agregado; não demonstra simultaneidade horária nem créditos.
        solar_utilizada = min(solar, demanda)
        rede = demanda - solar_utilizada
        reducao_rede = demanda_atual - rede
        energia_rs = rede * tarifa
        economia_bruta = custo_referencia - energia_rs
        economia_liquida = economia_bruta - manutencao
        return {
            "nome": nome, "demanda_kwh": demanda, "rede_kwh": rede,
            "solar_considerada_kwh": solar, "solar_utilizada_kwh": solar_utilizada,
            "reducao_consumo_kwh": demanda_atual - demanda,
            "reducao_rede_kwh": reducao_rede,
            "reducao_rede_pct": reducao_rede / demanda_atual * 100,
            "renovavel_pct": solar_utilizada / demanda * 100,
            "investimento_rs": investimento, "reserva_manutencao_mes_rs": manutencao,
            "custo_energia_mes_rs": energia_rs,
            "custo_operacao_modelado_mes_rs": energia_rs + manutencao,
            "economia_bruta_mes_rs": economia_bruta,
            "economia_liquida_mes_rs": economia_liquida,
            "retorno_bruto_meses": investimento / economia_bruta if economia_bruta > 0 else None,
            "retorno_liquido_meses": investimento / economia_liquida if economia_liquida > 0 else None,
            "co2_evitado_ano_kg": reducao_rede * n("fator_co2_kg_kwh") * n("meses_equivalentes_ano")
        }

    r = {
        "projeto": p["projeto"], "integrantes": p["integrantes"],
        "escopo": p["escopo"], "natureza": "Simulação; sem medição real",
        "horas_iluminacao_mes": horas_luz, "horas_ar_mes": horas_ar,
        "iluminacao_atual_kwh": luz_atual, "iluminacao_led_kwh": luz_led,
        "ar_kwh": ar, "economia_iluminacao_kwh": luz_atual - luz_led,
        "economia_iluminacao_pct": (luz_atual - luz_led) / luz_atual * 100 if luz_atual > 0 else None,
        "eficiencia_consumo_total_pct": (demanda_atual - demanda_led) / demanda_atual * 100,
        "fator_co2_kg_kwh": n("fator_co2_kg_kwh"),
        "meses_equivalentes_ano": n("meses_equivalentes_ano"),
        "cenario_atual": cenario("Atual", demanda_atual, D(0), D(0), D(0)),
        "cenario_led": cenario("A — LED", demanda_led, D(0), investimento_led, manut_led),
        "cenario_solar": cenario("B — Solar", demanda_atual, geracao, investimento_solar, manut_solar),
        "cenario_combinado": cenario("LED + Solar", demanda_led, geracao, investimento_led + investimento_solar, manut_led + manut_solar)
    }
    # Monitoramento simulado: confronta os cenários calculados com a referência.
    c = r["cenario_combinado"]
    r["monitoramento"] = {
        "tipo": "Comparação simulada com a referência atual",
        "regra": "Se a energia calculada da rede for menor que a referência, indicar redução projetada; caso contrário, revisão necessária.",
        "status": "Redução projetada" if c["rede_kwh"] < demanda_atual else "Revisão necessária",
        "referencia_rede_kwh": demanda_atual,
        "cenario_rede_kwh": c["rede_kwh"],
        "sensores_instalados": False
    }
    # JSON usa números; a aritmética acima usa Decimal para preservar precisão.
    def serializar(x):
        if isinstance(x, D):
            return float(x)
        if isinstance(x, dict):
            return {k: serializar(v) for k, v in x.items()}
        if isinstance(x, list):
            return [serializar(v) for v in x]
        return x
    return serializar(r)


def gerar_dashboard(p, r, base=BASE):
    modelo = (base / "modelos" / "dashboard.template.html").read_text(encoding="utf-8")
    c = r["cenario_combinado"]
    indicadores = [
        ("Compra de energia da rede", br(c["rede_kwh"]), "kWh / mês considerado"),
        ("Redução da compra da rede", br(c["reducao_rede_pct"]) + "%", br(c["reducao_rede_kwh"]) + " kWh / mês"),
        ("Economia líquida projetada", "R$ " + br(c["economia_liquida_mes_rs"], 2), "por mês, após reserva de manutenção"),
        ("Participação solar", br(c["renovavel_pct"]) + "%", "da demanda elétrica após LED"),
        ("Emissões evitadas projetadas", br(c["co2_evitado_ano_kg"], 0) + " kg", "CO₂ / ano equivalente; fator de 2023"),
        ("Retorno simples líquido", br(c["retorno_liquido_meses"]), "meses — investimento de R$ " + br(c["investimento_rs"], 0))
    ]
    cards = "\n".join(f'<article class="kpi"><div class="label">{html.escape(a)}</div><strong>{html.escape(b)}</strong><small>{html.escape(u)}</small></article>' for a,b,u in indicadores)
    membros = " • ".join(f'{html.escape(x["nome"])} · RM {html.escape(x["rm"])}' for x in p["integrantes"])
    rows = []
    for key in ["cenario_atual", "cenario_led", "cenario_solar", "cenario_combinado"]:
        x = r[key]
        rows.append(f'<tr><th scope="row">{html.escape(x["nome"])}</th><td>{br(x["demanda_kwh"])}</td><td>{br(x["rede_kwh"])}</td><td>{br(x["investimento_rs"],0)}</td><td>{br(x["reserva_manutencao_mes_rs"],2)}</td><td>{br(x["custo_operacao_modelado_mes_rs"],2)}</td><td>{br(x["economia_liquida_mes_rs"],2)}</td><td>{br(x["retorno_liquido_meses"])}</td></tr>')
    barras = []
    maximo = r["cenario_atual"]["rede_kwh"]
    for key,cor in [("cenario_atual","#94a3b8"),("cenario_led","#5cc9a8"),("cenario_solar","#edc666"),("cenario_combinado","#116e58")]:
        x = r[key]
        barras.append(f'<div class="barrow"><span>{html.escape(x["nome"])}</span><div class="track"><div style="width:{x["rede_kwh"]/maximo*100:.4f}%;background:{cor}"></div></div><b>{br(x["rede_kwh"])}</b></div>')
    pct = c["renovavel_pct"]
    resultado_json = json.dumps(r, ensure_ascii=False, indent=2).replace("</", "<\\/")
    valores = {
        "@@CARDS@@": cards, "@@INTEGRANTES@@": membros, "@@ROWS@@": "\n".join(rows),
        "@@STATUS@@": html.escape(r["monitoramento"]["status"]),
        "@@BARRAS@@": "\n".join(barras), "@@RENOVAVEL_PCT@@": str(pct),
        "@@RENOVAVEL_FORMATADO@@": br(pct), "@@SOLAR_KWH@@": br(c["solar_utilizada_kwh"]),
        "@@REDE_KWH@@": br(c["rede_kwh"]), "@@DEMANDA_LED@@": br(c["demanda_kwh"]),
        "@@BRUTA@@": br(c["economia_bruta_mes_rs"],2),
        "@@RESERVA@@": br(c["reserva_manutencao_mes_rs"],2),
        "@@LIQUIDA@@": br(c["economia_liquida_mes_rs"],2),
        "@@EFICIENCIA@@": br(r["eficiencia_consumo_total_pct"]),
        "@@RESULTADOS_JSON@@": resultado_json
    }
    for token,valor in valores.items():
        modelo = modelo.replace(token,valor)
    if "@@" in modelo:
        raise ValueError("Há marcadores não preenchidos no modelo do dashboard.")
    (base / "dashboard.html").write_text(modelo, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--premissas", type=Path, default=BASE / "dados" / "premissas.json")
    args = parser.parse_args()
    p = json.loads(args.premissas.read_text(encoding="utf-8"))
    r = calcular(p)
    (BASE / "dados").mkdir(exist_ok=True)
    (BASE / "dados" / "resultados.json").write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding="utf-8")
    gerar_dashboard(p,r)
    print("SERS 2026.2 — SIMULAÇÃO ENERGÉTICA | Não são dados medidos")
    print("Consumo de iluminação e ar-condicionado, não de toda a escola.")
    print(f"Atual: {br(r['cenario_atual']['demanda_kwh'])} kWh/mês")
    print(f"Após LED: {br(r['cenario_led']['demanda_kwh'])} kWh/mês | redução de consumo: {br(r['eficiencia_consumo_total_pct'])}%")
    print(f"Solar considerada em {p['dias_solar_considerados_mes']} dias: {br(r['cenario_solar']['solar_considerada_kwh'])} kWh")
    c=r["cenario_combinado"]
    print(f"Compra da rede: {br(c['rede_kwh'])} kWh/mês | redução: {br(c['reducao_rede_pct'])}%")
    print(f"Participação solar na demanda após LED: {br(c['renovavel_pct'])}%")
    print(f"Economia bruta: R$ {br(c['economia_bruta_mes_rs'],2)}/mês")
    print(f"Reserva de manutenção: R$ {br(c['reserva_manutencao_mes_rs'],2)}/mês")
    print(f"Economia líquida: R$ {br(c['economia_liquida_mes_rs'],2)}/mês")
    print(f"Retorno simples líquido: {br(c['retorno_liquido_meses'])} meses")
    print(f"Emissões: {br(c['co2_evitado_ano_kg'],0)} kg CO₂/ano equivalente (fator histórico de 2023)")
    print("Monitoramento: " + r["monitoramento"]["status"] + " (simulado)")
    print("Gerados: dados/resultados.json e dashboard.html. Abra o HTML no navegador.")
    print("Premissas, custos e resultados são projeções; verificar condições reais antes de implantação.")


if __name__ == "__main__":
    main()
