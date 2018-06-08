# MAIN

import datetime
import HandlerRequest

######## DATABASE #######
countryPlay = {'Deutschland': '21.12.2018', 'Spanien': '01.06.2019', 'Sizilien': '01.01.2018'}
#########################

def getDate():
    nowDate = datetime.datetime.now()
    return [nowDate.year, nowDate.month, nowDate.day, nowDate.hour, nowDate.minute, nowDate.second]

def findCountry(search, countries):
    return countries[search]

# Get Country from Request-File
handler = HandlerRequest.HandlerRequest()
handler.LoadRequest('Request.json')
var_country = handler.GetCountry()

# Get & Print Play Date from Database
playDate = findCountry(var_country, countryPlay)
print("Game is on " + str(playDate))
