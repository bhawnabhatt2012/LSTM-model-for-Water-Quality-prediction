import pandas as pd

df=pd.read_csv('new_york.csv')
df['code']='NY'
df=df.set_index(df['date'])
df.to_csv('new_york_modified.csv')