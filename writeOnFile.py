

def write (links, api, file):
    with open(str(file), "w", encoding="utf-8") as arq:
        cont = 0
        for k_item in links:
            try:
                odds = api.odds(str(k_item))
                for j_item in odds:
                    cont += 1
                    
                    championship = k_item.split('/')

                    print(championship[-2])
                    arq.write(f"\n{championship[-2]} , ") 
                    arq.write(f"{test(j_item['time'])} , ")
                    arq.write(f"{test(j_item['home_team'])} , ")
                    arq.write(f"{test(j_item['away_team'])} , ")
                
                    if j_item['full_time_result'] is not None:
                        arq.write(f"{test(j_item['full_time_result']['1'])} , ")
                        arq.write(f"{test(j_item['full_time_result']['X'])} , ")
                        arq.write(f"{test(j_item['full_time_result']['2'])} , ")
                    else:
                        arq.write("  ,   ,   ,  ")
                
                    if j_item['under_over'] is not None:
                        arq.write(f"{test(j_item['under_over']['O2.5'])} , ")
                        arq.write(f"{test(j_item['under_over']['U2.5'])} , ")
                    else:
                        arq.write("  ,   ,  ")   
                
                    if j_item['both_teams_to_score'] is not None:
                        arq.write(f"{test(j_item['both_teams_to_score']['yes'])}")
                        arq.write(f"{test(j_item['both_teams_to_score']['no'])} , ")
                    else:
                        arq.write("  ,   ,  ")
                
                    if j_item['double_chance'] is not None:
                        arq.write(f"{test(j_item['double_chance']['1X'])} , ")
                        arq.write(f"{test(j_item['double_chance']['12'])} , ")
                        arq.write(f"{test(j_item['double_chance']['2X'])}")
                    else:
                        arq.write("  ,   ,   ,  ")
            except:
                print(f'Erro no link: {k_item}')

            


def test(item):
    if item is not None:
        return item
    else:
        return "  , "
        
    


