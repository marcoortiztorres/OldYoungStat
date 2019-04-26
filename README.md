# OldYoungStat
Give me a baseball player and I will tell you how good they really are!

Using a lahman dataset, I have calculated my own statistic which aims to set a universal scoreing system for players regardless of age. As we know, a players preformance varies by age with the peak at age 26. In order to account for this preformance change, I have weighted the players age in my calculation in order to have a consistance player score across their career. 

The statistics that I consider in this calculation are sacraficed flies & walk as older player skill and stolen bases & ISO as younger player skills. These scores are all averaged out by the average of the season. Finally the young scores are weighted lower if they are younger with the older scores being weighted higher and the vice versa if they are older. 

The code was meant to run on a jupyter notebook, but it stopped working on my computer. So instead you can run it from your terminal by running:

```
python main.py
```

You will be prompted to enter in a playerID and if you don't know any by heart, don't worry I have a couple here that you can use

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
