from pybaseball.lahman import *
import pandas as pd
import matplotlib.pylab as plt
%matplotlib inline

class player:
    playerID = ''
    playerName = ''
    palyerBirthYear = 0
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

    def getName(self):
        return self.playerName

    def getAge(self, year):
        return year - self.palyerAge

    def setData(self, playerID):
        bat = batting()
        bat = bat.loc[bat['playerID']==playerID]
        bat['BA'] = bat['H']/bat['AB']
        bat['ISO'] = (bat['2B']+2*bat['3B']+3*bat['HR'])/bat['AB']
        self.data = bat[['playerID','yearID','BA','ISO','SO','BB','SB']]

    def getData(self):
        return self.data

    def setChapoScore(self, year):
        yearData = self.data.loc[self.data['yearID'] == year].set_index('playerID')
        print(yearData)
        ageWeight = (yearData['yearID'][self.playerID] - self.palyerBirthYear-24) / 12
        self.ChapoScore = ((yearData['BA'][self.playerID]*14yearData['BA'][self.playerID]*14)*(1-ageWeight) + (yearData['ISO'][self.playerID]*yearData['SO'][self.playerID]*.5)*(ageWeight))/4

    def getChapoScore(self):
        return self.ChapoScore



OldP = player('beckhgo01')
OldP.getData()
OldP.setChapoScore(2015)
OldP.getChapoScore()
