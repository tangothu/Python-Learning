# # # # -*- coding: utf-8 -*-
'''
@author: Kevin

https://www.kaggle.com/c/titanic

The sinking of the RMS Titanic is one of the most infamous shipwrecks in history.  On April 15, 1912, during her maiden voyage, the Titanic sank after colliding with an iceberg, killing 1502 out of 2224 passengers and crew. This sensational tragedy shocked the international community and led to better safety regulations for ships.
One of the reasons that the shipwreck led to such loss of life was that there were not enough lifeboats for the passengers and crew. Although there was some element of luck involved in surviving the sinking, some groups of people were more likely to survive than others, such as women, children, and the upper-class.
In this challenge, we ask you to complete the analysis of what sorts of people were likely to survive. In particular, we ask you to apply the tools of machine learning to predict which passengers survived the tragedy.

VARIABLE DESCRIPTIONS:
survival        Survival
                (0 = No; 1 = Yes)
pclass          Passenger Class
                (1 = 1st; 2 = 2nd; 3 = 3rd)
name            Name
sex             Sex
age             Age
sibsp           Number of Siblings/Spouses Aboard
parch           Number of Parents/Children Aboard
ticket          Ticket Number
fare            Passenger Fare
cabin           Cabin
embarked        Port of Embarkation
                (C = Cherbourg; Q = Queenstown; S = Southampton)

SPECIAL NOTES:
Pclass is a proxy for socio-economic status (SES)
 1st ~ Upper; 2nd ~ Middle; 3rd ~ Lower

Age is in Years; Fractional if Age less than One (1)
 If the Age is Estimated, it is in the form xx.5

'''

import pandas as pd
from pandas import Series, DataFrame
import csv

class TrainInfoProcessor(object):

    def __init__(self):
        self.data=DataFrame(columns=('PassengerId','Survived','Pclass','Name','Sex','Age','SibSp',\
                                'Parch','Ticket','Fare','Cabin','Embarked'))
        self.loadData()

    def getSurvivalInfo(self):
        df=self.data

        print df[df['Age']>60][['Sex','Pclass','Age','Survived']]

        print(self.data[:5])
        # print self.data.loc[1]
        #print self.data.loc[:10,['Name','Survived']]
        #print self.data.iloc[:5]
        men=self.data[self.data['Sex']=='male']
        women=self.data[self.data['Sex']=='female']

        # One way of getting survival rate
        survivalwomen=float(sum(women.Survived=='1'))/len(women)
        survivalmen=float(sum(men.Survived=='1'))/len(men)

        # Data massage as the data loaded from csv needs to be transformed to numeric
        self.data.Survived=pd.to_numeric(self.data.Survived,errors='ignore')
        self.data.Age=pd.to_numeric(self.data.Age,errors='ignore')
        groupsBySex = self.data.groupby('Sex') #divide group by column Sex
        print "Survived rate by Sex..."
        print groupsBySex['Survived'].mean()
        print "Average age by Sex..."
        print groupsBySex['Age'].mean()

        # Get the survived groups
        survivedGroup = self.data[self.data['Survived']==1]
        survivedGroupsBySex = survivedGroup.groupby('Sex')
        print "Average age by Sex who survived..."
        print survivedGroupsBySex['Age'].mean()

    def loadData(self):
        i=0
        with open('train.csv','rb') as f:
            reader=csv.reader(f)
            for row in reader:
                if i==0:
                    i += 1
                    continue
                self.data.loc[i]=row
                i +=1
        f.close()

if __name__ == '__main__':
    trainProcessor = TrainInfoProcessor()
    trainProcessor.getSurvivalInfo()
