from bs4 import BeautifulSoup
import requests

urls = []
leagues = []
files_total = []
matches_next = []


headers = {
    "Accept-Encoding": "identity"
}

'''
urls.append('https://www.soccerstats.com/results.asp?league=england2&pmtype=bydate')
files_total.append('england2.txt')
urls.append('https://www.soccerstats.com/results.asp?league=italy&pmtype=bydate')
files_total.append('italy1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=italy2&pmtype=bydate')
files_total.append('italy2.txt')
urls.append('https://www.soccerstats.com/results.asp?league=germany&pmtype=bydate')
files_total.append('germany1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=germany2&pmtype=bydate')
files_total.append('germany2.txt')
urls.append('https://www.soccerstats.com/results.asp?league=germany10&pmtype=bydate')
files_total.append('germany3.txt')
urls.append('https://www.soccerstats.com/results.asp?league=spain&pmtype=bydate')
files_total.append('spain1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=spain2&pmtype=bydate')
files_total.append('spain2.txt')
urls.append('https://www.soccerstats.com/results.asp?league=england&pmtype=bydate')
files_total.append('england1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=england3&pmtype=bydate')
files_total.append('england3.txt')
urls.append('https://www.soccerstats.com/results.asp?league=england19&pmtype=bydate')
files_total.append('england19.txt')
urls.append('https://www.soccerstats.com/results.asp?league=england7&pmtype=bydate')
files_total.append('england7.txt')
urls.append('https://www.soccerstats.com/results.asp?league=portugal&pmtype=bydate')
files_total.append('portugal1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=argentina&pmtype=bydate')
files_total.append('argentina1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=armenia&pmtype=bydate')
files_total.append('armenia1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=australia&pmtype=bydate')
files_total.append('australia1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=austria&pmtype=bydate')
files_total.append('austria1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=bahrain&pmtype=bydate')
files_total.append('bahrain1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=belgium&pmtype=bydate')
files_total.append('belgium1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=bosnia&pmtype=bydate')
files_total.append('bosnia1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=brazil&pmtype=bydate')
files_total.append('brazil1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=brazil2&pmtype=bydate')
files_total.append('brazil2.txt')
urls.append('https://www.soccerstats.com/results.asp?league=bulgaria&pmtype=bydate')
files_total.append('bulgaria1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=croatia&pmtype=bydate')
files_total.append('croatia1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=ecuador&pmtype=bydate')
files_total.append('ecuador1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=estonia2&pmtype=bydate')
files_total.append('estonia2.txt')
urls.append('https://www.soccerstats.com/results.asp?league=france&pmtype=bydate')
files_total.append('france1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=france2&pmtype=bydate')
files_total.append('france2.txt')
urls.append('https://www.soccerstats.com/results.asp?league=france3&pmtype=bydate')
files_total.append('france3.txt')
urls.append('https://www.soccerstats.com/results.asp?league=mongolia&pmtype=bydate')
files_total.append('mongolia1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=romania&pmtype=bydate')
files_total.append('romania1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=serbia&pmtype=bydate')
files_total.append('serbia1.txt')


urls.append('https://www.soccerstats.com/results.asp?league=sweden2&pmtype=bydate')
files_total.append('sweden2.txt')
urls.append('https://www.soccerstats.com/results.asp?league=poland&pmtype=bydate')
files_total.append('poland1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=peru&pmtype=bydate')
files_total.append('peru1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=paraguay&pmtype=bydate')
files_total.append('paraguay1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=norway2&pmtype=bydate')
files_total.append('norway2.txt')
urls.append('https://www.soccerstats.com/results.asp?league=norway&pmtype=bydate')
files_total.append('norway1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=netherlands2&pmtype=bydate')
files_total.append('eerste.txt')
urls.append('https://www.soccerstats.com/results.asp?league=netherlands&pmtype=bydate')
files_total.append('eredivise.txt')
urls.append('https://www.soccerstats.com/results.asp?league=mexico2&pmtype=bydate')
files_total.append('mexico2.txt')
urls.append('https://www.soccerstats.com/results.asp?league=mexico&pmtype=bydate')
files_total.append('mexico1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=ireland&pmtype=bydate')
files_total.append('ireland1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=hungary&pmtype=bydate')
files_total.append('hungary1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=portugal2&pmtype=bydate')
files_total.append('portugal2.txt')
urls.append('https://www.soccerstats.com/results.asp?league=belgium2&pmtype=bydate')
files_total.append('belgium2.txt')
urls.append('https://www.soccerstats.com/results.asp?league=brazil3&pmtype=bydate')
files_total.append('brazil3.txt')
urls.append('https://www.soccerstats.com/results.asp?league=chile&pmtype=bydate')
files_total.append('chile1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=china&pmtype=bydate')
files_total.append('china1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=colombia2&pmtype=bydate')
files_total.append('colombia2.txt')
urls.append('https://www.soccerstats.com/results.asp?league=colombia&pmtype=bydate')
files_total.append('colombia1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=denmark2&pmtype=bydate')
files_total.append('denmark2.txt')
urls.append('https://www.soccerstats.com/results.asp?league=denmark&pmtype=bydate')
files_total.append('denmark1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=finland&pmtype=bydate')
files_total.append('finland1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=greece&pmtype=bydate')
files_total.append('greece1.txt')
urls.append('https://www.soccerstats.com/results.asp?league=germany4&pmtype=bydate')
files_total.append('germany5.txt')
urls.append('https://www.soccerstats.com/results.asp?league=germany3&pmtype=bydate')
files_total.append('germany4.txt')
'''

urls.append('https://www.soccerstats.com/results.asp?league=italy&pmtype=bydate')
files_total.append('italy1.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=italy2&pmtype=bydate')
files_total.append('italy2.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy2')

urls.append('https://www.soccerstats.com/results.asp?league=germany&pmtype=bydate')
files_total.append('germany1.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=germany')

urls.append('https://www.soccerstats.com/results.asp?league=austria&pmtype=bydate')
files_total.append('austria1.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=austria')

urls.append('https://www.soccerstats.com/results.asp?league=germany2&pmtype=bydate')
files_total.append('germany2.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=germany2')

urls.append('https://www.soccerstats.com/results.asp?league=germany3&pmtype=bydate')
files_total.append('germany4.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=germany4&pmtype=bydate')
files_total.append('germany5.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=spain&pmtype=bydate')
files_total.append('spain1.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')
'''
urls.append('https://www.soccerstats.com/results.asp?league=spain2&pmtype=bydate')
files_total.append('spain2.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')
'''
urls.append('https://www.soccerstats.com/results.asp?league=england&pmtype=bydate')
files_total.append('england1.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=england2&pmtype=bydate')
files_total.append('england2.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=england3&pmtype=bydate')
files_total.append('england3.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=portugal&pmtype=bydate')
files_total.append('portugal1.txt')

urls.append('https://www.soccerstats.com/results.asp?league=portugal2&pmtype=bydate')
files_total.append('portugal2.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=argentina&pmtype=bydate')
files_total.append('argentina1.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=belgium&pmtype=bydate')
files_total.append('belgium1.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=belgium2&pmtype=bydate')
files_total.append('belgium2.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=brazil&pmtype=bydate')
files_total.append('brazil1.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=brazil2&pmtype=bydate')
files_total.append('brazil2.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=brazil3&pmtype=bydate')
files_total.append('brazil3.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=chile&pmtype=bydate')
files_total.append('chile1.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=china&pmtype=bydate')
files_total.append('china1.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=greece&pmtype=bydate')
files_total.append('greece1.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=colombia&pmtype=bydate')
files_total.append('colombia1.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=croatia&pmtype=bydate')
files_total.append('croatia1.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=denmark&pmtype=bydate')
files_total.append('denmark1.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=denmark2&pmtype=bydate')
files_total.append('denmark2.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=ecuador&pmtype=bydate')
files_total.append('ecuador1.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=france&pmtype=bydate')
files_total.append('france1.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=france2&pmtype=bydate')
files_total.append('france2.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=hungary&pmtype=bydate')
files_total.append('hungary1.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=ireland&pmtype=bydate')
files_total.append('ireland1.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')
'''
urls.append('https://www.soccerstats.com/results.asp?league=mexico&pmtype=bydate')
files_total.append('mexico1.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')
'''
urls.append('https://www.soccerstats.com/results.asp?league=mexico2&pmtype=bydate')
files_total.append('mexico2.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=netherlands&pmtype=bydate')
files_total.append('eredivise.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=netherlands2&pmtype=bydate')
files_total.append('eerste.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=norway&pmtype=bydate')
files_total.append('norway1.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=norway2&pmtype=bydate')
files_total.append('norway2.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=paraguay&pmtype=bydate')
files_total.append('paraguay1.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=peru&pmtype=bydate')
files_total.append('peru1.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=poland&pmtype=bydate')
files_total.append('poland1.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=romania&pmtype=bydate')
files_total.append('romania1.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=sweden2&pmtype=bydate')
files_total.append('sweden2.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=finland&pmtype=bydate')
files_total.append('finland1.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=finland2&pmtype=bydate')
files_total.append('finland2.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=estonia&pmtype=bydate')
files_total.append('estonia1.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=southkorea&pmtype=bydate')
files_total.append('south_korea1.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=brazil4&pmtype=bydate')
files_total.append('brazil4.txt')
matches_next.append('https://www.soccerstats.com/results.asp?league=italy')

urls.append('https://www.soccerstats.com/results.asp?league=japan&pmtype=bydate')
files_total.append('japan1.txt')

urls.append('https://www.soccerstats.com/results.asp?league=japan2&pmtype=bydate')
files_total.append('japan2.txt')

urls.append('https://www.soccerstats.com/results.asp?league=japan3&pmtype=bydate')
files_total.append('japan3.txt')

urls.append('https://www.soccerstats.com/results.asp?league=iceland&pmtype=bydate')
files_total.append('iceland1.txt')

'''
urls.append('https://www.soccerstats.com/results.asp?league=iceland2&pmtype=bydate')
files_total.append('iceland2.txt')


urls.append('https://www.soccerstats.com/results.asp?league=iceland3&pmtype=bydate')
files_total.append('iceland3.txt')

urls.append('https://www.soccerstats.com/results.asp?league=iceland4&pmtype=bydate')
files_total.append('iceland4.txt')
'''

urls.append('https://www.soccerstats.com/results.asp?league=lithuania&pmtype=bydate')
files_total.append('lithuania1.txt')

urls.append('https://www.soccerstats.com/results.asp?league=southkorea2&pmtype=bydate')
files_total.append('south_korea2.txt')

urls.append('https://www.soccerstats.com/results.asp?league=southkorea3&pmtype=bydate')
files_total.append('south_korea3.txt')

urls.append('https://www.soccerstats.com/results.asp?league=malaysia&pmtype=bydate')
files_total.append('malasya1.txt')
'''
urls.append('https://www.soccerstats.com/results.asp?league=myanmar&pmtype=bydate')
files_total.append('myanmar1.txt')
'''
urls.append('https://www.soccerstats.com/results.asp?league=usa&pmtype=bydate')
files_total.append('USA_1.txt')

urls.append('https://www.soccerstats.com/results.asp?league=usa2&pmtype=bydate')
files_total.append('USA_2.txt')

urls.append('https://www.soccerstats.com/results.asp?league=usa3&pmtype=bydate')
files_total.append('USA_3.txt')

urls.append('https://www.soccerstats.com/results.asp?league=venezuela&pmtype=bydate')
files_total.append('venezuela1.txt')

urls.append('https://www.soccerstats.com/results.asp?league=chile2&pmtype=bydate')
files_total.append('chile2.txt')





cont = 1

for item in urls:
    print(cont)
    ind = urls.index(item)
    print(files_total[ind])
    cont += 1
    req = requests.get(item, timeout=10, headers=headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    league = soup.find ('table' , id= 'btable').text
    league = league.split()
    leagues.append(league)
    


