#from bs4 import BeautifulSoup
#import requests
import os
#import datetime
from pathlib import Path
import logging

str2 = 'parei em nenhum flag'
str3 = 'str3 vazia'

# Criando a pasta leagues caso não exista
output_dir = Path("leagues")
output_dir.mkdir(parents=True, exist_ok=True)

os.makedirs("logs", exist_ok=True)               
logging.basicConfig(filename="logs/debugs.log", level=logging.DEBUG, format="%(message)s")
logger = logging.getLogger(__name__)



def scrapeSoup (matches, textFile, i, league_name):

    conttt = 0
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    next_matches_home = []
    next_matches_away = []
    next_matches_date = []
    return_list = []
    lines2 = []
    str8 = 'estou no ultimo elemento' 
    str3 = 'str3 vazia'
    day2 = ''
    indexador = 0
    cont = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    home2 = ""
    away2 = ""
    home3 = ""
    day = matches[0][-3] + matches[0][-2] + matches[0][-1]
    day = day + ' ' + matches[1] + ' '
    day_match = []
    home_team = []
    away_team = []
    result = []
    home = ""
    away = ""
    res = ""
    flag = 2
    del matches[0]
    del matches[0]
    flag2 = 0
    flag3 = 2
    flag4 = 0

    for index in range(len(matches)):
        #try:
            ix = index     

            if "eers" in textFile:
                logger.info("element: %r", matches[ix])
                logger.info("Flag atual: %s", flag) 
                if flag == 6:
                    logger.info("Flag3: %s", flag3)

                logger.info("\n\n")



            if (matches[index].find('+') == -1 or matches[index].find('-') == -1) and flag != 5 and flag != 6:
                if flag == 1:
                    day += matches[index] + ' '
                    flag = 2

                elif flag == 2:
                    day += matches[index][:3]
                    day_match.append(day)
                    day = ''
                    if matches[index + 2] == '-': 
                        home += matches[index][3:]
                
                    else: 
                        home += matches[index][3:] + ' '
                    flag = 3
        
                elif flag == 3:
                    if index == len(matches) - 1:
                        indexador = index
                        str2 = "parei no flag 3"
                        os.system("pause")
                        break
                    if matches[index + 1].isdigit() == True and matches[index + 2] == '-' :
                        home += matches[index]
                        home_team.append(home)
                        home = ""
                        flag = 4
            
                    elif matches[index].isdigit() == True and matches[index + 1] == '-': 
                        home_team.append(home)
                        home = ""
                        res += matches[index] + ' '
                        flag = 4
                    elif matches[index].find('pp.') != -1 :
                        #print('alo')
                        home = ''
                        day_match.pop()
                        flag = 5
                        flag2 = 1
                    elif len(matches[index]) == 5 and matches[index][0].isdigit() == True and matches[index][1].isdigit() == True and matches[index][-1].isdigit() == True and matches[index][-2].isdigit() == True and matches[index][-3] == ':':
                            #print('Ola estou aqui')
                            str3 = 'to na condicao de "eers" in textFile correta'
                            str2 = 'to no flag 4'
                            cont2 = index - 1
                            cont5 = 0
                            cont6 = index-1
                            #print('entrando no loop infinito')
                            while True:
                                
                                if (len(matches[cont2]) > 3) and (matches[cont2][3].isupper() == True) and matches[cont2][2].islower() == True:
                                    ix = cont6 - cont5 + 1
                                    home2 += matches[cont2][3:]
                                    month = matches[cont2][:3]
                                    day3 = matches[cont2-1]
                                    week_day = matches[cont2-2][-3:]
                                    #print (matches[cont2-2])
                                    day2 += week_day + ' ' + day3 + ' ' + month
                                    next_matches_date.append(day2)
                                    day2 = ''   
                                    if matches[cont2 + 1].find(':') == -1:
                                        home2 += ' '
                                    while ix != index:
                                        if ix + 1 != index:
                                            home2 += matches[ix] + ' ' 
                                        else:
                                            home2 += matches[ix]
                                        ix += 1
                                    break
                                cont2 -= 1
                                cont5 += 1
                            #print(home2)
                            next_matches_home.append(home2)
                            home2 = ''
                            #print ('saindo do loop infinito')
                            indexador = index

                            if "eers" in textFile:
                                logger.info("Next matches home (flag 3): %s", next_matches_home[0])
                                logger.info("Next matches date (flag 3): %s\n\n", next_matches_date[0])
                            
                            flag = 6
                    else:
                        home += matches[index] + ' '
        
                elif flag == 4:
                    if matches[index].isdigit() == True and matches[index + 1] == "-":
                        res += matches[index] + ' '
                
                    elif matches[index].isdigit() == False and matches[index] == "-":
                        res += matches[index] + ' '

                    elif matches[index].isdigit() == True and matches[index -1] == "-":
                        res += matches[index]
                        result.append(res)
                        res = ''
                        flag = 5
                    else:
                        if len(matches[index]) == 5 and matches[index][0].isdigit() == True and matches[index][1].isdigit() == True and matches[index][-1].isdigit() == True and matches[index][-2].isdigit() == True and matches[index][-3] == ':':
                            #print('Ola')
                            next_matches_home.append(home_team[-1])
                            next_matches_date.append(day_match[-1])
                            home_team.pop()
                            day_match.pop()

                            if "eers" in textFile:
                                logger.info("Next matches home (flag 4): %s", next_matches_home[0])
                                logger.info("Next matches Date (flag 4): %s\n\n", next_matches_date[0])
                            str3 = 'to na condicao de "eers" in textFile correta'
                            flag = 6
                        else:
                            home_team.pop()
                            day_match.pop()
                            newIndex = jumpTo(index)
                            index = newIndex
                            #print ("Postponed")
                            #print( matches[index] )
                            day += matches[index][-2:]
                            flag = 2
                            away = ""
                            home = ""
            elif flag == 6:
                str2 = "parei no flag 6"
                indexador = index
                if index == (len(matches)) or cont3 == 34:
                    break
                else:
                    
                    if flag3 == 1:
                        if len(matches[index]) <= 2 and len(matches[index + 1]) > 3 and matches[index + 1][:3] in months and (matches[index + 1][3].isupper() == True or matches[index + 1][3].isdigit() == True):
                            day2 += matches[index] + ' '
                        
                        elif len(matches[index]) > 3 and matches[index][:3] in months and (matches[index][3].isupper() == True or matches[index][3].isdigit() == True):
                            day2 += matches[index][:3]
                            next_matches_date.append(day2)
                            day2 = ''
                            home3 += matches[index][3:]
                            cont3 += 1

                        elif len(matches[index]) <= 5 and matches[index].find(':') != -1:
                            flag3 = 2 
                            next_matches_home.append(home3)
                            home3 = ''
                            cont3 += 1

                        elif 'pp.' in matches[index]:
                            home3 = ''
                            day2 = ''
                            next_matches_date.pop()
                            newIndex = jumpTo(index)
                            index = newIndex
                            day2 += matches[index][-2:] + ' '
                            flag3 = 1
                            cont3 -= 1
                        
                        else: 
                            home3 += ' ' + matches[index]
                    
                    elif flag3 == 2:
                        if "eers" in textFile:
                            logger.info("Dentro do flag3: 2")
                        
                        aux = ""
                        weekDays = ['Sat', 'Sun', 'Wed', 'Fri', 'Thu', 'Tue', 'Mon']
                        
                        if len(matches[ix]) > 3:
                            aux = matches[ix][-3:]

                        if aux in weekDays:
                            if "eers" in textFile:
                                logger.info("Dentro da if de cadastro do team away")
                            if index != len(matches) - 1:
                                away2 += matches[index][:-3]
                                
                                next_matches_away.append(away2)
                                day2 += matches[index][-3:] + ' '
                                
                                away2 = ''
                                flag3 = 1
                                cont3 += 1
                                
                                
                            else:
                                away2 += matches[index]
                                next_matches_away.append(away2)
                                away2 = ''
                                str8 = 'parei no ultimo elemento'
                                cont3 += 1
                        else:
                            if "eers" in textFile:
                                logger.info("Dentro do else de cadastro do team away")
                            away2 += matches[index] + ' '

                '''if "eers" in textFile:
                    logger.info("Next matches home: %s", next_matches_home[-1])

                    if len(next_matches_away) > 0:
                        logger.info("Next matches away: %s", next_matches_away[-1])
                    
                    logger.info("Next matches date: %s\n\n", next_matches_date[-1])'''
                            
            else:
                if "eers" in textFile:
                    logger.info("Ultimo else das flags\n")
                    
                    
                if matches[index].find('+') != -1 or matches[index].find('-') != -1:
                    contt = 0
                    
                    for caracter in range( 0 , len(matches[index])):
                        #print (caracter)
                        if matches[index][caracter] == '+' or matches[index][caracter] == '-':
                            contt += 1
                            #print(contt)
                    
                    if contt >= 2:
                        if matches[index].find('(') != -1:
                            
                            tamanhoo = len(matches[index]) - 10

                            away += matches[index][:tamanhoo]

                            if away.endswith('('):
                                away = away[:-1]
                            
                            if len(away) >= 2 and away[-2] == ('('):
                                away = away[:-2]

                            away_team.append(away)
                            away = ''
                
                            day += matches[index][-3:] + ' '
                        else:
                            
                            tamanhoo = len(matches[index]) - 5
                            away += matches[index][:tamanhoo]
                            
                            if away.endswith('('):
                                away = away[:-1]
                            
                            if len(away) >= 2 and away[-2] == ('('):
                                away = away[:-2]
                            
                            away_team.append(away)
                            away = ''

                            day += matches[index][-3:] + ' '

                        flag = 1
                    
                else:
                    away += matches[index] + ' '
                    flag = 5                                                                                        
    
            def jumpTo(index):
                cont = index
                while len(matches[cont]) > 3 and matches[cont][:3] in months and (matches[cont][3].isupper() == True or matches[cont][3].isdigit() == True):
                    cont += 1
            
                return cont - 1
            
    # Resolve o caminho absoluto (útil para debug)
    textFile = str(textFile)  # garante str se vier Path
    output_path = (output_dir / textFile).resolve()
    temp_path = output_path.with_suffix(output_path.suffix + ".tmp")  # leagues/arquivo.txt.tmp

    with open(temp_path, "w") as arq:
        for index in range(len(away_team)):
            if len(home_team) > index:
                arq.write(f"{day_match[index]} , {home_team[index]} , {result[index]} , {away_team[index]}\n")
                #print('To aqyu')
            else:
                if len(result) > index:
                    arq.write(f"{day_match[index]} , NULL , {result[index]} , {away_team[index]}\n")
                    print('To aqyu 2')
    
    temp_path.replace(output_path)

    lines3 = []

    for index in range(15):
        if index >= len(next_matches_home) - 1 or index >= len(next_matches_date) - 1 or index >= len(next_matches_away) - 1:
            break
        lines3.append(next_matches_date[index])
        lines3.append(next_matches_home[index])
        lines3.append(next_matches_away[index])
        return_list.append(lines3)   
    if len(return_list) > 0: 
        #print (return_list[0][1])
        pass
    
    #print (return_list)
    return return_list


