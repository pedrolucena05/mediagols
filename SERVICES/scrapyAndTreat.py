from MODELS.populateTable import urls
from bs4 import BeautifulSoup
import requests
import psycopg2
from treatMatches import generateLeagueCSV
from calculateTeamsAverages import processNextMatches


conn = psycopg2.connect(
    dbname="bestBet",
    user="postgres",
    password="446123ABpp",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()


headers = {
    "Accept-Encoding": "identity"
}

corruptedLeagues = []

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

        # cálculo das medias das proximas partidas 
        processNextMatches("league.csv", "league_averages.csv", "next_games.csv", league_name)

    except Exception as erro:
        print("Liga encerrada")
        print(erro)
        corruptedLeagues.append(cont - 1)