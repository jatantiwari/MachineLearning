import pandas as pd
import quandl
df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open','Adj. High','Adj. Low']]
df['HL'] =(df['Adj. High']-df['Adj. Low'])

df  = df[["Adj. High",'HL']]
print(df.head())