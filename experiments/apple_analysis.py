import pandas as pd

df = pd.read_csv('aapl_5y.csv')
#print(df.columns)
#print(df['Close/Last'].describe())
#print(df['Close/Last'].std())

df_clean = (df['Close/Last'].str.replace("$", "")).astype(float)
print(df_clean.describe())


