# Cálculo de média de gols e portcentagem de partidas acima de 1.5 gols e 2.5 gols de diversas ligas de futebol.

<p style="text-ident: 20px">Fiz essa aplicação para pegar a média de gols de times de diversas ligas de futebol. Faço a leitura do site <b><a href="https://www.soccerstats.com/">soccerstats.com</a></b> e o algoritmo organiza os dados como no arquivo 
<b>england1.txt</b>. Outro algoritmo calcula a média de gols dos times, a quantidade de partidas que tiveram acima de 1.5 gols e abaixo de 2.5 gols. E no arquivo <b>next_games.txt</b>
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
'-', '4', 'Victoria', 'H.', 'Bstats+5+Su'] 
// Trecho da lista com os dados de jogos que a biblioteca BeautifulSoup consegue extrair do site <a>soccerstats.com</a>


Tive que organizar a lista acima num arquivo de texto como no england1.txt.

Link de onde eu extraio os dados no site: <a>https://www.soccerstats.com/results.asp?league=italy&pmtype=bydate</a><br/> 
Link da Série A italiana.











