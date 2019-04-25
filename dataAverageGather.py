from pybaseball.lahman import *
import pandas as pd
import matplotlib.pylab as plt
%matplotlib inline

class yearAvg:
    average = {}

    def __init__(self, year):
        self.setAvgs(year)

    def setAvgs(self, year):
        bat = batting()
        bat = bat.dropna()
        bat = bat.loc[(bat['yearID']==year) & (bat['AB']>0)]
        bat['BA'] = bat['H']/bat['AB']
        bat['ISO'] = (bat['2B']+2*bat['3B']+3*bat['HR'])/bat['AB']
        self.average['BA'] = bat['BA'].mean()
        self.average['ISO'] = bat['ISO'].mean()
        self.average['BB'] = bat['BB'].mean()
        self.average['SO'] = bat['SO'].mean()
        self.average['SB'] = bat['SB'].mean()
        # self.data = bat[['playerID','yearID','BA','ISO','SO','BB','SB']]


    def getAvgs(self):
        return self.average
year1 = yearAvg(2016)
print(year1.getAvgs())
