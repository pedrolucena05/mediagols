from bs4 import BeautifulSoup
import requests
import os
import datetime

str2 = 'parei em nenhum flag'
str3 = 'str3 vazia'


def scrapeSoup (matches, textFile, i, league_name):
    #try:
        
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
        day = matches[0][-2] + matches[0][-1]
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
                        elif len(matches[index]) == 5 and matches[index][0].isdigit() == True and matches[index][1].isdigit() == True and matches[index][-1].isdigit() == True and matches[index][-2].isdigit() == True:
                                #print('Ola estou aqui')
                                str3 = 'to na condicao de parada correta'
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
                                        week_day = matches[cont2-2][-2:]
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
                            if len(matches[index]) == 5 and matches[index][0].isdigit() == True and matches[index][1].isdigit() == True and matches[index][-1].isdigit() == True and matches[index][-2].isdigit() == True:
                                print('Ola')
                                home_team.pop()
                                next_matches_home.append(matches[index])
                                str3 = 'to na condicao de parada correta'
                                flag = 6
                            else:
                                home_team.pop()
                                day_match.pop()
                                jump = jumpTo(index)
                                index += jump
                                day += matches[index][-2:]
                                flag = 1
                elif flag == 6:
                    str2 = "parei no flag 6"
                    indexador = index
                    if index == (len(matches)) or cont3 == 14:
                        break
                    else:
                        if flag3 == 1:
                            if ((index+1) < len(matches)) and matches[index+1].find(':') != -1:
                                flag3 = 2
                                if (len(matches[index]) > 3) and (matches[index][3].isupper() == True or matches[index][3].isdigit() == True) and matches[index][2].islower() == True:
                                    home2 += matches[index][3:]
                                    day2 += matches[index-2][-2:] + ' '
                                    day2 += matches[index-1] + ' '
                                    day2 += matches[index][:3]
                                    next_matches_date.append(day2)
                                    day2 = ''
                                    if home2[2] == ' ':
                                        home2 = home2[3:]
                                        if home2[-1] == ' ':
                                            home2 = home2[:-1]
                                        next_matches_home.append(home2)
                                        home2 = ''
                                    elif home2[1] == ' ':
                                        home2 = home2[2:]
                                        if home2[-1] == ' ':
                                            home2= home2[:-1] 
                                        next_matches_home.append(home2)
                                        home2 = ''
                                else:
                                    home2 += matches[index]
                                    cont2 = index - 1
                                    cont5 = 0
                                    cont6 = index-1
                                    while True:
                                    
                                        if (len(matches[cont2]) > 3) and (matches[cont2][3].isupper() == True or matches[cont2][3].isdigit() == True) and matches[cont2][2].islower() == True:
                                            ix = cont6 - cont5 + 1
                                            month = matches[cont2][:3]
                                            day3 = matches[cont2-1]
                                            week_day = matches[cont2-2][-2:]
                                            day2 += week_day + ' ' + day3 + ' ' + month
                                            next_matches_date.append(day2)
                                            day2 = ''   
                                            if matches[cont2 + 1].find(':') == -1:
                                                home2 += ' '
                                            while ix != index:
                                                ix += 1
                                            break
                                        cont2 -= 1
                                        cont5 += 1

                                    if ( len(matches[index]) > 2 ) and matches[index][2] == ' ':
                                        home2 = home2[3:]
                                        if home2[0] == ' ':
                                            #print (home2)
                                            #os.system("pause")
                                            home2 = home2[1:]
                                        if home2[-1] == ' ':
                                            home2 = home2[:-1]
                                        next_matches_home.append(home2)
                                        home2 = '' 
                                    else:
                                        home2 = home2[2:]
                                        if home2[0] == ' ':
                                            home2 = home2[1:]
                                            #print (home2)
                                            #os.system("pause")
                                        if home2[-1] == ' ':
                                            home2 = home2[:-1]
                                        next_matches_home.append(home2)
                                        home2 = ''
                            else:
                                if (len(matches[index]) > 3) and (matches[index][3].isupper() == True or matches[index][3].isdigit() == True) and matches[index][2].islower() == True:
                                    home2 += matches[index][3:] + ' '
                                else:
                                    home2 += matches[index] + ' '
                        
                        elif flag3 == 2:
                            if matches[index].find('h2h') != -1:
                                if index != len(matches) - 1:
                                    away2 += matches[index][:-5]
                                    if flag4 != 0:
                                        away2 = away2[6:]
                                        next_matches_away.append(away2)
                                        away2 = ''
                                        flag3 = 1
                                    else:
                                        next_matches_away.append(away2)
                                        away2 = ''
                                        flag3 = 1
                                        flag4 = 1
                                else:
                                    away2 += matches[index][:-3]
                                    next_matches_away.append(away2)
                                    away2 = ''
                                    str8 = 'parei no ultimo elemento'
                            else:
                                away2 += matches[index] + ' '
                else:
                    if flag2 == 1:
                        if len(matches[index]) > 1:  
                            if matches[index][-2].isupper() and matches[index][-1].islower() and matches[index + 1].isdigit():
                                day += matches[index][-2]
                                day += matches[index][-1] + ' '
                                flag = 1    
                                flag2 = 0

                    
                    
                    elif matches[index].find('stats') == -1 and matches[index].find('(') == -1:
                        if matches[index].find('+') != -1 or matches[index].find('-') != -1:
                            indexes = [i for i, c in enumerate(matches[index]) if c == '+' or c == '-']
                            if len(indexes) >= 2:
                                away += matches[index][:indexes[-2]]
                            away_team.append(away)
                            away = ''
                            if len(indexes)>=1:
                                day += matches[index][indexes[-1] + 1:] + ' '
                            flag = 1
                        else:
                            away += matches[index] + ' '
            
                    elif matches[index].find('stats') != -1 and matches[index].find('(') != -1:
                        matches[index] = matches[index].replace('stats', '')
                        ind = matches[index].find('(')
                        away += matches[index][:ind]
                        away_team.append(away)
                        away.split()
                        matches[index] = matches[index].replace(away[-1], '')
                        away = ''
                        str = ''
                        for i in range(5):
                            str += matches[index][i]
                        matches[index] = matches[index].replace(str, '') 
                        indexes = [i for i, c in enumerate(matches[index]) if c == '+' or c == '-']
                        day += matches[index][indexes[-1] + 1:] + ' ' 
                        flag = 1

                    elif matches[index].find('(') != -1 and matches[index].find('stats') == -1:
                        ind = matches[index].find('(')
                        away += matches[index][:ind]
                        away = ''
                        indexes = [i for i, c in enumerate(matches[index]) if c == '+' or c == '-']
                        day += matches[index][indexes[-1]:]
                        flag = 1
            
                    elif matches[index].find('(') == -1 and matches[index].find('stats') != -1:
                        matches[index] = matches[index].replace('stats', '')
                        indexes = [i for i, c in enumerate(matches[index]) if c == '+' or c == '-']
                        away += matches[index][:indexes[-2]]
                        away_team.append(away)
                        away = ''
                        day += matches[index][indexes[-1] + 1:] + ' ' 
                        flag = 1
                    else:
                        day += matches[index][-2]
                        day += matches[index][-1]
                        day += ' '
                        flag = 1
                    

        
                def jumpTo(index):
                    cont = index
                    while len(matches[cont]) > 2 and matches[cont] < '0' and matches[cont] > '9':
                        cont += 1
                
                    return cont - 1
                cont += 1
   
        print("\n\n\nListas apos o scrapesoup\n\n\n")
       
        print(away_team)
        print("\n\n\nFIm do screpe")
        with open(textFile, "w") as arq:
            for index in range(len(away_team)):
                if len(home_team) > index:
                    arq.write(f"{day_match[index]} , {home_team[index]} , {result[index]} , {away_team[index]}\n")
                else:
                    if len(result) > index:
                        arq.write(f"{day_match[index]} , NULL , {result[index]} , {away_team[index]}\n")
        lines3 = []

        for index in range(15):
            if index >= len(next_matches_home) - 1 or index >= len(next_matches_date) - 1 or index >= len(next_matches_away) - 1:
                break
            lines3.append(next_matches_date[index])
            lines3.append(next_matches_home[index])
            lines3.append(next_matches_away[index])
            return_list.append(lines3)   
        if len(return_list) > 0: 
            print (return_list[0][1])
        
        return return_list

       



