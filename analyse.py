import pandas as pd 
import numpy as np 



df = pd.read_csv('jumia_articles_prep1.csv')
print(df.head())

# print(df['Article Brand'].value_counts())

##count the number of articles with the value_counts equal to 1
print(df['Article Brand'].value_counts().loc[1])

# Assuming 'df' is your DataFrame and 'Article Brand' is the column you're interested in
unique_count = df['Article Brand'].nunique()
print(unique_count)
