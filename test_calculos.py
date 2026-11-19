"""Testes dos resultados, balanços e salvaguardas da simulação."""
import copy
import json
import math
from pathlib import Path
import unittest
from calculos import calcular


class TestCalculos(unittest.TestCase):
    def setUp(self):
        self.p = json.loads((Path(__file__).parent / 'dados' / 'premissas.json').read_text(encoding='utf-8'))
        self.r = calcular(self.p)

    def quase(self, real, esperado):
        self.assertTrue(math.isclose(real, esperado, rel_tol=1e-9, abs_tol=1e-6), (real, esperado))

    def test_diagnostico(self):
        self.quase(self.r['iluminacao_atual_kwh'], 1126.4)
        self.quase(self.r['ar_kwh'], 1100)
        self.quase(self.r['cenario_atual']['demanda_kwh'], 2226.4)
        self.quase(self.r['iluminacao_led_kwh'], 506.88)

    def test_consumo_diferente_de_compra_rede(self):
        c=self.r['cenario_combinado']
        self.quase(c['demanda_kwh'],1606.88)
        self.quase(c['rede_kwh'],1228.48)
        self.quase(c['solar_utilizada_kwh'],378.4)
        self.quase(c['rede_kwh']+c['solar_utilizada_kwh'],c['demanda_kwh'])
        self.assertLess(self.r['eficiencia_consumo_total_pct'],c['reducao_rede_pct'])

    def test_economia_e_manutencao(self):
        c=self.r['cenario_combinado']
        self.quase(c['economia_bruta_mes_rs'],948.024)
        self.quase(c['reserva_manutencao_mes_rs'],47.5)
        self.quase(c['economia_liquida_mes_rs'],900.524)
        self.quase(c['custo_operacao_modelado_mes_rs'],1214.556)
        self.quase(c['retorno_liquido_meses'],57000/900.524)

    def test_emissoes_e_participacao(self):
        c=self.r['cenario_combinado']
        self.quase(c['co2_evitado_ano_kg'],461.03904)
        self.quase(c['renovavel_pct'],378.4/1606.88*100)
        self.assertFalse(self.r['monitoramento']['sensores_instalados'])

    def test_alternativas(self):
        a,b=self.r['cenario_led'],self.r['cenario_solar']
        self.quase(a['economia_liquida_mes_rs'],558.544)
        self.quase(b['economia_liquida_mes_rs'],341.98)
        self.quase(a['reserva_manutencao_mes_rs'],30)
        self.quase(b['reserva_manutencao_mes_rs'],17.5)

    def test_solar_nao_deixa_rede_negativa(self):
        p=copy.deepcopy(self.p)
        p['potencia_solar_kwp']=500
        r=calcular(p)
        for k in ['cenario_solar','cenario_combinado']:
            self.assertEqual(r[k]['rede_kwh'],0)
            self.quase(r[k]['renovavel_pct'],100)

    def test_validacao_e_nao_mutacao(self):
        antes=copy.deepcopy(self.p)
        calcular(self.p)
        self.assertEqual(self.p,antes)
        p=copy.deepcopy(self.p)
        p['tarifa_rs_kwh']=-1
        with self.assertRaises(ValueError): calcular(p)
        p=copy.deepcopy(self.p)
        p['desempenho_solar']=1.1
        with self.assertRaises(ValueError): calcular(p)


if __name__ == '__main__':
    unittest.main()
