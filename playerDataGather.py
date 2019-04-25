from pybaseball.lahman import *
import pandas as pd
import matplotlib.pylab as plt
from dataAverageGather.py import yearAvg
%matplotlib inline

class player:
    playerID = ''
    playerName = ''
    palyerBirthYear = 0
    yearsPlayed = []
    ChapoScore = 0
    data = pd.DataFrame()


    def __init__(self, playerID):
        self.playerID = playerID
        self.playerName = self.getName()
        self.setData(self.playerID)
        self.setInfo(self.playerID)

    def getStatcast(self, playerID):
        return dp.DataFrame()

    def setInfo(self, playerID):
        masterData = master()
        playerData = masterData.loc[masterData['playerID']==playerID].set_index('playerID')
        self.playerName = playerData['nameFirst'][playerID] + ' ' + playerData['nameLast'][playerID]
        self.palyerBirthYear = playerData['birthYear'][playerID]
        self.yearsPlayed = self.data['yearID'].tolist()

    def getName(self):
        return self.playerName

    def setData(self, playerID):
        bat = batting()
        bat = bat.loc[bat['playerID']==playerID]
        bat['BA'] = bat['H']/bat['AB']
        bat['ISO'] = (bat['2B']+2*bat['3B']+3*bat['HR'])/bat['AB']
        self.data = bat[['playerID','yearID','BA','ISO','SO','BB','SB']]

    def getData(self):
        return self.data

    def setChapoScore(self, year):
        yearWeights = yearAvg(year)
        yearData = self.data.loc[self.data['yearID'] == year].set_index('playerID')
        yw = yearWeights.getWeight()
        age = yearData['yearID'][self.playerID] - self.palyerBirthYear
        old_scores = yearData['SO'][self.playerID]*yw['SO']+yearData['BB'][self.playerID]*yw['BB']
        young_scores = yearData['ISO'][self.playerID]*yw['ISO'] + yearData['BA'][self.playerID]*yw['BA'] + yearData['SB'][self.playerID]*yw['SB']
        if age <= 27:
            self.ChapoScore = (young_scores*(0.6) + old_scores*1.4)/5
        else:
            self.ChapoScore = (young_scores*(1.4) + old_scores*0.6)/5

    def getYearsPlayed(self):
        return self.yearsPlayed
    def getChapoScore(self):
        return self.ChapoScore

    def getSummary(self):
        print(self.playerName, "Score Summary")
        print("="*30)
        for year in self.yearsPlayed:
            age = year - self.palyerBirthYear
            self.setChapoScore(year)
            print("age: ",age, "|",year,"score: ",self.getChapoScore())


OldP = player('harpebr03')
print(OldP.getYearsPlayed())
OldP.getSummary()
