from pybaseball.lahman import *
import pandas as pd
import matplotlib.pylab as plt
%matplotlib inline

class player:
    playerID = ''
    playerName = ''
    palyerBirthYear = 0
    data = pd.DataFrame()


    def __init__(self, playerID):
        self.playerID = playerID
        self.playerName = self.getName()
        self.setLahman(self.playerID)
        self.setInfo(self.playerID)

    def getStatcast(self, playerID):
        return dp.DataFrame()

    def setInfo(self, playerID):
        masterData = master()
        playerData = masterData.loc[masterData['playerID']==playerID].set_index('playerID')
        self.playerName = playerData['nameFirst'][playerID] + ' ' + playerData['nameLast'][playerID]
        self.palyerAge = playerData['birthYear'][playerID]

    def getName(self):
        return self.playerName

    def getAge(self, year):
        return year - self.palyerAge

    def setLahman(self, playerID):
        bat = batting()
        self.data = bat.loc[bat['playerID']==playerID]

    def getLahman(self):
        return self.data

OldP = player('freemfr01')
