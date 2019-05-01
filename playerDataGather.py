from pybaseball.lahman import *
import pandas as pd
import matplotlib.pylab as plt
from dataAverageGather import yearAvg

class player:
    playerID = ''
    playerName = ''
    palyerBirthYear = 0
    yearsPlayed = []
    ChapoScore = 0
    yearISO = 0
    data = pd.DataFrame()


    def __init__(self, playerID):
        self.playerID = playerID
        self.setData(self.playerID)
        self.setInfo(self.playerID)

    def getStatcast(self, playerID):
        return dp.DataFrame()

    def setInfo(self, playerID):
        try:
            masterData = master()
            playerData = masterData.loc[masterData['playerID']==playerID].set_index('playerID')
            self.playerName = playerData['nameFirst'][playerID] + ' ' + playerData['nameLast'][playerID]
            self.palyerBirthYear = playerData['birthYear'][playerID]
            self.yearsPlayed = self.data['yearID'].tolist()
        except:
            print("Failed to find player")

    def getName(self):
        return self.playerName

    def setData(self, playerID):
        bat = batting()
        bat = bat.loc[bat['playerID']==playerID]
        bat['BA'] = bat['H']/bat['AB']
        bat['ISO'] = (bat['2B']+2*bat['3B']+3*bat['HR'])/bat['AB']
        self.data = bat[['playerID','yearID','BA','ISO','SO','BB','SB','SF']]

    def getData(self):
        return self.data

    def setChapoScore(self, year):
        # get the year averages for the used scores
        yearAverages = yearAvg(year)
        ya = yearAverages.getAvgs()
        # get all the data for one player in a specific year
        yearData = self.data.loc[self.data['yearID'] == year].set_index('playerID')
        age = yearData['yearID'][self.playerID] - self.palyerBirthYear
        age_weight = 0.00625*(float(age)-23)**3 + 1
        old_scores = yearData['SF'][self.playerID]/ya['SF']+yearData['BB'][self.playerID]/ya['BB']
        young_scores = yearData['ISO'][self.playerID]/ya['ISO'] + yearData['SB'][self.playerID]/ya['SB']
        self.yearISO = yearData['ISO'][self.playerID]
        try:
            self.ChapoScore = (young_scores*(age_weight) + old_scores*(2-age_weight))/4
        except:
            self.ChapoScore = 0

    def getYearsPlayed(self):
        return self.yearsPlayed
    def getChapoScore(self):
        return self.ChapoScore

    def getSummary(self):
        print("="*30)
        print(self.playerName, "Score Summary")
        print("="*30)
        for year in self.yearsPlayed:
            age = year - self.palyerBirthYear
            self.setChapoScore(year)
            print("age: ",age, "|",year,"score: ",self.getChapoScore(), "| ISO:",self.yearISO)
