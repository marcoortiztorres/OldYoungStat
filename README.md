# Old Young Stat

### Intro ###

While taking this class there was always one reoccurring thing that would affect all other statistics. As players mature in the game, they reach a point of peak performance and deteriorate from then on. The statistic I chose to create takes into account this point of peak performance and determines the players overall statistic by removing the performance buff/de-buff of their age. After working on this assignment, I realised that this does not mean that the score I am calculating should be constant over time. While looking through different players, I learned that the difference in the players score comes from more than just age. Although age has a large impact on the players performance, it is not the only important factor in a player’s performance.

### What is the statistic? ###

\begin{equation} age_weight = 0.00625(age-26)^3+1  \end{equation}

The Chapo statistic is a combinate of 4 statistics, half of which I have defined to be young player statistics and the other half old player statistics. The young player statistics are those which value speed and power, where the old player statistics value more sacrifices and hits. The players score is then divided by the average to get a normalised score for each statistic. The weight was made to be a cubic formula so that as the player gets closer to the performance peak their scores level off. Otherwise as they get older the weight gets larger so younger player scores are weighed higher, and older player scores are weighed lower. 

### Similar Statistics ###

All the time we see great player age curves that show a player’s performance change using the basic statistics. However, why do we never see a statistic that accounts for this age curve. When searching for statistics that considered the players age, I was unable to find any. Even when trying to find statistics that were age dependent, I failed to find anyone who was willing to compare the statistics. Maybe it’s because this was a terrible idea or maybe it is because they assume that a player’s performance will average out at some point, so there is no need to worry about their age. This statistic doesn’t simply average out the players performance over the years. Instead it aims to remove any age bias and see how much luck/skill that player had that season and to figure out the trend of their performance beyond age.

### Effectiveness ###

I genuinely believe that this statistic would do a much better job of determining players’ performance than the available stats. This information not be as useful for someone trying to purchase a player, but it does help for someone trying to determine how good a player was for hall of fame. Sure you can have high performance young players in your hall of fame, or you can have player who have had circumstances like age removed from their ratings. The Chapo score makes it possible for seemingly average players to shine, and show the efforts of their training regardless of all the circumstances against them like age.

###  How to run ###

```
python main.py
```

you will be prompted to enter in a playerID and if you don't know any by heart, don't worry I have a couple here that you can use

**Good Players:**

- arenano01
- harpebr03

**Bad Players**

- zimmejo02
- gennesc01

### Sample Output ###

```
Enter a players playerID: arenano01

==============================
Nolan Arenado Score Summary
==============================
age:  22.0 | 2013 score:  1.1853149459578618 | ISO: 0.13786008230452676
age:  23.0 | 2014 score:  1.9973716915770532 | ISO: 0.21296296296296297
age:  24.0 | 2015 score:  1.8051055022382663 | ISO: 0.28733766233766234
age:  25.0 | 2016 score:  1.723476597268371 | ISO: 0.2750809061488673
```
