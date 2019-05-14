import pandas as pd
from datetime import datetime
import numpy as np

df=pd.read_csv(r'H:\Major Project\data of us\georgia\01400500.csv',parse_dates=['datetime'],dayfirst=True)
df['date']=pd.to_datetime(df['datetime'])
df=df.set_index('date')
df.drop(['datetime'],axis=1,inplace=True)
sample=df.resample('D').mean()
sample.to_csv('01400500_modified.csv')

