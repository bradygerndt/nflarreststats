import requests
import json

teams = ['min','den','cin','ten','jac','tb','ind','cle','kc','chi','mia','sea','bal','lac','no','sf','pit','gb','car','oak','ari','was','nyj','atl','ne','buf','dal','la','nyg','det','phi','hou']



def dataRequest(team, inFile):
    print('Getting data for ' + team + '\n')
    r = requests.get('http://nflarrest.com/api/v1/team/arrests/' + team) # optional to include years + '&end_date=2013-12-31')
    if r.status_code == requests.codes.ok:
        print(team + ' request responded with 200')
        json.dump(r.json(), inFile)


with open('arrestData.json', 'a') as file:
    [dataRequest(team, file) for team in teams]