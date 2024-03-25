import scrapyStatsSoup2 as sss
from listasSocccerStats import leagues
from listasSocccerStats import files_total
import statistics_1 as stats
import writeOnFile
import keys

'''
scrapeUni = ApiUnibet()
UniBetLinks = scrapeUni.competitions()
tupleUni = UniBetLinks.items()

uniLinks = keys.organizing_keys(tupleUni)

writeOnFile.write(uniLinks, scrapeUni, "Unibet.txt")
'''
'''
dict_leagues = {
    "serie_a": "italy1.txt",
    "serie_b": "italy2.txt",
    "bundesliga": "germany1.txt",
    "bundesliga": "austria1.txt",
    "2__bundesliga": "germany2.txt",
    "3__liga": "germany4.txt",
    "regionalliga_nord": "germany5.txt",
    "la_liga": "spain1.txt",
    "la_liga_2": "spain2.txt",
    "premier_league": "england1.txt",
    "the_championship": "england2.txt",
    "league_one": "england3.txt",
    "primeira_liga": "portugal1.txt",
    "ligapro": "portugal2.txt",
    "liga_profesional_argentina": "argentina1.txt",
    "jupiler_pro_league": "belgium1.txt",
    "challenger_pro_league": "belgium2.txt",
    "brasileirao_serie_a": "brazil1.txt",
    "brasileirao_serie_b": "brazil2.txt",
    "brasileirao_serie_c": "brazil3.txt",
    "primera_chile": "chile1.txt",
    "super_league": "china1.txt", 
    "super_league": "greece1.txt",
    "liga_betplay_dimayor": "colombia1.txt",
    "1__hnl_league": "croatia1.txt",
    "superligaen": "denmark1.txt",
    "1st_division": "denmark2.txt",
    "liga_pro": "ecuador1.txt",
    "veikkausliiga": "finland1.txt",
    "ligue_1": "france1.txt",
    "ligue_2": "france2.txt",
    "nb_1": "hungary1.txt",
    "premier_division": "ireland1.txt",
    "liga_mx": "mexico1.txt", 
    "liga_mx": "mexico2.txt",
    "eredivisie": "eredivise.txt",
    "eerste_divisie": "eerste.txt",
    "eliteserien": "norway1.txt",
    "obos-ligaen": "norway2.txt",
    "primera_paraguay": "paraguay1.txt",
    "liga_1": "peru1.txt",
    "ekstraklasa": "poland1.txt",
    "liga_1": "romania1.txt",
    "superettan": "sweden2.txt"
}
'''

leagues_dict = []
leagues_dict.append('Serie A , Italy')
leagues_dict.append('Serie B , Italy')
leagues_dict.append('Bundesliga , Germany')
leagues_dict.append('Bundesliga , Austria')
leagues_dict.append('2 Bundesliga , Germany')
leagues_dict.append('3 Liga , Germany')
leagues_dict.append('Regionalliga Nord , Germany')
leagues_dict.append('La Liga , Spain')
leagues_dict.append('La liga 2 , Spain')
leagues_dict.append('Premier League , England')
leagues_dict.append('The Championship , England')
leagues_dict.append('League One , England')
leagues_dict.append('Primeira Liga , Portugal')
leagues_dict.append('Liga Pro , Portugal')
leagues_dict.append('Liga Profesional Argentina , Argentina')
leagues_dict.append('Jupiler Pro League , Belgium')
leagues_dict.append('Challenger Pro League , Belgium')
leagues_dict.append('Brasileirao Serie A , Brazil')
leagues_dict.append('Brasileirao Serie B , Brazil')
leagues_dict.append('Brasileirao Serie C , Brazil')
leagues_dict.append('Primera Chile , Chile')
leagues_dict.append('Super League , China')
leagues_dict.append('Super League , Greece')
leagues_dict.append('Liga Betplay Dimayor , Colombia')
leagues_dict.append('1 HNL League , Croatia')
leagues_dict.append('Superligaen , Denmark')
leagues_dict.append('1st Division , Denmark')
leagues_dict.append('Liga Pro , Ecuador')
leagues_dict.append('Ligue 1 , France')
leagues_dict.append('Ligue 2 , France')
leagues_dict.append('NB 1 , Hungary')
leagues_dict.append('Premier Division , Ireland')
leagues_dict.append('Liga MX , Mexico')
leagues_dict.append('Liga MX , Mexico')
leagues_dict.append('Eredivisie , Netherlands')
leagues_dict.append('Eerste Divisie , Netherlands')
leagues_dict.append('Eliteserien , Norway')
leagues_dict.append('Obos Ligaen , Norway')
leagues_dict.append('Primera Paraguay , Paraguay')
leagues_dict.append('Liga 1 , Peru')
leagues_dict.append('Ekstraklasa , Polland')
leagues_dict.append('liga 1 , Romenia')
leagues_dict.append('Superettan , Sweden')
leagues_dict.append('Veikkausliiga , Finland')
leagues_dict.append('Ykkonen , Finland')
leagues_dict.append('Meistriliiga , Estonia')
leagues_dict.append('K-League-1 , South Korea')
leagues_dict.append('Brasileirao Serie D , Brazil')
leagues_dict.append('J1 League , Japan')
leagues_dict.append('J2 League , Japan')
leagues_dict.append('J3 League , Japan')
leagues_dict.append('Urvalsdeild , Iceland')
leagues_dict.append('1. Deild , Iceland')
leagues_dict.append('2. Deild , Iceland')
leagues_dict.append('3. Deild , Iceland')
leagues_dict.append('A Lyga , Lithuania')
leagues_dict.append('K-League-2 , South Korea')
leagues_dict.append('K3 League , South Korea')
leagues_dict.append('Malasya Super League , Malasya')
leagues_dict.append('Myanmar National League , Myanmar')
leagues_dict.append('Major League Soccer , USA')
leagues_dict.append('USL Championship , USA')
leagues_dict.append('USL League 2 , USA')
leagues_dict.append('Primera Division , Venezuela')
leagues_dict.append('Primera B , Chile')


average_goals = 0
average_goalsConceded = 0


'''
for item in files_total:
    ind = files_total.index(item)
    print(f'File: {item} | League: {leagues_dict[ind]}')
'''
    
final_list = []
aux_list = []
lines = []
aux = []
averages_list = []
team = ''
cont = 1
flag = 0
primary_key = 1

nextGames_list = []
aux_list_2 = [] 


def find_index (textFile):
    for item in files_total:
        if item == textFile:
            return item.index()



for ind in range(len(leagues)):
    cont += 1
    aux_list_2 = sss.scrapeSoup(leagues[ind], files_total[ind], ind, leagues_dict[ind])
    if len(aux_list_2) > 0:
        aux_list_2 = aux_list_2[0]
    nextGames_list.append(aux_list_2)
    aux_list_2 = []
    
underTwohalf_home = 0    


conta = 0


championships_average_goals = stats.statistics_averages(files_total)
print('\n\n')
print(len(championships_average_goals))

def find_average(homeTeam, awayTeam, ind, conta):
    conta += 1

    try:
        global underTwohalf_home
        average = 0
        cont = 0
        goals_home = 0
        goals_away = 0
        conceded_home = 0
        conceded_away = 0
        overOnehalf_home = 0
        overOneHalf_away = 0
        for team in championships_average_goals[ind]:
            
            if team[0] == homeTeam:
                average += team[-4] + team[-2]
                goals_home = team[-4]
                conceded_home = team[-2]
                overOnehalf_home = team[7]
                games_total = team[5] + team[6]
                overOnehalf_home = float(overOnehalf_home)
                underTwohalf_home = team[9]
                underTwohalf_home = float(underTwohalf_home)
                if team[5]!= 0:
                    overOnehalf_home = round((overOnehalf_home/team[5])*100 , 2)
                    underTwohalf_home = round((underTwohalf_home/team[5])*100 , 2)
                else:
                    overOnehalf_home = 0
                    underTwohalf_home = 0
                #print(f'{team[0]} - {team[7]} - {overOnehalf_home}')
                cont += 1

            elif team[0] == awayTeam:
                goals_away = team[-3]
                conceded_away = team[-1]
                average += team[-3] + team[-1]
                overOneHalf_away = team[8]
                games_total = team[5] + team[6]
                overOneHalf_away = float(overOneHalf_away)
                if team[6] != 0:
                    overOneHalf_away = round((overOneHalf_away/team[6])*100 , 2)
                else:
                    overOneHalf_away = 0
                underTwohalf_away = team[10]
                underTwohalf_away = float(underTwohalf_away)
                if team[6] != 0:
                    underTwohalf_away = round((underTwohalf_away/team[6])*100 , 2)
                else:
                    underTwohalf_away = 0
                #print(f'{team[0]} - {team[7]} - {overOneHalf_away}')
                cont +=1
            
            elif cont == 2:
                average = float(average)
                average = round(average / 2, 2)
                break
        total = goals_away + goals_home + conceded_home + conceded_away
        if average == total:
            average = round(average / 2, 2)
        elif average > total - 0.3 and average < total + 0.3:
            average = round(average / 2, 2)
        

        return average, overOnehalf_home, overOneHalf_away, underTwohalf_home, underTwohalf_away , conta
    except:
        print ("Entrei no except")
        print(conta)
        input()
        return average, overOnehalf_home, overOneHalf_away, underTwohalf_home, 0, conta

def sort_list (averages_list):
    aux_list_3 = []
    larger = 0.0
    larger = float(larger)
    flag = 0

    for loop in range(len(averages_list)):
        for league in averages_list:
            for game2 in league:
                print(game2)
                '''
                if float(game2[3]) > larger:
                    larger = game2
                    flag = 1
                    ind1 = averages_list.index(league)
                    ind2 = league.index(game2)
                '''
        '''
        if flag != 0:
            aux_list_3.append(larger)
            del averages_list[ind1][ind2]
            larger = 0.0
            larger = float(larger)
            flag = 0
        '''
    return aux_list_3
     

with open("statistics.txt", "w") as arq2:    
    for league in championships_average_goals:
        for team in league:
            for attributes in team:
                if (type(attributes) is int) or (type(attributes) is float):
                    aux = str(attributes)
                    arq2.write(f'{aux} ')
                else:
                    arq2.write(f'{attributes} ')
            arq2.write('\n')
        arq2.write('---------------------------------------------------------\n')

lines = []
game = []
print (len(nextGames_list))
print (type(nextGames_list[0]))
cont7 = 0
cont8 = 0 

for league in nextGames_list:
    ind = nextGames_list.index(league)
    conta = 0
    for item in league:
    
        if ind != 5:
            
            game.append(item)
            cont7 += 1
            if cont7 == 3:
                average = find_average(game[1], game[2], ind , conta)
                print(average)
                lines.append(game[0])
                lines.append(game[1])
                lines.append(game[2])
                lines.append(average[0])
                lines.append(average[1])
                lines.append(average[2])
                lines.append(average[3])
                lines.append(average[4])
                lines.append(leagues_dict[ind])
                averages_list.append(lines)
                conta = average[-1]
                game = []
                lines = []
                cont7 = 0
    if cont8 == 1:
        break 
    
#averages_list = sort_list(averages_list)
    
with open ("next_games.txt" , "w") as arq:
    for i in range(len(averages_list)):
        arq.write(f"{averages_list[i][0]} , {averages_list[i][1]} x {averages_list[i][2]} , Average: {averages_list[i][3]} , Home Over 1.5 goals: {averages_list[i][4]}% , Away Over 1.5 goals: {averages_list[i][5]}% , Home Under 2.5 goals: {averages_list[i][6]}% , Away Under 2.5 goals: {averages_list[i][7]}% , {averages_list[i][8]} \n")



'''         
with open("unibet.txt", "r", errors="ignore") as arq:
    team_name = ''
    
    matches = arq.readlines()
    for match in matches:
        attributes = match.split(' , ')
        for league in leagues_dict:
            if '-2' in league:
                aux2 = league.replace ('-2', '')
                flag =1
            if attributes[0] == league:
                home_team = attributes[2]
                away_team = attributes[3]
                current_file_index = leagues_dict.index(league)
                for team in championships_average_goals[current_file_index]:
                    #aux = team.split()
                    if ' ' in team[0]:
                        aux3 = team[0].split()
                        team_name = aux3[0]
                        for z_item in aux3:
                            if len(z_item) > len(team):
                                team_name = z_item    
                    else:
                        team_name = aux
                    if team_name in home_team:
                        average_goals += team[-4]
                        average_goalsConceded += team[-2]
                    elif team_name in away_team:
                        average_goals += team[-3]
                        average_goalsConceded += team[-1]
                        average = round((float(average_goals) + float(average_goalsConceded))/2 , 4)
                        lines.append(home_team)
                        lines.append(away_team)
                        lines.append(average)
                        lines.append(primary_key)
                        aux_list.append(lines)
                        averages_list.append(average)
                        averages_list.append(primary_key)
                        lines = []
                        primary_key += 1
                        average_goals = 0
                        average_goalsConceded = 0
                        team_name = ''
    '''  
'''           
    averages_list = sorted(averages_list, reverse = True)
    for averages in averages_list:
        for item in aux_list:
            if averages == item[2]:
                lines.append(item[0])
                lines.append(item[1])
                lines.append(averages)
                final_list.append(lines)
                lines = []
    '''
'''
print(len(aux_list))
with open("final-list.txt", "w") as arq3:
    for match in aux_list:
        arq3.write(f'{match[0]} x {match[1]} | Media: {match[2]}\n')


'''
    

                        






    
    




