#BAR CHART
import numpy as np
import pandas as pd
from IPython.core.display import display

import matplotlib.pyplot as plt
import seaborn as sns

# Read the Excel file into a DataFrame
df = pd.read_excel('LifeExp.xls')

df.columns = df.columns.map(str)

#view local authority names
local_authorities = df['Local Authority'].unique()
print(local_authorities)

    
# Filter the dataframe to only include rows with 'Local Authority' equal to 'Hammersmith & Fulham'
df2 = df[df['Local Authority'] == 'Hammersmith and Fulham']


#to create a bar chart later we need to add a column called mean
# Create a new column 'mean' and assign the mean of the values in '2007' to it
df['2007_mean'] = df.groupby('Local Authority')['2007'].transform('mean')

#shift column
# Remove the '2007_mean' column from the DataFrame
col = df.pop('2007_mean')

# Insert the '2007_mean' column at index 7
df.insert(7, '2007_mean', col)



# Set the plot style
sns.set()

# Create the bar chart
ax = sns.barplot(x='Local Authority', 
                 y='2007_mean', palette = 'cool', 
                 width  = 1,
                 data=df)

# Rotate the x-tick labels
plt.xticks(rotation=90)
#axis
plt.ylim(16, 24)

# Remove the grid lines
plt.grid(visible=False)

ax.set_facecolor('white')

# Set the y-axis label
plt.ylabel('2007: mean life expectancy at 65')


# Show the plot
plt.show()













#SCATTER PLOT
import matplotlib.pyplot as plt
import seaborn as sns

# Set the plot style
sns.set()

hammersmith_df = df[df['Local Authority'] == 'Hammersmith and Fulham']

# Initialize empty lists to store the year and values
years = []
values = []

# Iterate through each year from 2006 to 2014
for year in range(2006, 2015):
    year = str(year)
    years.extend([year]*len(hammersmith_df[year].values))
    values.extend(hammersmith_df[year].values)

# Create the scatter plot
fig, ax = plt.subplots()
ax.set_facecolor('white')
ax.scatter(years, values, c=values, cmap='Wistia', s=50, edgecolors='black')
ax.set_xlabel('Years')
ax.set_ylabel('H&F: Life expectancy at 65')
# Remove the grid lines
ax.grid(visible=False)

plt.show()











#BOXPLOT
'''

local_authorities = df['Local Authority']
values_2012 = df['2012']

# Create the box plot
import matplotlib.pyplot as plt
import pandas as pd


# Group the data by 'Local Authority'
grouped_data = df.groupby('Local Authority')['2012']

# Create a list to store the data for each 'Local Authority'
data = []

# Extract the data for each 'Local Authority'
for name, group in grouped_data:
    data.append(group.values)

# Create the box plot
plt.boxplot(data, flierprops = dict(marker='o', markersize=3))
# Set the x-axis labels
plt.xticks(range(1, len(grouped_data.groups) + 1), grouped_data.groups.keys())

# Set the x-axis label
plt.xlabel('Local Authority')

# Set the y-axis label
plt.ylabel('2012: Life expectancy at 65')

plt.xticks(rotation=90)

# Remove grid lines
plt.grid(b=None)

# Change the face color to white
plt.gca().set_facecolor('white')

# Show the plot
plt.show()

'''

#boxplot just Hammermith and Fulham


# Filter the dataframe for 'Hammersmith and Fulham'
HF_df = df[df['Local Authority'] == 'Hammersmith and Fulham']

data = []
years = range(2006, 2015)
#extract data for each year

for year in range(2006,2015):
    data.append(HF_df[str(year)].values)
    
sns.boxplot(data)

#x labels
plt.xticks(range(len(data)), [str(year) for year in years])

# Set the x-axis label
plt.xlabel('Year')

# Set the y-axis label
plt.ylabel('H&F: Life expectancya t 65')

# Remove grid lines
plt.grid(b=None)

# Change the face color to white
plt.gca().set_facecolor('white')

# Show the plot
plt.show()


#heatmap
import seaborn as sns



# Group the data by 'Local Authority' and get the mean of the values
grouped_data = df.groupby(['Local Authority']).mean()

# Transpose the dataframe
grouped_data = grouped_data.T


# Create the heatmap
# ax = 
sns.heatmap(grouped_data, annot=False, xticklabels=True, yticklabels=True)

# Reverse the order of the y-axis
# ax.invert_yaxis()

# Show the plot
plt.show()






