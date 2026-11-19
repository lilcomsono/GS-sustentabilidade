# Roteiro do vídeo — SERS 2026.2

**Narrador:** Kalil Bachur. **Tempo planejado:** 2min52s, com limite de 3 minutos.

As falas abaixo totalizam 346 palavras (contagem por espaços). Isso não garante duração: números levam mais tempo para falar. Ensaie com cronômetro, incluindo as trocas de tela, e busque encerrar entre 2min45s e 2min55s.

## Identificação do grupo

- Letticia Aparecida Martins — RM 575441
- Kalil Bachur — RM 576335
- Gustavo Valentim de Souza — RM 575916

Os nomes e RMs devem aparecer na capa; não é necessário lê-los em voz alta. Kalil pode narrar tudo.

## Mapa de gravação

| Slide | Tempo planejado | Tema |
|---|---|---|
| 1 | 0:00–0:12 | Capa |
| 2 | 0:12–0:30 | Problema |
| 3 | 0:30–0:50 | Método e consumo de referência |
| 4 | 0:50–1:12 | Alternativas e custos |
| 5 | 1:12–1:28 | Diagrama |
| 6 | 1:28–2:05 | Resultados: economia bruta e líquida |
| 7 | 2:05–2:28 | Demonstração do dashboard |
| 8 | 2:28–2:52 | Benefícios e limitações |

## Slide 1 — Capa (0:00–0:12)

**Fala:**

Olá, sou Kalil. Nosso grupo propõe uma combinação de LED e energia solar para uma escola pública em São Paulo.

**Na tela:** Capa com os três nomes e RMs legíveis. Não é necessário ler os RMs em voz alta.

## Slide 2 — Problema (0:12–0:30)

**Fala:**

O cenário é hipotético, sem visita técnica nem medições. Consideramos dois usos: 80 luminárias de 80 W, ligadas 176 horas por mês, e 10 aparelhos de ar-condicionado de 1000 W, por 110 horas. Juntos, consomem 2.226,4 kWh por mês.

**Na tela:** Tabela com os dois usos e o consumo de referência.

## Slide 3 — Método e consumo de referência (0:30–0:50)

**Fala:**

Calculamos energia como potência vezes quantidade e tempo. O Python lê as premissas e gera um arquivo de resultados e o dashboard offline. São dados simulados, não de sensores reais. Aqui, mostramos a execução do programa.

**Na tela:** Fluxo do método; recorte de 3 a 5 segundos do terminal executando o script Python.

## Slide 4 — Alternativas e custos (0:50–1:12)

**Fala:**

Avaliamos duas alternativas. Primeiro, LED de 36 W, uma luz equivalente que ainda precisa ser validada em lúmens e iluminância antes da instalação, por 36 mil reais. Segundo, solar de 5 kWp, com 4,3 horas de sol pleno por dia e desempenho de 80%, por 21 mil reais. Telhado e orçamento não foram levantados.

**Na tela:** Dois cartões: LED e solar, com premissas e CAPEX.

## Slide 5 — Diagrama (1:12–1:28)

**Fala:**

No diagrama, o solar passa pelo inversor e, com a rede, chega ao quadro, que alimenta LED e ar-condicionado. Hoje, premissas de simulação alimentam o Python; no futuro, medidores poderiam fazer isso, num monitoramento ainda conceitual.

**Na tela:** Diagrama: solar/inversor + rede -> quadro -> LED + AC; premissas (simulação) ou medidores (futuro) -> Python -> indicadores/dashboard.

## Slide 6 — Resultados: economia bruta e líquida (1:28–2:05)

**Fala:**

Com LED, o consumo dos dois usos cai 27,8%. A solar gera 378,4 kWh nos 22 dias considerados. A compra da rede cai 44,8%, e a participação solar é de 23,5%. Com tarifa hipotética de 95 centavos por kWh, a economia bruta é de 948 reais mensais. A reserva de manutenção de 47 reais e 50 centavos reduz esse valor para aproximadamente 901 reais. O investimento combinado é de 57 mil reais, com retorno simples líquido em 63,3 meses.

**Na tela:** Gráfico de consumo (referência, pós-LED, rede final) e tabela bruta/líquida/retorno.

## Slide 7 — Demonstração do dashboard (2:05–2:28)

**Fala:**

Agora, o dashboard real, aberto offline. Mostramos os seis indicadores, os gráficos e a comparação dos cenários. A redução é comparada à referência atual. Estes números foram gerados pelo Python, não por medições.

**Na tela:** Gravação de tela do dashboard.html: indicadores, comparação e retorno (cerca de 23 s).

## Slide 8 — Benefícios e limitações (2:28–2:52)

**Fala:**

A estimativa é evitar 461 quilos de CO₂ por ano equivalente. Usamos o fator histórico do SIN de 2023, não um dado de 2026 nem uma análise de ciclo de vida. A economia pode apoiar a comunidade escolar. Antes de implantar, precisamos validar iluminação, telhado, uso e orçamento. Obrigado.

**Na tela:** Lista de benefícios e limitações; encerramento.

## Pontos para o ensaio

- Não leia a apresentação inteira. As notas já trazem a fala resumida.
- Slide 3: mostre a execução real de `python calculos.py`, por poucos segundos.
- Slide 7: abra o dashboard no navegador, mostre os indicadores e desça aos gráficos e à comparação. A imagem no slide é apenas apoio.
- O painel usa uma casa decimal para energia/percentuais; o README conserva precisão maior. As economias monetárias do painel são R$ 948,02 brutos e R$ 900,52 líquidos. Na fala, 948 e 901 são aproximações deliberadas.
- Não diga que a escola foi medida, que há sensores instalados ou que os preços são cotações.
- A geração calculada considera só 22 dias; não inclui os demais dias ou créditos.
- O retorno é simples e depende das hipóteses, incluindo reserva didática de manutenção.
- Se passar de 2min55s no ensaio, encurte a introdução ou as explicações; preserve as duas alternativas, a demonstração, os custos e as limitações.
