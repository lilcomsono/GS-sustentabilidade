# Fontes, hipóteses e condições de validade

## Dados com referência pública verificável

**Emissões do SIN em 2023:** 38,5 kg de CO₂/MWh = 0,0385 kg CO₂/kWh.

- Fonte: Ministério de Minas e Energia, reproduzido pela Agência Gov em 14/02/2024, com dados do MCTI.
- [Publicação consultada](https://agenciagov.ebc.com.br/noticias/202402/geracao-de-energia-eletrica-tem-a-menor-emissao-de-co2-dos-ultimos-onze-anos-1).
- Natureza: média histórica do sistema; não fator de 2026, emissão marginal ou avaliação de ciclo de vida.
- Aplicação: redução calculada da compra da rede × fator × 12 meses equivalentes. Unidade CO₂, não CO₂e.

**Metodologia de irradiação:** SunData fornece médias diárias mensais em kWh/m²/dia, por localidade e plano.

- Fonte: [CRESESB / CEPEL — SunData v3.0](https://cresesb.cepel.br/sundata/index.php).
- Essa página fundamenta a metodologia e as unidades, não o valor 4,3 para a escola. As coordenadas não foram levantadas.
- Conversão: HSP = irradiação diária / 1 kW/m². Neste cenário, assume-se 4,3 h/dia de sol pleno.

## Hipóteses de simulação — não dados coletados

| Item | Hipótese e justificativa de uso | Como validar numa implantação |
|---|---|---|
| Escola e uso | Escola pública hipotética em São Paulo; 22 dias letivos, luz 8 h/dia e ar 5 h/dia | Visita, inventário e calendário escolar |
| Iluminação existente | 80 luminárias, 80 W cada: duas lâmpadas de 36 W mais perdas aproximadas do reator | Etiquetas dos equipamentos e medição |
| Climatização | 10 aparelhos, potência elétrica média assumida de 1.000 W; sem modelagem do compressor | Etiquetas, perfil de uso e medição |
| LED | 36 W; supõe manutenção da iluminação necessária | Fluxo luminoso, fotometria, iluminância e instalação |
| Tarifa | R$ 0,95/kWh uniforme; mantém a comparação reproduzível | Distribuidora, modalidade, vigência, impostos e regras da geração |
| Solar | 5 kWp, HSP 4,3 h/dia e desempenho global de 80%; cenário de análise, não dimensionamento executivo | Irradiação no local, orientação, sombreamento e projeto |
| Dias de solar | Só 22 dias: exclui produção dos demais dias e créditos não simulados | Balanço horário e calendário completo |
| Investimento LED | R$ 450 por luminária instalada; hipótese de equipamento + instalação | Cotação compatível com sala de aula e instalação |
| Investimento solar | R$ 4.200/kWp instalado; hipótese de módulos, inversor e instalação | Cotação e análise técnica do telhado |
| Operação/manutenção | Reserva anual hipotética de 1% do investimento, para não assumir manutenção gratuita | Plano real de manutenção, limpeza e substituições |
| Aproveitamento | Toda a geração contabilizada atende à demanda no balanço mensal; não comprova coincidência horária | Medição de autoconsumo, excedentes e regras de compensação |
| Anualização | 12 meses iguais para comparar resultados | Férias, ocupação, sazonalidade e degradação |

[ANEEL — Tarifas](https://www.gov.br/aneel/pt-br/assuntos/tarifas) é uma referência para consulta de tarifa específica. O valor de R$ 0,95 do modelo não foi extraído como tarifa oficial dessa página.

## Escopo financeiro

- Custo operacional modelado = compra de energia + reserva mensal de manutenção.
- A manutenção do cenário existente não foi levantada; não há crédito por uma eventual economia de manutenção antiga.
- A reserva de 1% não é uma cotação nem garantia de cobertura de falhas. Troca futura do inversor não recebeu orçamento próprio.
- Retorno simples bruto = investimento / economia de energia em reais.
- Retorno simples líquido = investimento / (economia bruta − reserva mensal).
- Sem juros, desconto de fluxo de caixa, reajustes, inflação ou tributação detalhada.

## Escopo do protótipo

Implementado: leitura de premissas, cálculo reproduzível, comparação com a referência, testes, exportação JSON e geração automática de HTML local.

Conceitual: medidores, medição de geração/consumo, conexão desses dados ao processamento e atualização em tempo real. Não há hardware instalado.

Nenhuma estimativa é resultado garantido. Referências consultadas em 19/11/2026.
