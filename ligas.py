from listasSocccerStats import files_total


leagues_dict = []
leagues_dict.append('serie_a')
leagues_dict.append('serie_b')
leagues_dict.append('bundesliga')
leagues_dict.append('bundesliga-2')
leagues_dict.append('2__bundesliga')
leagues_dict.append('3__liga')
leagues_dict.append('regionalliga')
leagues_dict.append('la_liga')
leagues_dict.append('la_liga_2')
leagues_dict.append('premier_league')
leagues_dict.append('the_championship')
leagues_dict.append('league_one')
leagues_dict.append('primeira_liga')
leagues_dict.append('ligapro')
leagues_dict.append('liga_profesional_argentina')
leagues_dict.append('jupiler_pro_league')
leagues_dict.append('challenger_pro_league')
leagues_dict.append('brasileirao_serie_a')
leagues_dict.append('brasileirao_serie_b')
leagues_dict.append('brasileirao_serie_c')
leagues_dict.append('primera_chile')
leagues_dict.append('super_league')
leagues_dict.append('super_league-2')
leagues_dict.append('liga_betplay_dimayor')
leagues_dict.append('1__hnl_league')
leagues_dict.append('superligaen')
leagues_dict.append('1st_division')
leagues_dict.append('liga_pro')
leagues_dict.append('ligue_1')
leagues_dict.append('ligue_2')
leagues_dict.append('nb_1')
leagues_dict.append('premier_division')
leagues_dict.append('liga_mx')
leagues_dict.append('liga_mx-2')
leagues_dict.append('eredivisie')
leagues_dict.append('eerste_divisie')
leagues_dict.append('eliteserien')
leagues_dict.append('obos-ligaen')
leagues_dict.append('primera_paraguay')
leagues_dict.append('liga_1')
leagues_dict.append('ekstraklasa')
leagues_dict.append('liga_1-2')
leagues_dict.append('superettan')

with open('ligas.txt', 'w') as arq:
    for item in range(len(files_total)):
        arq.write(f'{files_total[item]} - {leagues_dict[item]}\n')                  