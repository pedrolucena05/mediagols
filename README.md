# ⚽ Football Goals Statistics Analyzer

Projeto desenvolvido para analisar estatísticas de partidas de futebol de mais de **65 ligas** diferentes, calculando médias ofensivas e defensivas dos times com base em jogos anteriores.

Os dados são extraídos automaticamente do site soccerstats.com e processados para gerar estatísticas sobre as próximas partidas. Marcando partidas onde uma equipe que faz muitos gols enfrenta outra que sofe muitos gols, as estatisticas são separadas com gols feitos em casa com gols feitos fora de casa para aumentar a acertividade.

---

# 📊 Funcionalidades

- Extração automática de dados do SoccerStats
- Processamento de partidas futuras e históricas
- Cálculo de médias de gols:
  - Média de gols marcados em casa
  - Média de gols sofridos em casa
  - Média de gols marcados fora
  - Média de gols sofridos fora
- Estatísticas de Over Goals:
  - Over 1.5 gols
  - Over 2.5 gols
- Análise separada para:
  - Jogos em casa
  - Jogos fora de casa
- Identificação de partidas promissoras:
  - Equipes com ataque forte vs defesa fraca
- Exportação dos dados em CSV/TXT

---

# 🧠 Objetivo

O sistema foi criado para auxiliar na análise estatística de partidas futuras utilizando dados históricos reais das equipes.

O foco principal é identificar padrões ofensivos e defensivos que possam indicar:

- Jogos com alta probabilidade de gols
- Times ofensivamente consistentes
- Defesas vulneráveis
- Confrontos com potencial de Over 1.5 e Over 2.5

---

# 📈 Estatísticas Calculadas

Para cada equipe são calculadas métricas como:

| Estatística | Descrição |
|---|---|
| Avg Goals Scored Home | Média de gols marcados em casa |
| Avg Goals Conceded Home | Média de gols sofridos em casa |
| Avg Goals Scored Away | Média de gols marcados fora |
| Avg Goals Conceded Away | Média de gols sofridos fora |
| Over 1.5 Goals | Percentual de jogos com mais de 1.5 gols |
| Over 2.5 Goals | Percentual de jogos com mais de 2.5 gols |

---

# 🚩 Sistema de Marcação Inteligente

O projeto também possui uma lógica de destaque para partidas onde:

- Um time possui média ofensiva elevada
- O adversário possui média defensiva ruim

Essas partidas recebem uma marcação especial indicando potencial para jogos com muitos gols.

---

# 🌍 Cobertura

Atualmente o sistema suporta:

- Mais de 65 ligas
- Diversos países
- Processamento automatizado de múltiplas partidas

---

# 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- Requests
- BeautifulSoup
- CSV Processing

---

# 📂 Estrutura dos Arquivos

```bash
project/
│
├── league.csv
├── next_games.csv
├── final.csv
├── scraper.py
├── analyzer.py
└── README.md
