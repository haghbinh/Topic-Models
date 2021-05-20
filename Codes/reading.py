import pandas as pd
df1 = pd.read_csv('dataset\CS-1977-1993.csv')
df1.head(3)
df1.columns

features = ['Title', 'Year','Abstract','Author Keywords', 'Index Keywords','Cited by','Affiliations']
from os import listdir,chdir
chdir("dataset")
path=listdir()
mydata = None
for i in path:
    df0 = pd.read_csv(i,usecols=features)
    if mydata is not None:
        mydata = mydata.append(df0)
    else:
        mydata = df0.copy()

mydata.to_csv('Dataset_00_02_10.csv',index=False)