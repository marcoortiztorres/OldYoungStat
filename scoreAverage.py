from pybaseball.lahman import *
import pandas as pd
from playerDataGather import player
from dataAverageGather import yearAvg

# if you are interesed in figuring out the average of my scores
# feel free to waste 5 hours of your life, running this function
# or take my word for it and say it is 1.4

bat = batting()
bat = bat.dropna()
players2016 = bat.loc[(bat['yearID']==2016)]
uniPlayerIDs = players2016['playerID'].tolist()

score_sum = 0
count = 0
print(len(uniPlayerIDs))
for pid in uniPlayerIDs:
    if count == 20:
        avg = score_sum / 20
        print(avg)
    print(pid)
    play = player(pid)
    play.setChapoScore(2016)
    score_sum += play.getChapoScore()
    count += 1

avg = score_sum / len(uniPlayerIDs)
print(avg)
