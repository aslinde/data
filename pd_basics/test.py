import os
import pandas as pd
import re

df = pd.read_csv('pokemon_data.csv')
#print(df)

df_poke_x = pd.read_excel('pokemon_data.xlsx')
#print(df_poke_x)

df_poke_tab = pd.read_csv('pokemon_data.csv', delimiter ="\t")
#print(df_poke_tab)

## Reading
#print(df.columns)

#print(df["Name"][0:5])

#print(df.loc[df["Type 1"] == "Fire"])

## RegEX
print(df.loc[df["Type 1"].str.contains('Fire|Grass', regex=True)])

print(df.loc[df["Type 1"].str.contains('fire|grass', flags = re.I, regex=True)])

print(df.loc[df["Name"].str.contains('^pi[a-z]*', flags = re.I, regex=True)])


df.loc[df['Type 1'] == "Fire", 'Type 1' ] = 'Flamer'
print(df)
df.loc[df['Type 1'] == "Flamer", 'Type 1' ] = 'Fire'
print(df)
df.loc[df['Type 1'] == "Fire", 'Legendary' ] = True