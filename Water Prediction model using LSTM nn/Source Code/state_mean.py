import pandas as pd
import glob

path="C:/Users/HARI/PycharmProjects/sampleProject/georgia"
allFiles = glob.glob(path+"/*.csv")

list_ = []

for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    list_.append(df)

frame = pd.concat(list_, axis = 0,sort=True)
keep_col=['date','temperature','dissolved_oxygen','pH']
new_f=frame[keep_col]


f1=new_f.groupby('date').mean()
f1.to_csv('georgia.csv')