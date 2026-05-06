from bs4 import BeautifulSoup
import requests
import psycopg2

urls = []
leagues = []
files_total = []
leagues_dict = []
cont = 1


headers = {
    "Accept-Encoding": "identity"
}

urls.append('https://www.soccerstats.com/results.asp?league=italy&pmtype=bydate')
leagues_dict.append('Serie A , Italy')

urls.append('https://www.soccerstats.com/results.asp?league=italy2&pmtype=bydate')
leagues_dict.append('Serie B , Italy')

urls.append('https://www.soccerstats.com/results.asp?league=germany&pmtype=bydate')
leagues_dict.append('Bundesliga , Germany')

urls.append('https://www.soccerstats.com/results.asp?league=austria&pmtype=bydate')
leagues_dict.append('Bundesliga , Austria')

urls.append('https://www.soccerstats.com/results.asp?league=germany2&pmtype=bydate')
leagues_dict.append('2 Bundesliga , Germany')

urls.append('https://www.soccerstats.com/results.asp?league=germany3&pmtype=bydate')
leagues_dict.append('3 Liga , Germany')

urls.append('https://www.soccerstats.com/results.asp?league=germany4&pmtype=bydate')
leagues_dict.append('Regionalliga Nord , Germany')

urls.append('https://www.soccerstats.com/results.asp?league=spain&pmtype=bydate')
leagues_dict.append('La Liga , Spain')

urls.append('https://www.soccerstats.com/results.asp?league=spain2&pmtype=bydate')
leagues_dict.append('La liga 2 , Spain')

urls.append('https://www.soccerstats.com/results.asp?league=england&pmtype=bydate')
leagues_dict.append('Premier League , England')

urls.append('https://www.soccerstats.com/results.asp?league=england2&pmtype=bydate')
leagues_dict.append('The Championship , England')

urls.append('https://www.soccerstats.com/results.asp?league=england3&pmtype=bydate')
leagues_dict.append('League One , England')

urls.append('https://www.soccerstats.com/results.asp?league=portugal&pmtype=bydate')
leagues_dict.append('Primeira Liga , Portugal')

urls.append('https://www.soccerstats.com/results.asp?league=portugal2&pmtype=bydate')
leagues_dict.append('Liga Pro , Portugal')

urls.append('https://www.soccerstats.com/results.asp?league=argentina&pmtype=bydate')
leagues_dict.append('Liga Profesional Argentina , Argentina')

urls.append('https://www.soccerstats.com/results.asp?league=belgium&pmtype=bydate')
leagues_dict.append('Jupiler Pro League , Belgium')

urls.append('https://www.soccerstats.com/results.asp?league=belgium2&pmtype=bydate')
leagues_dict.append('Challenger Pro League , Belgium')

urls.append('https://www.soccerstats.com/results.asp?league=brazil&pmtype=bydate')
leagues_dict.append('Brasileirao Serie A , Brazil')

urls.append('https://www.soccerstats.com/results.asp?league=brazil2&pmtype=bydate')
leagues_dict.append('Brasileirao Serie B , Brazil')

urls.append('https://www.soccerstats.com/results.asp?league=brazil3&pmtype=bydate')
leagues_dict.append('Brasileirao Serie C , Brazil')

urls.append('https://www.soccerstats.com/results.asp?league=chile&pmtype=bydate')
leagues_dict.append('Primera Chile , Chile')

urls.append('https://www.soccerstats.com/results.asp?league=china&pmtype=bydate')
leagues_dict.append('Super League , China')

urls.append('https://www.soccerstats.com/results.asp?league=greece&pmtype=bydate')
leagues_dict.append('Super League , Greece')

urls.append('https://www.soccerstats.com/results.asp?league=colombia&pmtype=bydate')
leagues_dict.append('Liga Betplay Dimayor , Colombia')

urls.append('https://www.soccerstats.com/results.asp?league=croatia&pmtype=bydate')
leagues_dict.append('1 HNL League , Croatia')


urls.append('https://www.soccerstats.com/results.asp?league=denmark&pmtype=bydate')
leagues_dict.append('Superligaen , Denmark')

urls.append('https://www.soccerstats.com/results.asp?league=denmark2&pmtype=bydate')
leagues_dict.append('1st Division , Denmark')

urls.append('https://www.soccerstats.com/results.asp?league=ecuador&pmtype=bydate')
leagues_dict.append('Liga Pro , Ecuador')

urls.append('https://www.soccerstats.com/results.asp?league=france&pmtype=bydate')
leagues_dict.append('Ligue 1 , France')

urls.append('https://www.soccerstats.com/results.asp?league=france2&pmtype=bydate')
leagues_dict.append('Ligue 2 , France')

urls.append('https://www.soccerstats.com/results.asp?league=hungary&pmtype=bydate')
leagues_dict.append('NB 1 , Hungary')

urls.append('https://www.soccerstats.com/results.asp?league=ireland&pmtype=bydate')
leagues_dict.append('Premier Division , Ireland')

urls.append('https://www.soccerstats.com/results.asp?league=mexico&pmtype=bydate')
leagues_dict.append('Liga MX , Mexico')

urls.append('https://www.soccerstats.com/results.asp?league=mexico2&pmtype=bydate')
leagues_dict.append('Liga MX , Mexico')

urls.append('https://www.soccerstats.com/results.asp?league=netherlands&pmtype=bydate')
leagues_dict.append('Eredivisie , Netherlands')

urls.append('https://www.soccerstats.com/results.asp?league=netherlands2&pmtype=bydate')
leagues_dict.append('Eerste Divisie , Netherlands')

urls.append('https://www.soccerstats.com/results.asp?league=norway&pmtype=bydate')
leagues_dict.append('Eliteserien , Norway')

urls.append('https://www.soccerstats.com/results.asp?league=norway2&pmtype=bydate')
leagues_dict.append('Obos Ligaen , Norway')

urls.append('https://www.soccerstats.com/results.asp?league=paraguay&pmtype=bydate')
leagues_dict.append('Primera Paraguay , Paraguay')

urls.append('https://www.soccerstats.com/results.asp?league=peru&pmtype=bydate')
leagues_dict.append('Liga 1 , Peru')

urls.append('https://www.soccerstats.com/results.asp?league=poland&pmtype=bydate')
leagues_dict.append('Ekstraklasa , Polland')

urls.append('https://www.soccerstats.com/results.asp?league=romania&pmtype=bydate')
leagues_dict.append('liga 1 , Romenia')

urls.append('https://www.soccerstats.com/results.asp?league=sweden2&pmtype=bydate')
leagues_dict.append('Superettan , Sweden')

urls.append('https://www.soccerstats.com/results.asp?league=finland&pmtype=bydate')
leagues_dict.append('Veikkausliiga , Finland')

urls.append('https://www.soccerstats.com/results.asp?league=finland2&pmtype=bydate')
leagues_dict.append('Ykkonen , Finland')

urls.append('https://www.soccerstats.com/results.asp?league=estonia&pmtype=bydate')
leagues_dict.append('Meistriliiga , Estonia')

urls.append('https://www.soccerstats.com/results.asp?league=southkorea&pmtype=bydate')
leagues_dict.append('K-League-1 , South Korea')

urls.append('https://www.soccerstats.com/results.asp?league=brazil4&pmtype=bydate')
leagues_dict.append('Brasileirao Serie D , Brazil')

urls.append('https://www.soccerstats.com/results.asp?league=japan&pmtype=bydate')
leagues_dict.append('J1 League , Japan')

urls.append('https://www.soccerstats.com/results.asp?league=japan2&pmtype=bydate')
leagues_dict.append('J2 League , Japan')

urls.append('https://www.soccerstats.com/results.asp?league=japan3&pmtype=bydate')
leagues_dict.append('J3 League , Japan')

urls.append('https://www.soccerstats.com/results.asp?league=iceland&pmtype=bydate')
leagues_dict.append('Urvalsdeild , Iceland')

urls.append('https://www.soccerstats.com/results.asp?league=iceland2&pmtype=bydate')
leagues_dict.append('1. Deild , Iceland')

urls.append('https://www.soccerstats.com/results.asp?league=iceland3&pmtype=bydate')
leagues_dict.append('2. Deild , Iceland')

urls.append('https://www.soccerstats.com/results.asp?league=iceland4&pmtype=bydate')
leagues_dict.append('3. Deild , Iceland')

urls.append('https://www.soccerstats.com/results.asp?league=lithuania&pmtype=bydate')
leagues_dict.append('A Lyga , Lithuania')

urls.append('https://www.soccerstats.com/results.asp?league=southkorea2&pmtype=bydate')
leagues_dict.append('K-League-2 , South Korea')

urls.append('https://www.soccerstats.com/results.asp?league=southkorea3&pmtype=bydate')
leagues_dict.append('K3 League , South Korea')

urls.append('https://www.soccerstats.com/results.asp?league=malaysia&pmtype=bydate')
leagues_dict.append('Malasya Super League , Malasya')

urls.append('https://www.soccerstats.com/results.asp?league=myanmar&pmtype=bydate')
leagues_dict.append('Myanmar National League , Myanmar')

urls.append('https://www.soccerstats.com/results.asp?league=usa&pmtype=bydate')
leagues_dict.append('Major League Soccer , USA')

urls.append('https://www.soccerstats.com/results.asp?league=usa2&pmtype=bydate')
leagues_dict.append('USL Championship , USA')

urls.append('https://www.soccerstats.com/results.asp?league=usa3&pmtype=bydate')
leagues_dict.append('USL League 2 , USA')

urls.append('https://www.soccerstats.com/results.asp?league=venezuela&pmtype=bydate')
leagues_dict.append('Primera Division , Venezuela')

urls.append('https://www.soccerstats.com/results.asp?league=chile2&pmtype=bydate')
leagues_dict.append('Primera B , Chile')

print(len(urls))

conn = psycopg2.connect(
    dbname="bestBet",
    user="postgres",
    password="446123ABpp",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

dados = list(zip(urls, leagues_dict))

cursor.executemany("""
    INSERT INTO leagues (url, leagueName)
    VALUES (%s, %s)
""", dados)

conn.commit()

cursor.close()
conn.close()



























    


