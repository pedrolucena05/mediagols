from bs4 import BeautifulSoup
import requests
import os
import datetime




'''
matches = ['2.5+TGBTSFr', '29', 'JulUnion', 'Tornesch', '2', '-', '2', 'Altona+4+Su', '31', 'JulPaloma', '2', '-', '1', 'Rugenbergen+3+Su', '31', 'JulT.', 'Wilhelmsburg', 
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
'12:00', 'W.', 'Concordiah2hSu', '7', 'MaySasel', '13:00', 'RugenbergenSu', '7', 'MayUnion', 'Tornesch', '13:00', 'Dassendorfh2h']
'''

str2 = 'parei em nenhum flag'
str3 = 'str3 vazia'


def scrapeSoup (matches, textFile, i, league_name):
    #try:
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
                                #print('Ola')
                                next_matches_home.append(home_team[-1])
                                next_matches_date.append(day_match[-1])
                                home_team.pop()
                                day_match.pop()
                                
                                str3 = 'to na condicao de parada correta'
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
                            if len(matches[index]) > 2 and matches[index][-2].isupper() == True and matches[index][-1].islower() == True:
                                if index != len(matches) - 1:
                                    away2 += matches[index][:-2]
                                    
                                    next_matches_away.append(away2)
                                    day2 += matches[index][-2:] + ' '
                                    
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
                                away2 += matches[index] + ' '
                else:
                    '''
                    if flag2 == 1:
                        if len(matches[index]) > 1:  
                            if matches[index][-2].isupper() and matches[index][-1].islower() and matches[index + 1].isdigit():
                                day += matches[index][-2]
                                day += matches[index][-1] + ' '
                                flag = 1    
                                flag2 = 0
                    '''
                    
                    
                    #print(matches[index])
                    #print(day_match)
                    #print(home_team)
                    #print(result)
                    #print("\n\n\n")
                    
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
                                
                                away_team.append(away)
                                away = ''
                    
                                day += matches[index][-2:] + ' '
                            else:
                                tamanhoo = len(matches[index]) - 5
                                away += matches[index][:tamanhoo]
                                away_team.append(away)
                                away = ''

                                day += matches[index][-2:] + ' '

                            flag = 1
                        
                    else:
                        away += matches[index] + ' '
                        flag = 5
                        

                        
                    
                    

        
                def jumpTo(index):
                    cont = index
                    while len(matches[cont]) > 3 and matches[cont][:3] in months and (matches[cont][3].isupper() == True or matches[cont][3].isdigit() == True):
                        cont += 1
                
                    return cont - 1
                
    #except:
    #    print(matches)
    #    print("\n\n")
    #    print(cont)        
            
        #try:
        
        #print (len(day_match))
        #print (len(home_team))
        #print (len(result))
        #print (len(away_team))
        #print (day_match)
        #print (home_team)
        #print (result)
        #print (away_team)
        #print (str8)
        #print (next_matches_home)
        #print (next_matches_away)
        #print (next_matches_date)
        #print (len(next_matches_home))
        #print (len(next_matches_away))
        #print (len(next_matches_date))
        
        with open(textFile, "w") as arq:
            for index in range(len(away_team)):
                if len(home_team) > index:
                    arq.write(f"{day_match[index]} , {home_team[index]} , {result[index]} , {away_team[index]}\n")
                    print('To aqyu')
                else:
                    if len(result) > index:
                        arq.write(f"{day_match[index]} , NULL , {result[index]} , {away_team[index]}\n")
                        print('To aqyu 2')
            
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
        
        return return_list

        #except:
        #    print ("deu erro")
        #    print (matches[indexador])
        #    print (next_matches_home)
        #    print(textFile)


'''
            elif len(matches[index]) <= 2:
                if len(matches[index]) == 2:
                    day += matches[index][0]
                    day += matches[index][1]
                    day += ' '
                else:
                    day += matches[index][0]
                    day += ' '
                flag = 2
            '''

'''
if matches[index][3].isupper() == True:
                                    if (len(home2) > 3) and (home2[2] == ' ' or home2[3] == ' '): 
                                        home2 += matches[index][2:]
                                    else:
                                        home2 += matches[index][3:]
                                    if (len(home2) > 3) and home2[2] == ' ':
                                        home2 = home2[3:]    
                                        next_matches_home.append(home2)
                                        home2 = ''
                                    elif home2[1] == ' ':
                                        aux5 = home2.split()
                                        for item in aux5:
                                            if aux5.index(item) != 0:
                                                home3 += item   
                                        next_matches_home.append(home3)
                                        home2 = ''
                                        home3 = ''
                                else:
                                    home2 += matches[index]
                                    home2 = home2[3:]
                                    next_matches_home.append(home2)
                                    home2 = ''
    '''

'''
                                    if (len(matches[cont2]) > 3) and matches[cont2][3].isupper() == True:
                                        home2 += matches[cont2][3:]
                                        next_matches_home.append(home2)
                                        home2 = ""
                                        break
                                    else:
                                        home2 += matches[cont2]
                                        cont2 -= 1
                                    
                                    '''
