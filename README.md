# Football Goals Statistics Analyzer

Projeto desenvolvido para analisar estatísticas de gols de mais de **65 ligas** diferentes utilizando o webscraping, calculando médias ofensivas e defensivas dos times com base nas partidas anteriores.

Os dados são extraídos automaticamente do site soccerstats.com e processados para gerar estatísticas sobre as próximas partidas. Marcando partidas onde uma equipe que faz muitos gols enfrenta outra que sofre muitos gols.

As estatísticas são separadas com gols feitos em casa com gols feitos fora de casa para aumentar a assertividade.

---

# Funcionalidades

- Extração automática do resultado das partidas de diversas ligas do SoccerStats
- Tratamento de dados em arquivo csv
- Cálculo de médias de gols das equipes com a biblioteca Pandas:
  - Média de gols marcados em casa
  - Média de gols sofridos em casa
  - Média de gols marcados fora
  - Média de gols sofridos fora
- Estatísticas de Over Goals:
  - Porcentagem de partidas Over 1.5 gols
  - Porcentagem de partidas Over 2.5 gols
- Análise separada para:
  - Jogos em casa
  - Jogos fora de casa
- Identificação de partidas promissoras:
  - Equipes com ataque forte vs defesa fraca
- Resultado Final exibido numa página HTML

---

# Como exucutar o programa

1. Crie um banco de dados no postgrees para o programa;
2. No arquivo MODELS/dbVariable.py altere e coloque suas credenciais de usuario , senha e nome do banco;  
3. Execute o programa docker desktop;
4. No diretório onde esta localizado o makefile, execute no terminal os seguintes comandos:
     - make build-image // Cria ou reabre a imagem docker com as bibliotecas necessárias instaladas
     - make build-tables // Cria as tabelas do banco e as preenche corretamnte com dados de 65 ligas de futebol
     - make run // executa o programa completo e cria o arquivo csv final com as próximas partidas e suas estatísticas
     - make show // Cria um servidor http na porta 8000 e exibe o dashboard.html num navegador


---



