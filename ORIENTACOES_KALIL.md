# Orientações para Kalil — preparação e gravação

## 1. O que já está pronto

| Arquivo | Para que usar |
|---|---|
| `APRESENTACAO_SERS.pptx` | Apresentação editável, 8 slides em 16:9, com notas de fala |
| `APRESENTACAO_SERS.pdf` | Versão para visualizar ou apresentar se não houver PowerPoint |
| `ROTEIRO_VIDEO.md` | Texto das falas, tempos e ações na tela |
| `dashboard.html` | Painel real para a demonstração; funciona sem internet |
| `calculos.py` | Recalcula e gera o painel e os resultados |
| `README.md` | Explicação completa do trabalho, contas, limites e fontes |
| `dados/premissas.json` | Premissas que o código usa |

**Integrantes:** Letticia Aparecida Martins — RM 575441; Kalil Bachur — RM 576335; Gustavo Valentim de Souza — RM 575916. Os três aparecem na capa. Não precisa ler os RMs em voz alta.

Kalil pode narrar o vídeo inteiro; o enunciado não exige um trecho de fala de cada integrante.

## 2. Preparar os arquivos

1. Extraia o ZIP. Não rode o Python nem abra a apresentação diretamente de dentro do arquivo compactado.
2. Entre na pasta `Trabalho_SERS_Final` extraída. Não mova só o Python: ele usa as pastas `dados` e `modelos`.
3. Abra um terminal nessa pasta e execute:

```bash
python calculos.py
```

No Windows, se o comando `python` não estiver disponível e o Python estiver instalado, tente `py calculos.py`. O programa não precisa de bibliotecas adicionais.

4. Confira no terminal a indicação de arquivos gerados e abra `dashboard.html` no navegador.
5. Abra `APRESENTACAO_SERS.pptx`. Veja as notas de cada slide no PowerPoint: elas repetem as falas e as ações de tela. Sem PowerPoint, use o PDF junto com o roteiro separado.
6. Deixe terminal, apresentação e navegador prontos antes de gravar. A demonstração requer alternar entre eles.

**Se não tiver Python:** instale Python 3.8 ou superior antes de gravar a execução. O dashboard já incluído pode ser aberto sem Python, mas mostrar esse arquivo pronto não equivale a demonstrar o recálculo. Não diga que rodou se não rodou.

## 3. Gravar com clareza

- **Duração máxima: 3 minutos.** O roteiro planeja 2min52s; esse tempo é uma meta, não uma medição da fala. Ensaie com cronômetro e busque terminar entre 2min45s e 2min55s.
- Capture a tela em 16:9, de preferência em 1920 × 1080. Apresente os slides em tela cheia.
- Use gravador de tela já disponível (por exemplo, OBS ou a gravação de apresentação do PowerPoint). Teste o microfone por 10 segundos e ouça antes da tomada final.
- Narre naturalmente. Não leia cada número do gráfico ou toda a tabela; os detalhes já estão visíveis.
- **Slide 3:** alterne para o terminal e mostre a execução real por alguns segundos. Volte para os slides.
- **Slide 7:** mostre o `dashboard.html` de verdade, não apenas sua imagem no slide. Aponte os indicadores, desça até os gráficos e a comparação, depois volte para o slide 8.
- Não abra arquivos antigos. Use apenas esta versão para evitar os números e rótulos corrigidos.
- Webcam é opcional. A tela e a voz precisam ser legíveis/audíveis.

## 4. O que dizer corretamente

| Pode dizer | Evite dizer |
|---|---|
| “Cenário hipotético; resultados calculados.” | “Medimos esta escola” ou “visitamos o local”. |
| “O LED reduz o consumo dos dois usos em 27,8%.” | “O consumo caiu 45% graças ao solar”. |
| “LED + solar reduzem a compra da rede em 44,8%.” | Confundir compra da rede com demanda dos equipamentos. |
| “Solar cobre 23,5% da demanda após LED.” | “Toda a escola funciona com 24% renovável”. |
| “Economia bruta de R$ 948,02 e líquida de R$ 900,52/mês.” | Tratar a economia bruta como se a manutenção fosse gratuita. |
| “Custos e tarifa são hipóteses.” | “São cotações atuais” ou “tarifa oficial da ANEEL”. |
| “461 kg de CO₂ por ano equivalente; fator histórico de 2023.” | “É o fator atual de 2026” ou trocar CO₂ por CO₂e. |
| “Sensores são uma possibilidade futura.” | “Há medidores instalados e monitoramento em tempo real”. |

A comparação pressupõe iluminação equivalente: o LED de 36 W precisa de validação técnica antes de instalação. O telhado, os preços e o perfil horário também não foram levantados.

## 5. Conferência final da gravação

- [ ] Os três nomes/RMs aparecem legíveis na capa.
- [ ] O áudio está claro e o vídeo inteiro tem no máximo 3 minutos.
- [ ] O Python é executado de verdade e o dashboard é demonstrado na tela.
- [ ] Há explicação das duas alternativas, custos, diagrama e indicadores.
- [ ] A fala diferencia eficiência energética de geração solar.
- [ ] As limitações aparecem no encerramento.
- [ ] A gravação final foi assistida do início ao fim, sem pausas longas ou erros.

O vídeo deve ter visibilidade **não listado**, conforme o enunciado. O prazo deve ser conferido no Portal. Estas orientações tratam dos arquivos e da gravação; não substituem as regras acadêmicas informadas pelo professor.
