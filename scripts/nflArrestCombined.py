
import pandas as pd 
import numpy as np
from collections import Counter
# print(pd.read_csv('players.csv'))
#arrestdata json file
dfa = pd.read_json('../data/arrestData.json')
#player list from nflsavant
dfp = pd.read_csv('../data/players.csv')
#validating years with profootball reference data
dfv = pd.read_csv('../data/players_search_list.csv')



dfo = pd.merge(dfv, dfp, how='left', on='name')     #Combining validated names by year with basic stats from 2000 - 2013

dfo = dfo.drop_duplicates(subset='name', keep=False)    #Gets rid of duplicates 


#Fixing columns to take lists
dfo['arrestSeason']=dfo['arrestSeason'].astype(object)
dfo['arrestSeasonState']=dfo['arrestSeasonState'].astype(object)
dfo['arrestTeams']=dfo['arrestTeams'].astype(object)
dfo['crimeCategory']=dfo['crimeCategory'].astype(object)
dfo['resolutionCategory']=dfo['resolutionCategory'].astype(object)
dfo['legalLevel']=dfo['legalLevel'].astype(object)
dfo['encounter']=dfo['encounter'].astype(object)
dfo['daysToLastPersonalArrest']=dfo['daysToLastPersonalArrest'].astype(object)
dfo['daysToLastNFLArrest']=dfo['daysToLastNFLArrest'].astype(object)
dfo['daysToLastCrimeArrest']=dfo['daysToLastCrimeArrest'].astype(object)
dfo['daysToLastTeamArrest']=dfo['daysToLastTeamArrest'].astype(object)
dfo['description']=dfo['description'].astype(object)
dfo['outcome']=dfo['outcome'].astype(object)



for i, j in dfo.iterrows():         #go through each name in the newly created DFO ouput data frame
     curName = j['name']
     duh = dfa.loc[dfa['Name'] == curName]          #search through Arrest data and if there is a match 
     dfo.set_value(i,'num_arrests',len(duh.index))
     arrestSeason = []
     arrestSeasonState = []
     arrestTeams = []
     crimeCategory = []
     resolutionCategory = []
     legalLevel = []
     encounter = []
     daysToLastPersonalArrest = []
     daysToLastNFLArrest = []
     daysToLastCrimeArrest = []
     daysToLastTeamArrest = []
     description = []
     outcome = []
     if(len(duh.index) > 0):            #if there is an arrest for the person save the data 
         for k, l in duh.iterrows(): 
            arrestSeason.append(l['Season'])
            arrestSeasonState.append(l['ArrestSeasonState'])
            arrestTeams.append(l['Team'])
            crimeCategory.append(l['Crime_category'])
            resolutionCategory.append(l['resolution_category_id'])
            legalLevel.append(l['legal_level_id'])
            encounter.append(l['Encounter'])
            daysToLastPersonalArrest.append(l['DaysSince'])
            daysToLastNFLArrest.append(l['DaysToLastArrest'])
            daysToLastCrimeArrest.append(l['DaysToLastCrimeArrest'])
            daysToLastTeamArrest.append(l['DaysToLastTeamArrest'])
            description.append(l['Description'])
            outcome.append(l['Outcome'])
         dfo.set_value(i,'arrestSeason', arrestSeason)                  #actually set data in data frame
         dfo.set_value(i,'arrestSeasonState', arrestSeasonState)
         dfo.set_value(i, 'arrestTeams', arrestTeams)
         dfo.set_value(i,'crimeCategory',crimeCategory)
         dfo.set_value(i,'resolutionCategory',resolutionCategory)
         dfo.set_value(i,'legalLevel',legalLevel)
         dfo.set_value(i,'encounter',encounter)
         dfo.set_value(i,'daysToLastPersonalArrest',daysToLastPersonalArrest)
         dfo.set_value(i,'daysToLastNFLArrest',daysToLastNFLArrest)
         dfo.set_value(i,'daysToLastCrimeArrest',daysToLastCrimeArrest)
         dfo.set_value(i,'daysToLastTeamArrest',daysToLastTeamArrest)
         dfo.set_value(i,'description',description)
         dfo.set_value(i,'outcome',outcome)


#colname = ['Unnamed: 15', 'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22']
#for colname in columnList: # there are columns with title s in the above list that do not belong
    #del arrestDf[colname] 

dfo.describe()

arrestDf = dfo.loc[dfo['num_arrests'] > 0]  #returns only the people who have been arrested around 438 people w/ 579 arrests

### all team arrests per team 
countTeams = Counter()
for d in arrestDf['arrestTeams'].apply(lambda x: Counter(x)): 
     countTeams += d
print(countTeams)

### all arrests by category 
countCrimeCat = Counter()
for d in arrestDf['crimeCategory'].apply(lambda x: Counter(x)): 
     countCrimeCat += d
print(countCrimeCat)

### all arrests per season 
countSeason = Counter()
for d in arrestDf['arrestSeason'].apply(lambda x: Counter(x)): 
     countSeason += d
print(countSeason)

### all arrests in our out of season
countSeasonState = Counter()
for d in arrestDf['arrestSeasonState'].apply(lambda x: Counter(x)): 
     countSeasonState += d
print(countSeasonState)


dfpa = pd.merge(dfo, dfa, how='right', left_on=['name'], right_on=['Name'])     #data from every arrest with player in many times
dfpa.drop(dfpa.columns[[2,3,4,5,6,7,8,9,10,11,12,13,14,29,30,31,32,33,34,35,36]], axis = 1, inplace=True) # get rid of garbage columns 
dfpa = dfpa[dfpa.name.notnull()] # there are some players that are not in out data list but they have arrests durring out period



for y in range(2000,2013):                          # this code goes by year to and in the num_arrests column has totals of arrests per team
     yearDf = dfpa.loc[dfpa['Year'] == y] 
     #arrestsByYearByteam[y] = 
     yearDfCounts = yearDf.groupby('Team_name').count()
     break
     #.apply(pd.value_counts)
#print(arrestsByYearByteam)


dfpaSorted = dfpa.sort_values('Year')
dfpaSorted.to_csv('../output/outputDfpa.csv', sep=',') 
yearDfCounts.to_csv('../output/outputYearDfCounts.csv', sep=',')         #save data in data frame

 