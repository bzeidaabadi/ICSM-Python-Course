#data input
import numpy as np
import pandas as pd
from IPython.core.display import display


# Read the Excel file into a DataFrame
#df = pd.read_excel('LifeExp.xls')
#df = pd.read_excel('LifeExp copy.xls')
df = pd.read_excel('../LifeExp.xls')
# Read a specific sheet in the Excel file into a DataFrame
#df = pd.read_excel('file.xlsx', sheet_name='Sheet1')


display(df)

# Print the head of the DataFrame
print(df.head())
print(df.shape) #658 rows 14 columns
#print column names
print(df.columns)

print(df.dtypes) #objects and float

#turn to numeric columns 6-14 [:, 7:15]
print(df.iloc[:,7:15])
df.iloc[:,7:15] = pd.to_numeric(df.iloc[:,7:15]) #expects list,tuple or series


#column names to string
df.columns = df.columns.map(str)

#view local authority names
local_authorities = df['Local Authority'].unique()
print(local_authorities)

#make smaller df
Barking_df = df.iloc[:17, :]
print(Barking_df.head)
#using loc
Barking_df = df.loc[df['Local Authority'] == 'Barking and Dagenham', :]
# print(Barking_df.head)
    
# Filter the dataframe to only include rows with 'Local Authority' equal to 'Hammersmith & Fulham'
df2 = df[df['Local Authority'] == 'Hammersmith and Fulham']


#choose 2007 column
HF_LifeExp_07 = df2.loc[:, '2007']
HF_LifeExp_07 = df2.iloc[:, 6]

print(HF_LifeExp_07)

#choose ward column
print(df2['Ward name'])
print(df2['Local Authority'])

#make H&F smaller df

# Sort the dataframe by a specific column (in this case, 'Ward name') in ascending order
df2.sort_values(by='Ward name')

# Drop a specific column from the dataframe
df2.drop(columns=['Old Ward Code'])

# Fill missing values in the dataframe with a specific value
df2.fillna(value=0)

# Filter the dataframe to only include rows with a specific value in a column ward or district
df2[df2['Geography'].isin(['Ward', 'District'])]
df2[df2['Ward name'].isin(['Askew'])]


# Apply a function to each row or column of the dataframe - sum of 2006 + 2007
df2.apply(lambda row: row['2006'] + row['2007'], axis=1)

df2_copy = df2.copy()
df2_copy['06_07'] = df2_copy.apply(lambda row: row['2006'] + row['2007'], axis=1)


# Group the dataframe by a specific column and apply a function to the grouped data
a = df.groupby('Local Authority').apply(lambda group: group['2007'].mean())
a.sort_values(ascending=True)

'''
# Merge two dataframes on a specific column
import numpy as np
import pandas as pd

# Create data for first dataframe
data1 = np.array([['Alice', 10], ['Bob', 12], ['Charlie', 13]])
df1 = pd.DataFrame(data1, columns=['name', 'age'])

# Create data for second dataframe
data2 = np.array([['Alice', 'NYC'], ['Bob', 'LA'], ['Eve', 'SF']])
df2 = pd.DataFrame(data2, columns=['name', 'city'])

# Merge the two dataframes on the 'name' column
df3 = df1.merge(df2, on='name')

print(df3)
'''

#df[columns] = df[columns].apply(np.log)
# df2[columns] = df2[columns].apply(np.log)


