import pandas as pd 
import numpy as np 

data = pd.read_csv('jumia_articles.csv')

## Finding Number of rows and columns in the dataset
# rows_count, columns_count = data.shape
# print(f"There are {rows_count} rows, and {columns_count} columns")

##Format of the collected data
# print(data.head())

### DATA PREPROCESSNG 
# data.info()

#null entries in each and every row
print(data.isnull().sum())

##from the above, all columns don't have the number of ratings. This should be dropped. setting inplace=True will have an effect on original dataset
data1 = data.drop('Number of Ratings', axis=1)
# print(data1.isnull().sum())
# print(data1.head())


## PREPROCESSING EACH AND EVERY COLUMN
#creatin a new column known as brand and adding the first word in every Article Name to it. Placing the column after the first column
# data1['Article Brand'] = data1['Article Name'].str.split().str[0]
# cols = list(data1.columns)
# cols.insert(1, cols.pop(cols.index('Article Brand')))  # Move 'brand' to the second position

# # Reorder the DataFrame columns
# data1 = data1[cols]
# data1.info()

##Article rating Column
data1['Article Rating'] = data1['Article Rating'].str.split().str[0]
print(data1['Article Rating'])
