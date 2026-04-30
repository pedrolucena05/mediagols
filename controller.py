import SERVICES.scrapyStatsSoup as sss
from MODELS.populateTable import leagues, files_total, corruptedLeagues, leagues_dict

import pandas as pd


average_goals = 0
average_goalsConceded = 0
    
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



corruptedInd = len(corruptedLeagues)
corruptedFlag = False

base = 0
for ind in range(len(leagues)):
    cont += 1
    
    # busca binária para verificar se a liga selecionada 
    lo = 0
    hi = len(corruptedLeagues) - 1
    corruptedFlag = False

    while lo <= hi:
        mid = (lo + hi) // 2 # posição central
        mid_val = corruptedLeagues[mid] # valor nessa posição

        if mid_val == ind:
            corruptedFlag = True
            break
        elif mid_val < ind:
            
            lo = mid + 1
        else:
            
            hi = mid - 1

    # Se a liga estiver em recesso , pula para a proxima
    if corruptedFlag:
        continue
    
    # Armazenando as ligas que não estão em recesso
    with open("logs/meu_arquivo.log", "a") as f:
        f.write(f" {files_total[ind]} , {ind} , {leagues_dict[ind]}\n")
    
    aux_list_2 = sss.scrapeSoup(leagues[ind], files_total[ind], ind, leagues_dict[ind])
    
    if len(aux_list_2) > 0:
        aux_list_2 = aux_list_2[0]
    nextGames_list.append(aux_list_2)
    aux_list_2 = []
    
underTwohalf_home = 0    


conta = 0


championships_average_goals = statistics_averages(files_total)

for item in files_total:

    lo = 0
    hi = len(corruptedLeagues) - 1
    corruptedFlag = False

    while lo <= hi:
        mid = (lo + hi) // 2            # posição central
        mid_val = corruptedLeagues[mid] # valor nessa posição

        if mid_val == ind:
            corruptedFlag = True
            break
        elif mid_val < ind:
            
            lo = mid + 1
        else:
            
            hi = mid - 1

    # Se a liga estiver em recesso , pula para a proxima
    if corruptedFlag:
        continue

    df_matches, team_stats = analyze_file(item)

    with open("pandas.log", "a") as f:
        f.write(f"Dataframe de partidas (exemplo):\n")
        f.write(f"{df_matches.head()}\n")
        f.write(f"Estatísticas por time:\n")
        f.write(f"Estatísticas por time:\n")
        pd.set_option("display.max_columns", None)
        f.write(f"{team_stats}\n\n")



def find_average(homeTeam, awayTeam, ind, conta):
        conta += 1
        underTwohalf_away = -1
    #try:
        global underTwohalf_home
        average = 0
        cont = 0
        goals_home = 0
        goals_away = 0
        conceded_home = 0
        conceded_away = 0
        overOnehalf_home = 0
        overOneHalf_away = 0
        if len(championships_average_goals) > 0: 
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
    #except:
    #    print ("Entrei no except")
    #    print(conta)
        
    #    return average, overOnehalf_home, overOneHalf_away, underTwohalf_home, 0, conta

def sort_list (averages_list):
    aux_list_3 = []
    larger = 0.0
    larger = float(larger)
    flag = 0

    for loop in range(len(averages_list)):
        for league in averages_list:
            for game2 in league:
                #print(game2)
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
#print (len(nextGames_list))
#print (type(nextGames_list[0]))
cont7 = 0
cont8 = 0 

for league in nextGames_list:
    ind = nextGames_list.index(league)
    conta = 0
    for item in league:
    
        if ind != 5:
            
            game.append(item)
            cont7 += 1
            if cont7 == 3 and len(game) >= 3:
                average = find_average(game[1], game[2], ind , conta)
                #print(average)
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

#print ("next games")
#print (nextGames_list)

#print ("\n\nNext games averages")
#print (averages_list)
with open ("next_games.txt" , "w") as arq:
    for i in range(len(averages_list)):
        arq.write(f"{averages_list[i][0]} , {averages_list[i][1]} x {averages_list[i][2]} , Average: {averages_list[i][3]} , Home Over 1.5 goals: {averages_list[i][4]}% , Away Over 1.5 goals: {averages_list[i][5]}% , Home Under 2.5 goals: {averages_list[i][6]}% , Away Under 2.5 goals: {averages_list[i][7]}% , {averages_list[i][8]} \n")


    

                        






    
    




