<p style="text-ident: 20">Fiz essa aplicação para pegar a média de gols de times de diversas ligas de futebol, faço a leitura do site **soccerstats.com** e o algoritmo organiza os dados como no arquivo 
**england1.txt**. Outro algoritmo calcula a média de gols dos times, a porcentagem de partidas que tiveram acima de 1.5 gols e abaixo de 2.5 gols. E no arquivo **next_games.txt**
mostra as partidas que vão ter com as medias dos times que vão se enfrentar. </p>

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
'1', '-', '2', 'Buchholzstats+3+Fr', '2', 'SepW.', 'Concordia', '1', '-', '1', 'Victoria', 'H.', 'Bstats-2+Fr']


Tive que organizar a lista acima num arquivo de texto como no england1.txt.











