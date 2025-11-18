from soccerapi.api import Api888Sport
import writeOnFile
import keys

scrape888 = Api888Sport()
BetLinks888 = scrape888.competitions()
tuple888 = BetLinks888.items()

links888 = keys.organizing_keys(tuple888)

writeOnFile.write(links888, scrape888, "888Sports.txt")