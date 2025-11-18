
from soccerapi.api import ApiUnibet
import writeOnFile
import keys

scrapeUni = ApiUnibet()
UniBetLinks = scrapeUni.competitions()
tupleUni = UniBetLinks.items()

uniLinks = keys.organizing_keys(tupleUni)

writeOnFile.write(uniLinks, scrapeUni, "Unibet.txt")









#for item in chaves:
#    print(f"{item}\n")

#writeFile(UniBetLinks)




