import os
import pandas as pd
import numpy as np
import random
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
os.chdir(r'E:\training\Projects\Vehicle_traffic_data_mining')
#df=h2o.import_frame(path='E:\training\Projects\Vehicle_traffic_data_mining\DfTRoadSafety_Accidents_2014.csv')
df=pd.read_csv('DfTRoadSafety_Accidents_2014.csv')
Features=df[['Number_of_Vehicles','Day_of_Week','Junction_Detail',
    'Speed_limit','Weather_Conditions','Road_Type','Light_Conditions',
                  'Junction_Control','Urban_or_Rural_Area']]
myx=['Number_of_Vehicles','Day_of_Week','Junction_Detail',
    'Speed_limit','Weather_Conditions','Road_Type','Light_Conditions',
                  'Junction_Control','Urban_or_Rural_Area']
myy=['Accident_Severity']
Severity=df[['Accident_Severity']]
#print(Severity)
#Label=np.zeros(len(Severity))

ind=Severity==3
Label=[]
for i in np.array(ind):
    
    if i==True:
        Label.append(1)
    else:
        Label.append(0)
Label=np.array(Label)
numFeatures=len(Features)
numTrainFeatures=np.floor(0.8*numFeatures)
numTestFeatures=numFeatures-numTrainFeatures
ind=random.sample(range(numFeatures),(numFeatures))

trainIndices=ind[1:int(numTrainFeatures)]
testIndices=ind[int(numTrainFeatures+1):]
trainFeatures=Features.loc[trainIndices,:]
trainLabels=Label[trainIndices[:]];
testFeatures=Features.loc[testIndices,:]
testLabels=Label[testIndices[:]]

rf = RandomForestClassifier(n_estimators=100) # initialize
rf.fit(trainFeatures,trainLabels) # fit the data to the algorithm
results = rf.predict(trainFeatures)
ind=(results==trainLabels);
ind=list(ind);
trainAcc_tree=float(ind.count(True))/float(len(trainLabels));
print'Training Accuracy using RandomForest is:',trainAcc_tree*100;
results = rf.predict(testFeatures)
ind=(results==testLabels);
ind=list(ind);
testAcc_tree=float(ind.count(True))/float(len(testLabels));
print 'Testing Accuracy Using RandomForest is:',testAcc_tree*100;



from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
results= gnb.fit(trainFeatures,trainLabels)
print(results)
ind=(results==trainLabels);
ind=list(ind);
trainAcc_tree=float(ind.count(True))/float(len(trainLabels));
#print'Training Accuracy using naive_bayes is:',trainAcc_tree*100;

results= gnb.fit(trainFeatures,trainLabels).predict(testFeatures)
ind=(results==testLabels);
ind=list(ind);
testAcc_tree=float(ind.count(True))/float(len(testLabels));
print 'Testing Accuracy Using naive_bayes is:',testAcc_tree*100;


def proportion(total_range,attri_range):
    return float(attri_range)/float(total_range)*100

#Data Analysis
analysis1=len(df.loc[df.Speed_limit==30,:])
analysis11=len(df.loc[((df.Speed_limit==30) & (df.Accident_Severity==1)) ,:])
print 'proportion 30',proportion(len(df),analysis1)
print  'proportion2',proportion(analysis1,analysis11)

analysis2=len(df.loc[df.Urban_or_Rural_Area==1,:])
ana2=proportion(len(df),analysis2)
print 'analysis2 is ',ana2


analysis4=len(df.loc[df.Weather_Conditions==1,:]);
ana4=proportion(len(df),analysis4)
print 'analysis4 is',ana4

analysis5=len(df.loc[df.Light_Conditions==1,:])
ana5=proportion(len(df),analysis5)
print 'analysis5 is',ana5


#Analysis Number 7
acc_sunday=(float(len(df.loc[df.Day_of_Week==1,:]))/len(df))*100
#print 'acc_sunday',acc_sunday

acc_monday=float(len(df.loc[df.Day_of_Week==2,:]))/len(df)*100
#print 'acc_monday',acc_monday

acc_tuesday=(float(len(df.loc[df.Day_of_Week==3,:]))/len(df))*100
#print 'acc_tuesday',acc_tuesday

acc_wednesday=(float(len(df.loc[df.Day_of_Week==4,:]))/len(df))*100
#print 'acc_wednesday',acc_wednesday

acc_thursday=(float(len(df.loc[df.Day_of_Week==5,:]))/len(df))*100
#print 'acc_thursday',acc_thursday

acc_friday=(float(len(df.loc[df.Day_of_Week==6,:]))/len(df))*100
#print 'acc_friday',acc_friday

acc_saturday=(float(len(df.loc[df.Day_of_Week==7,:]))/len(df))*100
#print 'acc_saturday',acc_saturday
labels=['sunday','monday','Tuesday','wednesday','Thursday','Friday','Saturday']
data=[acc_sunday,acc_monday,acc_tuesday,acc_wednesday,acc_thursday,acc_friday,acc_saturday];
explode=(0.0,0.0,0.0,0.0,0.0,0.1,0.0)
plt.pie(data,explode=explode,labels=labels,shadow=True, autopct='%1.1f%%')
plt.show()


