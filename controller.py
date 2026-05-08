
from bs4 import BeautifulSoup
import requests
from MODELS.dbVariable import conn, cursor
from SERVICES.treatMatches import generateLeagueCSV
from SERVICES.calculateTeamsAverages import processNextMatches
from SERVICES.sortCSV import sortCSV


headers = {
    "Accept-Encoding": "identity"
}

corruptedLeagues = []
cont = 0
for i in range(1, 66):
    try:
        cursor.execute("""
            SELECT url, leagueName
            FROM leagues
            WHERE id = %s
        """, (i,))

        registro = cursor.fetchone()

        if registro is None:
            print(f"Nenhuma liga encontrada com id {i}")
            continue

        url = registro[0]
        league_name = registro[1]

        cont += 1

        req = requests.get(url, timeout=10, headers=headers)
        soup = BeautifulSoup(req.content, 'html.parser')

        league = soup.find('table', id='btable').text
        league = league.split()

        print(f"Processando: {league_name}")
        
        # tratamento de dados das partidas num arquivo csv
        generateLeagueCSV(league)

        # calculo das medias das proximas partidas 
        processNextMatches("league.csv", "league_averages.csv", "next_games.csv", league_name)

        # Ordenar csv com pandas
        sortCSV()

        arquivo = "final.csv"
        with open(arquivo, "r", encoding="utf-8") as f:
            conteudo = f.read()

        conteudo = conteudo.replace(" , ", " ")

        with open(arquivo, "w", encoding="utf-8") as f:
            f.write(conteudo)

        print("Arquivo atualizado com sucesso!")



    except Exception as erro:
        print("Liga encerrada")
        print(erro)
        corruptedLeagues.append(cont - 1)


