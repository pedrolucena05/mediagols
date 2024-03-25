Fiz essa aplicação para pegar a media de gols de times de diversas ligas de futebol, faço a leitura do site soccerstats.com e o algoritmo organiza os dados como no arquivo 
england1.txt. Outro algoritmo calcula a média de gols dos times, a porcentagem de partidas que tiveram acima de 1.5 gols e abaixo de 2.5 gols. E no arquivo next_games.txt
mostra as partidas que vão ter com as medias dos times que vão se enfrentar. 

O código acabou ficando complexo por causa que os dados extraidos do site vinham da seguinte forma:

['2.5+TGBTSFr', '29', 'JulUnion', 'Tornesch', '2', '-', '2', 'Altona+4+Su', '31', 'JulPaloma', '2', '-', '1', 'Rugenbergen+3+Su', '31', 'JulT.', 'Wilhelmsburg', 
'3', '-', '1', 'HEBC+4+Su', '31', 'JulNiendorfer', 'TSV', '1', '-', '0', 'Victoria', 'H.', 'B-1-Su', '31', 'JulBuchholz', '2', '-', '5', 'Eimsbutteler', 'TV+7+Su', 
'31', 'JulHamm', 'Utd', '1', '-', '1', 'Harksheide-2+Su', '31', 'JulOsdorf', '1', '-', '5', 'Curslack-N.+6+Su', '31', 'JulSasel', '4', '-', '0', 'Süderelbe+4-Su', 
'31', 'JulHamburger', 'SV', 'C', '0', '-', '2', 'W.', 'Concordia-2-Fr', '5', 'AugSüderelbe', '1', '-', '2', 'Paloma+3+Fr', '5', 'AugHarksheide', '1', '-', '0', 'T.', 
'Wilhelmsburg-1-Fr', '5', 'AugVictoria', 'H.', 'B', '3', '-', '2', 'Hamburger', 'SV', 'C+5+Fr', '5', 'AugW.', 'Concordia', '4', '-', '0', 'Buchholz+4-Fr', '5', 
'AugEimsbutteler', 'TV', '3', '-', '0', 'Dassendorfstats+3-Sa', '6', 'AugRugenbergen', '0', '-', '2', 'Niendorfer', 'TSVstats-2-Sa', '6', 'AugCurslack-N.', '1', '-', 
'1', 'Hamm', 'Utdstats-2+Sa', '6', 'AugAltona', '2', '-', '1', 'Osdorfstats+3+Fr', '12', 'AugDassendorf', '4', '-', '2', 'W.', 'Concordiastats+6+Fr', '12', 'AugHamm', 
'Utd', '2', '-', '1', 'Altonastats+3+Fr', '12', 'AugHamburger', 'SV', 'C', '3', '-', '0', 'Rugenbergenstats+3-Su', '14', 'AugPaloma', '1', '-', '1', 'HEBCstats-2+Su', 
'14', 'AugT.', 'Wilhelmsburg', '4', '-', '1', 'Curslack-N.stats+5+Su', '14', 'AugNiendorfer', 'TSV', '6', '-', '2', 'Süderelbestats+8+Su', '14', 'AugBuchholz', '1', 
'-', '4', 'Victoria', 'H.', 'Bstats+5+Su', '14', 'AugSasel', '5', '-', '1', 'Harksheidestats+6+Su', '14', 'AugUnion', 'Tornesch', '1', '-', '0', 'Osdorfstats-1-Fr', 
'19', 'AugSüderelbe', '7', '-', '0', 'Hamburger', 'SV', 'Cstats+7-Fr', '19', 'AugHarksheide', '3', '-', '0', 'Palomastats+3-Fr', '19', 'AugOsdorf', '1', '-', '3', 
'Hamm', 'Utdstats+4+Fr', '19', 'AugVictoria', 'H.', 'B', '2', '-', '1', 'Dassendorfstats+3+Fr', '19', 'AugEimsbutteler', 'TV', '1', '-', '1', 'Union', 
'Torneschstats-2+Sa', '20', 'AugCurslack-N.', '1', '-', '3', 'Saselstats+4+Sa', '20', 'AugAltona', '3', '-', '3', 'T.', 'Wilhelmsburgstats+6+Su', '21', 
'AugRugenbergen', '4', '-', '1', 'Buchholzstats+5+Tu', '23', 'AugBuchholz', '2', '-', '0', 'Süderelbestats-2-Tu', '23', 'AugT.', 'Wilhelmsburg', '0', '-', '1', 
'Osdorfstats-1-Tu', '23', 'AugDassendorf', '4', '-', '1', 'Rugenbergenstats+5+Tu', '23', 'AugSasel', '4', '-', '2', 'Altonastats+6+Tu', '23', 'AugEimsbutteler', 
'TV', '2', '-', '1', 'W.', 'Concordiastats+3+Tu', '23', 'AugNiendorfer', 'TSV', '6', '-', '1', 'Harksheidestats+7+Tu', '23', 'AugPaloma', '6', '-', '1', 
'Curslack-N.stats+7+Tu', '23', 'AugUnion', 'Tornesch', '0', '-', '0', 'Hamm', 'Utdstats-0-Fr', '26', 'AugSüderelbe', '0', '-', '0', 'Dassendorfstats-0-Fr', '26', 
'AugHamm', 'Utd', '2', '-', '0', 'T.', 'Wilhelmsburgstats-2-Fr', '26', 'AugHarksheide', '2', '-', '2', 'Hamburger', 'SV', 'Cstats+4+Fr', '26', 'AugOsdorf', '1', '-', 
'3', 'Saselstats+4+Fr', '26', 'AugVictoria', 'H.', 'B', '1', '-', '4', 'Eimsbutteler', 'TVstats+5+Fr', '26', 'AugW.', 'Concordia', '5', '-', '1', 'Union', 
'Torneschstats+6+Sa', '27', 'AugCurslack-N.', '2', '-', '2', 'Niendorfer', 'TSVstats+4+Sa', '27', 'AugAltona', '0', '-', '0', 'Palomastats-0-Su', '28', 'AugHEBC', 
'1', '-', '2', 'Buchholzstats+3+Fr', '2', 'SepW.', 'Concordia', '1', '-', '1', 'Victoria', 'H.', 'Bstats-2+Fr', '2', 'SepHamburger', 'SV', 'C', '4', '-', '0', 
'Curslack-N.stats+4-Fr', '2', 'SepEimsbutteler', 'TV', '5', '-', '0', 'Rugenbergenstats+5-Sa', '3', 'SepDassendorf', '2', '-', '0', 'HEBCstats-2-Sa', '3', 
'SepBuchholz', '2', '-', '1', 'Harksheidestats+3+Su', '4', 'SepPaloma', '5', '-', '0', 'Osdorfstats+5-Su', '4', 'SepNiendorfer', 'TSV', '0', '-', '2', 
'Altonastats-2-Su', '4', 'SepSasel', '2', '-', '3', 'Hamm', 'Utdstats+5+Su', '4', 'SepUnion', 'Tornesch', '0', '-', '3', 'T.', 'Wilhelmsburgstats+3-Fr', '9', 
'SepSüderelbe', '1', '-', '2', 'Eimsbutteler', 'TVstats+3+Fr', '9', 'SepHamm', 'Utd', '0', '-', '1', 'Palomastats-1-Fr', '9', 'SepHarksheide', '0', '-', '0', 
'Dassendorfstats-0-Fr', '9', 'SepOsdorf', '1', '-', '2', 'Niendorfer', 'TSVstats+3+Fr', '9', 'SepVictoria', 'H.', 'B', '1', '-', '0', 'Union', 'Torneschstats-1-Sa', 
'10', 'SepCurslack-N.', '1', '-', '0', 'Buchholzstats-1-Sa', '10', 'SepAltona', '2', '-', '0', 'Hamburger', 'SV', 'Cstats-2-Su', '11', 'SepT.', 'Wilhelmsburg', '1', 
'-', '1', 'Saselstats-2+Su', '11', 'SepRugenbergen', '0', '-', '3', 'W.', 'Concordiastats+3-Tu', '13', 'SepBuchholz', '1', '-', '2', 'Altonastats+3+Tu', '13', 
'SepDassendorf', '4', '-', '0', 'Curslack-N.stats+4-Tu', '13', 'SepEimsbutteler', 'TV', '1', '-', '1', 'HEBCstats-2+Tu', '13', 'SepNiendorfer', 'TSV', '4', '-', '1', 
'Hamm', 'Utdstats+5+Tu', '13', 'SepPaloma', '3', '-', '0', 'T.', 'Wilhelmsburgstats+3-Tu', '13', 'SepUnion', 'Tornesch', '1', '-', '6', 'Saselstats+7+Tu', '13', 
'SepVictoria', 'H.', 'B', '5', '-', '2', 'Rugenbergenstats+7+Tu', '13', 'SepW.', 'Concordia', '2', '-', '0', 'Süderelbestats-2-Tu', '13', 'SepHamburger', 'SV', 'C', 
'0', '-', '1', 'Osdorfstats-1-Fr', '16', 'SepSüderelbe', '2', '-', '2', 'Victoria', 'H.', 'Bstats+4+Fr', '16', 'SepHamm', 'Utd', '2', '-', '2', 'Hamburger', 'SV', 
'Cstats+4+Fr', '16', 'SepHarksheide', '0', '-', '0', 'Eimsbutteler', 'TVstats-0-Fr', '16', 'SepOsdorf', '0', '-', '2', 'Buchholzstats-2-Su', '18', 'SepHEBC', '4', 
'-', '1', 'W.', 'Concordiastats+5+Su', '18', 'SepRugenbergen', '1', '-', '6', 'Union', 'Torneschstats+7+Su', '18', 'SepSasel', '3', '-', '1', 'Palomastats+4+Fr', 
'23', 'SepVictoria', 'H.', 'B', '1', '-', '2', 'HEBCstats+3+Fr', '23', 'SepW.', 'Concordia', '2', '-', '2', 'Harksheidestats+4+Fr', '23', 'SepHamburger', 'SV', 'C', 
'0', '-', '3', 'T.', 'Wilhelmsburgstats+3-Fr', '23', 'SepEimsbutteler', 'TV', '7', '-', '1', 'Curslack-N.stats+8+Sa', '24', 'SepDassendorf', '4', '-', '1', 'Osdorfstats+5+Su', 
'25', 'SepNiendorfer', 'TSV', '3', '-', '1', 'Saselstats+4+Su', '25', 'SepBuchholz', '1', '-', '0', 'Hamm', 'Utdstats-1-Su', '25', 'SepUnion', 'Tornesch', '1', '-', 
'2', 'Palomastats+3+Tu', '27', 'SepHEBC', '1', '-', '4', 'Saselstats+5+Fr', '30', 'SepHEBC', '1', '-', '1', 'Rugenbergenstats-2+Fr', '30', 'SepSüderelbe', '6', '-', 
'1', 'Union', 'Torneschstats+7+Fr', '30', 'SepHamm', 'Utd', '0', '-', '5', 'Dassendorfstats+5-Fr', '30', 'SepHarksheide', '1', '-', '2', 'Victoria', 'H.', 
'Bstats+3+Fr', '30', 'SepPaloma', '3', '-', '2', 'Niendorfer', 'TSVstats+5+Fr', '30', 'SepHamburger', 'SV', 'C', '4', '-', '4', 'Saselstats+8+Sa', '1', 
'OctCurslack-N.', '0', '-', '3', 'W.', 'Concordiastats+3-Su', '2', 'OctT.', 'Wilhelmsburg', '2', '-', '2', 'Buchholzstats+4+Fr', '7', 'OctSüderelbe', '4', '-', '1', 
'HEBCstats+5+Fr', '7', 'OctVictoria', 'H.', 'B', '5', '-', '0', 'Curslack-N.stats+5-Fr', '7', 'OctW.', 'Concordia', '1', '-', '1', 'Altonastats-2+Fr', '7', 
'OctHamburger', 'SV', 'C', '0', '-', '2', 'Palomastats-2-Fr', '7', 'OctEimsbutteler', 'TV', '3', '-', '0', 'Osdorfstats+3-Sa', '8', 'OctDassendorf', '7', '-', '1', 
'T.', 'Wilhelmsburgstats+8+Su', '9', 'OctRugenbergen', '1', '-', '1', 'Harksheidestats-2+Su', '9', 'OctBuchholz', '1', '-', '3', 'Saselstats+4+Su', '9', 'OctUnion', 
'Tornesch', '2', '-', '1', 'Niendorfer', 'TSVstats+3+Tu', '11', 'OctAltona', '2', '-', '0', 'Victoria', 'H.', 'Bstats-2-Tu', '11', 'OctHarksheide', '3', '-', '0', 
'Süderelbestats+3-Tu', '11', 'OctHEBC', '1', '-', '1', 'Union', 'Torneschstats-2+Tu', '11', 'OctNiendorfer', 'TSV', '5', '-', '2', 'Hamburger', 'SV', 'Cstats+7+Tu', 
'11', 'OctOsdorf', '2', '-', '0', 'W.', 'Concordiastats-2-Tu', '11', 'OctPaloma', '0', '-', '0', 'Buchholzstats-0-Tu', '11', 'OctEimsbutteler', 'TV', '3', '-', '0', 
'Hamm', 'Utdstats+3-We', '12', 'OctCurslack-N.', '1', '-', '3', 'Rugenbergenstats+4+We', '12', 'OctSasel', '2', '-', '1', 'Dassendorfstats+3+Fr', '14', 
'OctSüderelbe', '4', '-', '3', 'Curslack-N.stats+7+Fr', '14', 'OctVictoria', 'H.', 'B', '6', '-', '2', 'Osdorfstats+8+Fr', '14', 'OctEimsbutteler', 'TV', '2', '-', 
'1', 'T.', 'Wilhelmsburgstats+3+Sa', '15', 'OctDassendorf', '6', '-', '0', 'Palomastats+6-Su', '16', 'OctHEBC', '2', '-', '0', 'Harksheidestats-2-Su', '16', 
'OctRugenbergen', '1', '-', '4', 'Altonastats+5+Su', '16', 'OctBuchholz', '1', '-', '3', 'Niendorfer', 'TSVstats+4+Su', '16', 'OctUnion', 'Tornesch', '2', '-', '1', 
'Hamburger', 'SV', 'Cstats+3+Tu', '18', 'OctHEBC', '1', '-', '2', 'Niendorfer', 'TSVstats+3+Fr', '21', 'OctHamm', 'Utd', '1', '-', '3', 'Victoria', 'H.', 
'Bstats+4+Fr', '21', 'OctHarksheide', '1', '-', '1', 'Union', 'Torneschstats-2+Fr', '21', 'OctOsdorf', '0', '-', '2', 'Rugenbergenstats-2-Fr', '21', 'OctW.', 
'Concordia', '2', '-', '0', 'T.', 'Wilhelmsburgstats-2-Fr', '21', 'OctHamburger', 'SV', 'C', '2', '-', '1', 'Buchholzstats+3+Sa', '22', 'OctCurslack-N.', '2', '-', 
'2', 'HEBCstats+4+Sa', '22', 'OctAltona', '0', '-', '3', 'Süderelbestats+3-Su', '23', 'OctNiendorfer', 'TSV', '1', '-', '1', 'Dassendorfstats-2+Su', '23', 'OctSasel', 
'2', '-', '1', 'Eimsbutteler', 'TVstats+3+Tu', '25', 'OctHamburger', 'SV', 'C', '3', '-', '2', 'HEBCstats+5+We', '26', 'OctAltona', '1', '-', '3', 
'Dassendorfstats+4+Fr', '28', 'OctSüderelbe', '2', '-', '2', 'Osdorfstats+4+Fr', '28', 'OctHarksheide', '3', '-', '3', 'Curslack-N.stats+6+Fr', '28', 'OctVictoria', 
'H.', 'B', '3', '-', '5', 'T.', 'Wilhelmsburgstats+8+Fr', '28', 'OctW.', 'Concordia', '0', '-', '1', 'Saselstats-1-Fr', '28', 'OctEimsbutteler', 'TV', '0', '-', '2', 
'Palomastats-2-Sa', '29', 'OctDassendorf', '4', '-', '0', 'Hamburger', 'SV', 'Cstats+4-Su', '30', 'OctHEBC', '0', '-', '2', 'Altonastats-2-Su', '30', 'OctUnion', 
'Tornesch', '1', '-', '2', 'Buchholzstats+3+Su', '30', 'OctRugenbergen', '0', '-', '3', 'Hamm', 'Utdstats+3-We', '2', 'NovAltona', '1', '-', '1', 'Eimsbutteler', 
'TVstats-2+Fr', '4', 'NovHamm', 'Utd', '1', '-', '5', 'Süderelbestats+6+Sa', '5', 'NovAltona', '1', '-', '0', 'Harksheidestats-1-Su', '6', 'NovPaloma', '3', 
'-', '3', 'W.', 'Concordiastats+6+Su', '6', 'NovOsdorf', '1', '-', '1', 'HEBCstats-2+Su', '6', 'NovT.', 'Wilhelmsburg', '2', '-', '0', 'Rugenbergenstats-2-Su', '6', 
'NovBuchholz', '0', '-', '4', 'Dassendorfstats+4-Su', '6', 'NovNiendorfer', 'TSV', '0', '-', '2', 'Eimsbutteler', 'TVstats-2-Su', '6', 'NovSasel', '1', '-', '1', 
'Victoria', 'H.', 'Bstats-2+Su', '6', 'NovUnion', 'Tornesch', '2', '-', '1', 'Curslack-N.stats+3+Fr', '11', 'NovSüderelbe', '2', '-', '2', 'T.', 
'Wilhelmsburgstats+4+Fr', '11', 'NovHarksheide', '2', '-', '1', 'Osdorfstats+3+Fr', '11', 'NovVictoria', 'H.', 'B', '0', '-', '3', 'Palomastats+3-Fr', '11', 
'NovEimsbutteler', 'TV', '2', '-', '1', 'Hamburger', 'SV', 'Cstats+3+Sa', '12', 'NovDassendorf', '4', '-', '1', 'Union', 'Torneschstats+5+Sa', '12', 
'NovCurslack-N.', '0', '-', '2', 'Altonastats-2-Su', '13', 'NovHEBC', '2', '-', '0', 'Hamm', 'Utdstats-2-Su', '13', 'NovW.', 'Concordia', '2', '-', '1', 
'Niendorfer', 'TSVstats+3+Su', '13', 'NovRugenbergen', '3', '-', '1', 'Saselstats+4+Fr', '18', 'NovSüderelbe', '0', '-', '2', 'Saselstats-2-Fr', '18', 
'NovHarksheide', '2', '-', '2', 'Hamm', 'Utdstats+4+Fr', '18', 'NovVictoria', 'H.', 'B', '5', '-', '2', 'Niendorfer', 'TSVstats+7+Fr', '18', 'NovW.', 'Concordia', 
'3', '-', '0', 'Hamburger', 'SV', 'Cstats+3-Fr', '18', 'NovEimsbutteler', 'TV', '1', '-', '1', 'Buchholzstats-2+Sa', '19', 'NovCurslack-N.', '3', '-', '3', 
'Osdorfstats+6+Sa', '19', 'NovAltona', '5', '-', '2', 'Union', 'Torneschstats+7+Su', '20', 'NovHEBC', '3', '-', '1', 'T.', 'Wilhelmsburgstats+4+Fr', '25', 'NovHamm', 
'Utd', '1', '-', '3', 'Curslack-N.stats+4+Fr', '25', 'NovOsdorf', '3', '-', '4', 'Altonastats+7+Fr', '25', 'NovHamburger', 'SV', 'C', '3', '-', '1', 'Victoria', 'H.', 
'Bstats+4+Sa', '26', 'NovDassendorf', '6', '-', '1', 'Eimsbutteler', 'TVstats+7+Su', '27', 'NovPaloma', '0', '-', '4', 'Süderelbestats+4-Su', '27', 'NovBuchholz', '1', 
'-', '3', 'W.', 'Concordiastats+4+Su', '27', 'NovNiendorfer', 'TSV', '2', '-', '1', 'Rugenbergenstats+3+Su', '27', 'NovSasel', '1', '-', '0', 'HEBCstats-1-Fr', '2', 
'DecSüderelbe', '2', '-', '1', 'Niendorfer', 'TSVstats+3+Fr', '2', 'DecHarksheide', '1', '-', '0', 'Saselstats-1-Fr', '2', 'DecOsdorf', '2', '-', '2', 'Union', 
'Torneschstats+4+Fr', '2', 'DecVictoria', 'H.', 'B', '3', '-', '2', 'Buchholzstats+5+Sa', '3', 'DecCurslack-N.', '0', '-', '3', 'T.', 'Wilhelmsburgstats+3-Sa', '3', 
'DecAltona', '3', '-', '0', 'Hamm', 'Utdstats+3-Su', '4', 'DecHEBC', '1', '-', '1', 'Palomastats-2+Su', '4', 'DecW.', 'Concordia', '1', '-', '3', 
'Dassendorfstats+4+Su', '4', 'DecRugenbergen', '2', '-', '2', 'Hamburger', 'SV', 'Cstats+4+Fr', '9', 'DecHamburger', 'SV', 'C', '0', '-', '4', 
'Süderelbestats+4-Sa', '10', 'DecT.', 'Wilhelmsburg', '2', '-', '0', 'Altonastats-2-Su', '11', 'DecUnion', 'Tornesch', '2', '-', '2', 'Eimsbutteler', 'TVstats+4+Su', 
'11', 'DecSasel', '5', '-', '2', 'Curslack-N.stats+7+Fr', '20', 'JanSüderelbe', '5', '-', '1', 'Buchholzstats+6+Fr', '20', 'JanHarksheide', '0', '-', '3', 'Niendorfer', 
'TSVstats+3-Fr', '20', 'JanOsdorf', '2', '-', '1', 'T.', 'Wilhelmsburgstats+3+Sa', '21', 'JanCurslack-N.', '0', '-', '1', 'Palomastats-1-Sa', '21', 'JanAltona', '2', 
'-', '1', 'Saselstats+3+Su', '22', 'JanHEBC', '2', '-', '1', 'Hamburger', 'SV', 'Cstats+3+Su', '22', 'JanW.', 'Concordia', '0', '-', '3', 'Eimsbutteler', 'TVstats+3-Fr', 
'27', 'JanHamburger', 'SV', 'C', '3', '-', '0', 'Harksheidestats+3-Fr', '27', 'JanEimsbutteler', 'TV', '2', '-', '0', 'Victoria', 'H.', 'Bstats-2-Sa', '28', 
'JanDassendorf', '3', '-', '3', 'Süderelbestats+6+Su', '29', 'JanPaloma', '0', '-', '4', 'Altonastats+4-Su', '29', 'JanT.', 'Wilhelmsburg', '3', '-', '1', 'Hamm', 
'Utdstats+4+Su', '29', 'JanBuchholz', '1', '-', '1', 'HEBCstats-2+Su', '29', 'JanNiendorfer', 'TSV', '2', '-', '2', 'Curslack-N.stats+4+Su', '29', 'JanUnion', 
'Tornesch', '1', '-', '4', 'W.', 'Concordiastats+5+Su', '29', 'JanSasel', '3', '-', '2', 'Osdorfstats+5+Fr', '3', 'FebHarksheide', '0', '-', '2', 'Buchholzstats-2-Fr', 
'3', 'FebOsdorf', '0', '-', '1', 'Palomastats-1-Fr', '3', 'FebVictoria', 'H.', 'B', '3', '-', '5', 'W.', 'Concordiastats+8+Sa', '4', 'FebCurslack-N.', '0', '-', '2', 
'Hamburger', 'SV', 'Cstats-2-Su', '5', 'FebHEBC', '0', '-', '0', 'Dassendorfstats-0-Fr', '10', 'FebHamburger', 'SV', 'C', '1', '-', '3', 'Altonastats+4+Fr', '10', 
'FebEimsbutteler', 'TV', '3', '-', '1', 'Süderelbestats+4+Sa', '11', 'FebDassendorf', '2', '-', '0', 'Harksheidestats-2-Su', '12', 'FebPaloma', '3', '-', '1', 'Hamm', 
'Utdstats+4+Su', '12', 'FebW.', 'Concordia', '0', '-', '1', 'Rugenbergenstats-1-Su', '12', 'FebBuchholz', '0', '-', '3', 'Curslack-N.stats+3-Su', '12', 'FebNiendorfer', 
'TSV', '4', '-', '0', 'Osdorfstats+4-Su', '12', 'FebUnion', 'Tornesch', '2', '-', '2', 'Victoria', 'H.', 'Bstats+4+Su', '12', 'FebSasel', '6', '-', '0', 'T.', 
'Wilhelmsburgstats+6-Tu', '14', 'FebPaloma', '2', '-', '3', 'Harksheidestats+5+Fr', '17', 'FebSüderelbe', '2', '-', '0', 'W.', 'Concordiastats-2-Fr', '17', 
'FebOsdorf', '3', '-', '2', 'Hamburger', 'SV', 'Cstats+5+Sa', '18', 'FebCurslack-N.', '2', '-', '2', 'Dassendorfstats+4+Su', '19', 'FebHEBC', '1', '-', '1', 
'Eimsbutteler', 'TVstats-2+Su', '19', 'FebRugenbergen', '0', '-', '2', 'Victoria', 'H.', 'Bstats-2-Su', '19', 'FebSasel', '8', '-', '0', 'Union', 'Torneschstats+8-Fr', 
'24', 'FebVictoria', 'H.', 'B', '0', '-', '3', 'Süderelbestats+3-Fr', '24', 'FebW.', 'Concordia', '1', '-', '2', 'HEBCstats+3+Fr', '24', 'FebHamburger', 'SV', 'C', 
'2', '-', '0', 'Hamm', 'Utdstats-2-Fr', '24', 'FebEimsbutteler', 'TV', '7', '-', '0', 'Harksheidestats+7-Su', '26', 'FebPaloma', '0', '-', '3', 'Saselstats+3-Su', 
'26', 'FebBuchholz', '1', '-', '0', 'Osdorfstats-1-Su', '26', 'FebNiendorfer', 'TSV', '3', '-', '2', 'T.', 'Wilhelmsburgstats+5+Su', '26', 'FebUnion', 'Tornesch', 
'2', '-', '1', 'Rugenbergenstats+3+Tu', '28', 'FebRugenbergen', 'pp.', 'PalomaFr', '3', 'MarSüderelbe', '0', '-', '2', 'Rugenbergenstats-2-Fr', '3', 'MarHarksheide', 
'1', '-', '1', 'W.', 'Concordiastats-2+Fr', '3', 'MarOsdorf', '0', '-', '4', 'Dassendorfstats+4-Sa', '4', 'MarCurslack-N.', '0', '-', '7', 'Eimsbutteler', 
'TVstats+7-Su', '5', 'MarHEBC', '3', '-', '2', 'Victoria', 'H.', 'Bstats+5+Su', '5', 'MarPaloma', '5', '-', '0', 'Union', 'Torneschstats+5-Su', '5', 'MarSasel', '1', 
'-', '1', 'Niendorfer', 'TSVstats-2+Fr', '17', 'MarVictoria', 'H.', 'B', '1', '-', '2', 'Harksheidestats+3+Fr', '17', 'MarW.', 'Concordia', '4', '-', '1', 
'Curslack-N.stats+5+Fr', '17', 'MarEimsbutteler', 'TV', '2', '-', '0', 'Altonastats-2-Sa', '18', 'MarDassendorf', '2', '-', '1', 'Hamm', 'Utdstats+3+Su', '19', 
'MarNiendorfer', 'TSV', '1', '-', '1', 'Palomastats-2+Su', '19', 'MarRugenbergen', '2', '-', '0', 'HEBCstats-2-Su', '19', 'MarBuchholz', '3', '-', '2', 'T.', 
'Wilhelmsburgstats+5+Su', '19', 'MarSasel', '4', '-', '1', 'Hamburger', 'SV', 'Cstats+5+Su', '19', 'MarUnion', 'Tornesch', '1', '-', '0', 'Süderelbestats-1-Tu', '21', 
'MarAltona', '4', '-', '1', 'Buchholzstats+5+Fr', '24', 'MarHarksheide', '1', '-', '0', 'Rugenbergenstats-1-Fr', '24', 'MarOsdorf', '3', '-', '3', 'Eimsbutteler', 
'TVstats+6+Sa', '25', 'MarCurslack-N.', '4', '-', '4', 'Victoria', 'H.', 'Bstats+8+Su', '26', 'MarHEBC', '4', '-', '1', 'Süderelbestats+5+Su', '26', 'MarPaloma', '5', 
'-', '2', 'Hamburger', 'SV', 'Cstats+7+Su', '26', 'MarNiendorfer', 'TSV', '3', '-', '0', 'Union', 'Torneschstats+3-Su', '26', 'MarSasel', '5', '-', '0', 
'Buchholzstats+5-Tu', '28', 'MarHamm', 'Utd', '4', '-', '2', 'Buchholzstats+6+We', '29', 'MarW.', 'Concordia', '4', '-', '3', 'Osdorfstats+7+Fr', '31', 
'MarSüderelbe', '4', '-', '0', 'Harksheidestats+4-Fr', '31', 'MarHamm', 'Utd', '0', '-', '0', 'Eimsbutteler', 'TVstats-0-Fr', '31', 'MarVictoria', 'H.', 'B', '2', 
'-', '3', 'Altonastats+5+Fr', '31', 'MarHamburger', 'SV', 'C', '1', '-', '3', 'Niendorfer', 'TSVstats+4+Sa', '1', 'AprDassendorf', '0', '-', '1', 'Saselstats-1-Su', 
'2', 'AprBuchholz', '0', '-', '1', 'Palomastats-1-Su', '2', 'AprUnion', 'Tornesch', '0', '-', '2', 'HEBCstats-2-Mo', '3', 'AprT.', 'Wilhelmsburg', '0', '-', '2', 
'Dassendorfstats-2-Tu', '4', 'AprHamm', 'Utd', '2', '-', '8', 'Saselstats+10+Th', '6', 'AprAltona', '4', '-', '1', 'Rugenbergenstats+5+Th', '6', 'AprCurslack-N.', '3', 
'-', '4', 'Süderelbestats+7+Th', '6', 'AprHarksheide', '1', '-', '1', 'HEBCstats-2+Th', '6', 'AprOsdorf', '1', '-', '4', 'Victoria', 'H.', 'Bstats+5+Th', '6', 
'AprHamburger', 'SV', 'C', '2', '-', '3', 'Union', 'Torneschstats+5+Fr', '7', 'AprPaloma', '2', '-', '2', 'Dassendorfstats+4+Fr', '7', 'AprT.', 'Wilhelmsburg', 
'0', '-', '1', 'Eimsbutteler', 'TVstats-1-Fr', '7', 'AprNiendorfer', 'TSV', '1', '-', '1', 'Buchholzstats-2+Sa', '8', 'AprRugenbergen', '6', '-', '3', 
'Curslack-N.stats+9+Mo', '10', 'AprDassendorf', '3', '-', '0', 'Altonastats+3-Mo', '10', 'AprT.', 'Wilhelmsburg', '1', '-', '3', 'Harksheidestats+4+Mo', '10', 
'AprNiendorfer', 'TSV', '2', '-', '1', 'HEBCstats+3+Mo', '10', 'AprBuchholz', '2', '-', '1', 'Rugenbergenstats+3+Mo', '10', 'AprHamm', 'Utd', '1', '-', '2', 
'Osdorfstats+3+Th', '13', 'AprT.', 'Wilhelmsburg', '2', '-', '1', 'Hamburger', 'SV', 'Cstats+3+Fr', '14', 'AprDassendorf', '3', '-', '2', 'Niendorfer', 
'TSVstats+5+Fr', '14', 'AprSüderelbe', '0', '-', '4', 'Altonastats+4-Fr', '14', 'AprVictoria', 'H.', 'B', '2', '-', '4', 'Hamm', 'Utdstats+6+Fr', '14', 
'AprEimsbutteler', 'TV', '2', '-', '1', 'Saselstats+3+Su', '16', 'AprHEBC', '4', '-', '2', 'Curslack-N.stats+6+Su', '16', 'AprT.', 'Wilhelmsburg', '6', 
'-', '2', 'W.', 'Concordiastats+8+Su', '16', 'AprRugenbergen', '2', '-', '1', 'Osdorfstats+3+Su', '16', 'AprBuchholz', '5', '-', '2', 'Hamburger', 'SV', 
'Cstats+7+Su', '16', 'AprUnion', 'Tornesch', '2', '-', '2', 'Harksheidestats+4+Tu', '18', 'AprRugenbergen', '2', '-', '2', 'Süderelbestats+4+Tu', '18', 
'AprDassendorf', '5', '-', '2', 'Victoria', 'H.', 'Bstats+7+We', '19', 'AprT.', 'Wilhelmsburg', '1', '-', '2', 'Niendorfer', 'TSVstats+3+We', '19', 'AprW.', 
'Concordia', '3', '-', '0', 'Hamm', 'Utdstats+3-Fr', '21', 'AprHamm', 'Utd', '1', '-', '0', 'Rugenbergenstats-1-Fr', '21', 'AprHamburger', 'SV', 'C', '4', '-', '3', 
'Dassendorfstats+7+Sa', '22', 'AprOsdorf', '0', '-', '5', 'Süderelbestats+5-Sa', '22', 'AprCurslack-N.', '2', '-', '3', 'Harksheidestats+5+Sa', '22', 'AprAltona', 
'3', '-', '2', 'HEBCstats+5+Su', '23', 'AprPaloma', '3', '-', '1', 'Eimsbutteler', 'TVstats+4+Su', '23', 'AprT.', 'Wilhelmsburg', '0', '-', '6', 'Victoria', 'H.', 
'Bstats+6-Su', '23', 'AprBuchholz', '1', '-', '1', 'Union', 'Torneschstats-2+Su', '23', 'AprSasel', '3', '-', '1', 'W.', 'Concordiastats+4+Tu', '25', 
'AprRugenbergen', '1', '-', '1', 'Palomastats-2+Tu', '25', 'AprAltona', '1', '-', '1', 'Niendorfer', 'TSVstats-2+Tu', '25', 'AprHamm', 'Utd', '4', '-', '1', 'W.', 
'Concordiastats+5+We', '26', 'AprT.', 'Wilhelmsburg', '3', '-', '4', 'Union', 'Torneschstats+7+Th', '27', 'AprRugenbergen', '2', '-', '2', 'Dassendorfstats+4+Fr', 
'28', 'AprSüderelbe', '17:00', 'Hamm', 'Utdh2hFr', '28', 'AprHarksheide', '17:30', 'Altonah2hFr', '28', 'AprVictoria', 'H.', 'B', '17:30', 'Saselh2hFr', '28', 'AprW.', 
'Concordia', '17:30', 'Palomah2hFr', '28', 'AprEimsbutteler', 'TV', '18:15', 'Niendorfer', 'TSVh2hSa', '29', 'AprCurslack-N.', '13:00', 'Union', 'Torneschh2hSu', '30', 
'AprHEBC', '08:45', 'Osdorfh2hSu', '30', 'AprRugenbergen', '12:00', 'T.', 'Wilhelmsburgh2hSu', '30', 'AprHamm', 'Utd', '13:00', 'Niendorfer', 'TSVh2hMo', '1', 
'MayDassendorf', '11:00', 'Buchholzh2hMo', '1', 'MayAltona', '12:00', 'W.', 'Concordiah2hTu', '2', 'MayRugenbergen', '16:30', 'Eimsbutteler', 
'TVh2hTu', '2', 'MayHamm', 'Utd', '17:00', 'Union', 'Torneschh2hTu', '2', 'MayT.', 'Wilhelmsburg', '17:00', 'Palomah2hFr', '5', 'MayHamm', 'Utd', '17:30', 
'HEBCh2hFr', '5', 'MayOsdorf', '17:30', 'Harksheideh2hFr', '5', 'MayHamburger', 'SV', 'C', '18:00', 'Eimsbutteler', 'TVh2hSa', '6', 'MayAltona', '12:00', 
'Curslack-N.h2hSu', '7', 'MayPaloma', '08:45', 'Victoria', 'H.', 'Bh2hSu', '7', 'MayT.', 'Wilhelmsburg', '11:00', 'Süderelbeh2hSu', '7', 'MayNiendorfer', 'TSV', 
'12:00', 'W.', 'Concordiah2hSu', '7', 'MaySasel', '13:00', 'Rugenbergenh2hSu', '7', 'MayUnion', 'Tornesch', '13:00', 'Dassendorfh2h']

Tive que organizar o vetor acima nesse arquivo de texto: 
'''
Fr 28 Jul , BW Lohne , 2 - 1 , Hannover 96 B
Fr 28 Jul , Meppen , 1 - 0 , Drochtersen/A.
Sa 29 Jul , Weiche F. , 0 - 5 , Teutonia O.
Su 30 Jul , Hamburger SV B , 0 - 5 , Norderstedt
Su 30 Jul , Havelse , 1 - 2 , Holstein Kiel B
Su 30 Jul , St. Pauli B , 1 - 1 , Jeddeloh
Su 30 Jul , Bremer SV , 2 - 2 , Kilia Kiel
Su 30 Jul , Spelle-Venhaus , 3 - 2 , Eimsbutteler
Sa 5 Aug , Hannover 96 B , 3 - 2 , Phonix Lubeck
Sa 5 Aug , Drochtersen/A. , 0 - 0 , Weiche F.
Sa 5 Aug , Bremer SV , 4 - 1 , Havelse
Su 6 Aug , Eimsbutteler , 1 - 4 , St. Pauli B
Su 6 Aug , Norderstedt , 2 - 0 , Spelle-Venhaus
Su 6 Aug , Teutonia O. , 3 - 0 , Hamburger SV B
Su 6 Aug , Oldenburg , 4 - 0 , Kilia Kiel
Fr 11 Aug , Kilia Kiel , 3 - 5 , Hannover 96 B
Fr 11 Aug , Weiche F. , 2 - 3 , Holstein Kiel B
Fr 11 Aug , Havelse , 2 - 0 , Oldenburg
Sa 12 Aug , Hamburger SV B , 1 - 1 , Drochtersen/A.
Sa 12 Aug , Phonix Lubeck , 7 - 0 , Jeddeloh
Sa 12 Aug , Meppen , 0 - 1 , Bremer SV
Sa 12 Aug , BW Lohne , 1 - 0 , Eimsbutteler
Su 13 Aug , Spelle-Venhaus , 1 - 6 , St. Pauli B
We 16 Aug , Phonix Lubeck , 5 - 1 , Oldenburg
We 16 Aug , Jeddeloh , 2 - 1 , Meppen
Sa 19 Aug , Hannover 96 B , 3 - 2 , Havelse
Sa 19 Aug , Teutonia O. , 2 - 1 , Spelle-Venhaus
Sa 19 Aug , Jeddeloh , 1 - 1 , Kilia Kiel
Sa 19 Aug , Drochtersen/A. , 1 - 3 , Norderstedt
Sa 19 Aug , Holstein Kiel B , 4 - 1 , Hamburger SV B
Su 20 Aug , Eimsbutteler , 0 - 3 , Phonix Lubeck
Su 20 Aug , St. Pauli B , 0 - 1 , BW Lohne
Su 20 Aug , Bremer SV , 0 - 0 , Weiche F.
Fr 25 Aug , Weiche F. , 2 - 2 , Oldenburg
Sa 26 Aug , Hamburger SV B , 3 - 1 , Bremer SV
Sa 26 Aug , Teutonia O. , 6 - 0 , Drochtersen/A.
Sa 26 Aug , Kilia Kiel , 2 - 1 , Eimsbutteler
Sa 26 Aug , Meppen , 5 - 2 , Hannover 96 B
Su 27 Aug , Havelse , 1 - 1 , Jeddeloh
Su 27 Aug , Norderstedt , 2 - 4 , Holstein Kiel B
Su 27 Aug , Phonix Lubeck , 0 - 5 , St. Pauli B
Su 27 Aug , Spelle-Venhaus , 0 - 1 , BW Lohne
Fr 1 Sep , Oldenburg , 0 - 0 , Hamburger SV B
Fr 1 Sep , Weiche F. , 1 - 1 , Hannover 96 B
Sa 2 Sep , Drochtersen/A. , 3 - 1 , Spelle-Venhaus
Sa 2 Sep , BW Lohne , 0 - 0 , Phonix Lubeck
Su 3 Sep , Eimsbutteler , 3 - 1 , Havelse
Su 3 Sep , Holstein Kiel B , 4 - 1 , Teutonia O.
Su 3 Sep , St. Pauli B , 2 - 2 , Kilia Kiel
Su 3 Sep , Bremer SV , 6 - 5 , Norderstedt
We 6 Sep , Oldenburg , 2 - 0 , Meppen
We 6 Sep , Norderstedt , 3 - 1 , Teutonia O.
Fr 8 Sep , Havelse , 1 - 1 , St. Pauli B
Sa 9 Sep , Weiche F. , 2 - 2 , Jeddeloh
Sa 9 Sep , Kilia Kiel , 0 - 2 , BW Lohne
Sa 9 Sep , Meppen , 1 - 0 , Eimsbutteler
Su 10 Sep , Teutonia O. , 3 - 1 , Bremer SV
Su 10 Sep , Norderstedt , 5 - 0 , Oldenburg
Su 10 Sep , Spelle-Venhaus , 0 - 4 , Phonix Lubeck
Su 10 Sep , Drochtersen/A. , 2 - 1 , Holstein Kiel B
Fr 15 Sep , Eimsbutteler , 0 - 5 , Weiche F.
Fr 15 Sep , Jeddeloh , 2 - 0 , Hamburger SV B
Sa 16 Sep , Hannover 96 B , 2 - 1 , Norderstedt
Sa 16 Sep , Oldenburg , 2 - 2 , Teutonia O.
Su 17 Sep , Holstein Kiel B , 2 - 1 , Spelle-Venhaus
Su 17 Sep , St. Pauli B , 2 - 3 , Meppen
Su 17 Sep , Phonix Lubeck , 2 - 0 , Kilia Kiel
Su 17 Sep , Bremer SV , 1 - 1 , Drochtersen/A.
Su 17 Sep , BW Lohne , 1 - 1 , Havelse
Tu 19 Sep , Hamburger SV B , 2 - 1 , Hannover 96 B
Fr 22 Sep , Meppen , 3 - 2 , BW Lohne
Sa 23 Sep , Hamburger SV B , 3 - 0 , Eimsbutteler
Sa 23 Sep , Weiche F. , 0 - 5 , St. Pauli B
Sa 23 Sep , Holstein Kiel B , 3 - 1 , Bremer SV
Sa 23 Sep , Drochtersen/A. , 1 - 1 , Oldenburg
Su 24 Sep , Havelse , 1 - 2 , Phonix Lubeck
Su 24 Sep , Norderstedt , 2 - 2 , Jeddeloh
Su 24 Sep , Teutonia O. , 2 - 3 , Hannover 96 B
Su 24 Sep , Spelle-Venhaus , 2 - 0 , Kilia Kiel
Sa 30 Sep , Bremer SV , 0 - 0 , Spelle-Venhaus
Sa 30 Sep , Hannover 96 B , 3 - 0 , Drochtersen/A.
Sa 30 Sep , Kilia Kiel , 0 - 2 , Havelse
Sa 30 Sep , Jeddeloh , 0 - 1 , Teutonia O.
Sa 30 Sep , Phonix Lubeck , 4 - 1 , Meppen
Sa 30 Sep , BW Lohne , 0 - 3 , Weiche F.
Sa 30 Sep , St. Pauli B , 0 - 1 , Hamburger SV B
Su 1 Oct , Eimsbutteler , 5 - 0 , Norderstedt
Su 1 Oct , Oldenburg , 0 - 2 , Holstein Kiel B
Fr 6 Oct , Holstein Kiel B , 0 - 1 , Hannover 96 B
Fr 6 Oct , Weiche F. , 0 - 5 , Phonix Lubeck
Sa 7 Oct , Hamburger SV B , 4 - 4 , BW Lohne
Sa 7 Oct , Meppen , 4 - 0 , Kilia Kiel
Su 8 Oct , Norderstedt , 3 - 2 , St. Pauli B
Su 8 Oct , Teutonia O. , 0 - 0 , Eimsbutteler
Su 8 Oct , Bremer SV , 0 - 2 , Oldenburg
Su 8 Oct , Drochtersen/A. , 2 - 2 , Jeddeloh
Su 8 Oct , Spelle-Venhaus , 1 - 3 , Havelse
Fr 13 Oct , Kilia Kiel , 2 - 3 , Weiche F.
Sa 14 Oct , BW Lohne , 2 - 1 , Norderstedt
Sa 14 Oct , Hannover 96 B , 4 - 0 , Bremer SV
Sa 14 Oct , Oldenburg , 7 - 2 , Spelle-Venhaus
Sa 14 Oct , Jeddeloh , 1 - 1 , Holstein Kiel B
Su 15 Oct , Havelse , 4 - 2 , Meppen
We 18 Oct , Jeddeloh , 0 - 0 , BW Lohne
Sa 21 Oct , Weiche F. , 1 - 2 , Havelse
Sa 21 Oct , Holstein Kiel B , 5 - 3 , Eimsbutteler
Sa 21 Oct , Spelle-Venhaus , 0 - 3 , Meppen
Sa 21 Oct , Drochtersen/A. , 2 - 0 , St. Pauli B
Su 22 Oct , Norderstedt , 0 - 2 , Phonix Lubeck
Su 22 Oct , Teutonia O. , 5 - 2 , BW Lohne
Su 22 Oct , Hamburger SV B , 4 - 2 , Kilia Kiel
Su 22 Oct , Oldenburg , 2 - 1 , Hannover 96 B
Fr 27 Oct , Meppen , 3 - 2 , Weiche F.
Fr 27 Oct , BW Lohne , 0 - 0 , Drochtersen/A.
Sa 28 Oct , Hannover 96 B , 9 - 2 , Spelle-Venhaus
Sa 28 Oct , St. Pauli B , 2 - 3 , Holstein Kiel B
Sa 28 Oct , Kilia Kiel , 1 - 3 , Norderstedt
Sa 28 Oct , Jeddeloh , 1 - 1 , Oldenburg
Su 29 Oct , Eimsbutteler , 2 - 2 , Bremer SV
Su 29 Oct , Havelse , 2 - 1 , Hamburger SV B
Sa 4 Nov , Bremer SV , 1 - 1 , St. Pauli B
Sa 4 Nov , Holstein Kiel B , 1 - 1 , BW Lohne
Sa 4 Nov , Oldenburg , 4 - 1 , Eimsbutteler
Sa 4 Nov , Jeddeloh , 2 - 6 , Hannover 96 B
Su 5 Nov , Norderstedt , 1 - 1 , Havelse
Su 5 Nov , Teutonia O. , 3 - 2 , Kilia Kiel
Su 5 Nov , Drochtersen/A. , 1 - 2 , Phonix Lubeck
Fr 10 Nov , St. Pauli B , 0 - 1 , Oldenburg
Fr 10 Nov , Kilia Kiel , 1 - 3 , Drochtersen/A.
Fr 10 Nov , Weiche F. , 1 - 2 , Hamburger SV B
Fr 10 Nov , BW Lohne , 5 - 0 , Bremer SV
Sa 11 Nov , Phonix Lubeck , 1 - 3 , Holstein Kiel B
Sa 11 Nov , Eimsbutteler , 1 - 1 , Hannover 96 B
Sa 11 Nov , Meppen , 4 - 2 , Norderstedt
Su 12 Nov , Havelse , 2 - 2 , Teutonia O.
Sa 18 Nov , Hannover 96 B , 2 - 1 , St. Pauli B
Sa 18 Nov , Bremer SV , 0 - 5 , Phonix Lubeck
Sa 18 Nov , Oldenburg , 2 - 1 , BW Lohne
Sa 18 Nov , Jeddeloh , 1 - 2 , Eimsbutteler
Sa 18 Nov , Drochtersen/A. , 2 - 0 , Havelse
Su 19 Nov , Teutonia O. , 0 - 3 , Meppen
Su 19 Nov , Kilia Kiel , 1 - 0 , Holstein Kiel B
Tu 21 Nov , Eimsbutteler , 1 - 1 , Drochtersen/A.
We 22 Nov , St. Pauli B , 1 - 1 , Teutonia O.
Fr 24 Nov , Drochtersen/A. , 3 - 3 , Meppen
Sa 25 Nov , Hannover 96 B , 4 - 1 , BW Lohne
Sa 25 Nov , Kilia Kiel , 2 - 2 , Bremer SV
Sa 25 Nov , Jeddeloh , 0 - 1 , St. Pauli B
Su 26 Nov , Holstein Kiel B , 1 - 3 , Havelse
Su 26 Nov , Oldenburg , 1 - 1 , Phonix Lubeck
Su 26 Nov , Teutonia O. , 1 - 0 , Weiche F.
Su 26 Nov , Eimsbutteler , 2 - 2 , Spelle-Venhaus
Sa 9 Dec , Hannover 96 B , 2 - 1 , Kilia Kiel
Su 10 Dec , Hamburger SV B , 1 - 0 , Spelle-Venhaus
Su 17 Dec , Teutonia O. , 3 - 1 , Norderstedt
Sa 27 Jan , Kilia Kiel , 0 - 0 , Oldenburg
Su 28 Jan , Meppen , 2 - 0 , Holstein Kiel B
Tu 30 Jan , St. Pauli B , 3 - 1 , Eimsbutteler
Fr 2 Feb , Drochtersen/A. , 0 - 0 , Hamburger SV B
Sa 3 Feb , Bremer SV , 0 - 1 , Meppen
Sa 3 Feb , St. Pauli B , 5 - 0 , Spelle-Venhaus
Su 4 Feb , Holstein Kiel B , 0 - 3 , Weiche F.
We 7 Feb , Meppen , 3 - 2 , Oldenburg
Sa 10 Feb , Kilia Kiel , 1 - 1 , Jeddeloh
Su 11 Feb , Hamburger SV B , 2 - 3 , Holstein Kiel B
Su 11 Feb , BW Lohne , 1 - 3 , St. Pauli B
Su 11 Feb , Havelse , 1 - 4 , Hannover 96 B
Su 11 Feb , Norderstedt , 0 - 1 , Drochtersen/A.
Su 11 Feb , Spelle-Venhaus , 1 - 1 , Teutonia O.
Fr 16 Feb , Drochtersen/A. , 2 - 0 , Teutonia O.
Sa 17 Feb , BW Lohne , 3 - 1 , Spelle-Venhaus
Su 18 Feb , Hannover 96 B , 2 - 1 , Meppen
Su 18 Feb , Bremer SV , 1 - 1 , Hamburger SV B
Su 18 Feb , Holstein Kiel B , 4 - 0 , Norderstedt
Su 18 Feb , Oldenburg , 2 - 0 , Weiche F.
Fr 23 Feb , Kilia Kiel , 2 - 3 , St. Pauli B
Sa 24 Feb , Teutonia O. , 0 - 1 , Holstein Kiel B
Sa 24 Feb , Hannover 96 B , 1 - 1 , Weiche F.
Sa 24 Feb , Phonix Lubeck , 3 - 1 , BW Lohne
Sa 24 Feb , Meppen , 3 - 0 , Jeddeloh
Su 25 Feb , Havelse , 1 - 0 , Eimsbutteler
Su 25 Feb , Spelle-Venhaus , 1 - 3 , Drochtersen/A.
We 28 Feb , Phonix Lubeck , 1 - 0 , Teutonia O.
We 28 Feb , BW Lohne , 1 - 2 , Jeddeloh
Sa 2 Mar , Hannover 96 B , 2 - 0 , Hamburger SV B
Sa 2 Mar , Phonix Lubeck , 1 - 0 , Spelle-Venhaus
Sa 2 Mar , Holstein Kiel B , 1 - 3 , Drochtersen/A.
Sa 2 Mar , Eimsbutteler , 0 - 0 , Meppen
Sa 2 Mar , Jeddeloh , 3 - 1 , Weiche F.
Sa 2 Mar , BW Lohne , 3 - 0 , Kilia Kiel
Su 3 Mar , Oldenburg , 5 - 0 , Norderstedt
Su 3 Mar , St. Pauli B , 1 - 1 , Havelse
Su 3 Mar , Bremer SV , 1 - 0 , Teutonia O.
We 6 Mar , Holstein Kiel B , 3 - 3 , Meppen
We 6 Mar , Norderstedt , 0 - 3 , Hamburger SV B
We 6 Mar , Spelle-Venhaus , 1 - 3 , Jeddeloh
Fr 8 Mar , Drochtersen/A. , 2 - 1 , Bremer SV
Fr 8 Mar , Weiche F. , 1 - 0 , Eimsbutteler
Sa 9 Mar , Teutonia O. , 1 - 0 , Oldenburg
Sa 9 Mar , Kilia Kiel , 2 - 2 , Phonix Lubeck
Su 10 Mar , Hamburger SV B , 4 - 1 , Jeddeloh
Su 10 Mar , Havelse , 1 - 0 , BW Lohne
Su 10 Mar , Meppen , 3 - 4 , St. Pauli B
Su 10 Mar , Norderstedt , 1 - 3 , Hannover 96 B
Su 10 Mar , Spelle-Venhaus , 0 - 3 , Holstein Kiel B
Fr 15 Mar , Eimsbutteler , 0 - 3 , Hamburger SV B
Fr 15 Mar , BW Lohne , 0 - 0 , Meppen
Sa 16 Mar , Hannover 96 B , 1 - 0 , Teutonia O.
Sa 16 Mar , Phonix Lubeck , 4 - 1 , Havelse
Sa 16 Mar , Kilia Kiel , 1 - 1 , Spelle-Venhaus
Sa 16 Mar , Bremer SV , 2 - 0 , Holstein Kiel B
Sa 16 Mar , Jeddeloh , 0 - 2 , Norderstedt
Su 17 Mar , Oldenburg , 1 - 3 , Drochtersen/A.
Su 17 Mar , St. Pauli B , 0 - 0 , Weiche F.
We 20 Mar , Norderstedt , 1 - 1 , Weiche F.
'''

Pra depois extrair os dados dos times.
