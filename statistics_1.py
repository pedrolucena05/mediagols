





#try:




def statistics_averages(files):
    championships_average_goals = []
    cont = 0
    cont1 = 0
    cont2 = 0
    cont3 = 1
    for item in files:
                #print (f'League: {cont3}')
                #cont3 += 1
                teams = []
                def find_team(team):
                    for index in range(0, len(teams)):
                        if teams[index][0] == team:
                            return index
                    return -1

                def addLines_and_team (team, goalsHome, goalsAway, home_goalsConceded, away_goalsConceded, matches_home, matches_away, overOnehalf_home, overOnehalf_away, underTwoHaf_home, underTwoHalf_away):
                    lines = []
                    overOnehalf_home = int(overOnehalf_home)
                    overOnehalf_away = int(overOnehalf_away)
                    lines.append(team)
                    lines.append(goalsHome)
                    lines.append(goalsAway)
                    lines.append(home_goalsConceded)
                    lines.append(away_goalsConceded)
                    lines.append(matches_home)
                    lines.append(matches_away)
                    lines.append(overOnehalf_home)
                    lines.append(overOnehalf_away)
                    lines.append(underTwoHaf_home)
                    lines.append(underTwoHalf_away)
                    teams.append(lines)

                def addTeams (home, result, away):
                    if result.find('pp.') != -1:
                        return
                    result = result.split(' - ')
            
                    result[0]= int(result[0])
                    result[1]= int(result[1])

                    home_goalsHome= result[0]
                    home_goalsConceded= result[1]

                    away_goalsAway = result[1]
                    away_goalsConceded = result[0]

        
                    if (find_team(home) == -1 and find_team(away) == -1):
                        if result[0] + result[1] > 1:
                            if result[0] + result[1] <=2:
                                    addLines_and_team(home, home_goalsHome, 0 , home_goalsConceded, 0 , 1 , 0 , 1 , 0, 1, 0)
                                    addLines_and_team(away, 0 , away_goalsAway, 0 , away_goalsConceded, 0 , 1 , 0 , 1, 0, 1)
                            else:
                                    addLines_and_team(home, home_goalsHome, 0 , home_goalsConceded, 0 , 1 , 0 , 1 , 0, 0, 0)
                                    addLines_and_team(away, 0 , away_goalsAway, 0 , away_goalsConceded, 0 , 1 , 0 , 1, 0, 0)
                        else:
                            if result[0] + result[1] <=2:
                                    addLines_and_team(home, home_goalsHome, 0 , home_goalsConceded, 0 , 1 , 0 , 0, 0, 1, 0)
                                    addLines_and_team(away, 0 , away_goalsAway, 0 , away_goalsConceded, 0 , 1 , 0, 0, 0, 1) 
                            else:
                                    addLines_and_team(home, home_goalsHome, 0 , home_goalsConceded, 0 , 1 , 0 , 0, 0, 0, 0)
                                    addLines_and_team(away, 0 , away_goalsAway, 0 , away_goalsConceded, 0 , 1 , 0, 0, 0, 0)
        
                    elif find_team(home) != -1 and find_team(away) != -1:
                        index1 = find_team(home)
                        teams[index1][1] += home_goalsHome
                        teams[index1][3] += home_goalsConceded
                        teams[index1][5] += 1

                        index2 = find_team(away)
                        teams[index2][2] += result[1]
                        teams[index2][4] += result[0]
                        teams[index2][6] += 1

                        if result[0] + result[1] > 1:
                            teams[index1][7] +=1
                            teams[index2][8] +=1
                        
                        if result[0] + result[1] <= 2:
                                teams[index1][9] +=1
                                teams[index2][10] +=1
                        
                    elif (find_team(home) == -1 and find_team(away) != -1):
                        if result[0] + result[1] > 1:
                             overOnehalf = 1
                        else:
                             overOnehalf = 0

                        if result[0] + result[1] <= 2:
                                 underTwoHalf = 1
                        else:
                                 underTwoHalf = 0

                        addLines_and_team(home, home_goalsHome, 0, home_goalsConceded, 0, 1, 0, overOnehalf, 0, underTwoHalf, 0)

                        index= find_team(away)
                        teams[index][2] += result[1]
                        teams[index][4] += result[0]
                        teams[index][6] += 1
                        teams[index][7] += overOnehalf
                        teams[index][10] += underTwoHalf

                    elif (find_team(home) != -1 and find_team(away) == -1):
                        if result[0] + result[1] > 1:
                             overOnehalf = 1
                        else:
                             overOnehalf = 0
                        if result[0] + result[1] <= 2:
                                 underTwoHalf = 1
                        else:
                                 underTwoHalf = 0 
                        addLines_and_team(away, 0 , away_goalsAway, 0, away_goalsConceded, 0, 1, 0, overOnehalf, 0, underTwoHalf)
            
                        index = find_team(home)
                        teams[index][1] += home_goalsHome
                        teams[index][3] += home_goalsConceded
                        teams[index][5] += 1
                        teams[index][8] += overOnehalf
                        teams[index][9] += underTwoHalf
                
                
                try:    
                    with open (item, "r") as arq:
                        content = arq.readlines()
                        for item in content:
                            i = item.split(' , ')
                            i[-1]=i[-1].replace('\n', '')
                            addTeams (i[1], i[2], i[3])
                            cont1 += 1
    
                        for item in teams:
                            cont2 += 1

                            if teams.index(item) == 1:
                                 pass
                
                            if item[5] > 0:
                                goals_home_average = round(float(item[1]) / float(item[5]) , 2)
                                goalsConceded_home_average = round(float(item[3]) / float(item[5]) , 2)
                            if item[6] > 0: 
                                goals_away_average = round(float(item[2]) / float(item[6]) , 2)
                                goalsConceded_away_average = round(float(item[4]) / float(item[6]) , 2)
            
                            item.append(goals_home_average)
                            item.append(goals_away_average)
                            item.append(goalsConceded_home_average)
                            item.append(goalsConceded_away_average)
                        championships_average_goals.append(teams)
                except:
                    print('entrei no except')
                    print (item)
                           
    return championships_average_goals
    
        
#except:
#    print(files[index])


        


                        


    
