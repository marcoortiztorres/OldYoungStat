from pybaseball.lahman import *
import pandas as pd
import matplotlib.pylab as plt
%matplotlib inline

class yearAvg:
    average = {}
    weights = {}

    def __init__(self, year):
        self.setAvgs(year)
        self.setWeight()

    def setAvgs(self, year):
        bat = batting()
        bat = bat.dropna()
        bat = bat.loc[(bat['yearID']==year) & (bat['AB']>0)]
        bat['BA'] = bat['H']/bat['AB']
        bat['ISO'] = (bat['2B']+2*bat['3B']+3*bat['HR'])/bat['AB']
        self.average['BA'] = bat['BA'].mean() # hits/AB - young
        self.average['ISO'] = bat['ISO'].mean() # young
        self.average['BB'] = bat['BB'].mean() # bases on balls (walks) - old
        self.average['SO'] = bat['SO'].mean() # strike outs - old
        self.average['SB'] = bat['SB'].mean() # stolen bases - young

    def setWeight(self):
        for i in self.average:
            self.weights[i] = (4.20 / self.average[i]) # I want my scores to be avergeing around 4.20

    def getAvgs(self):
        return self.average
    def getWeight(self):
        return self.weights
