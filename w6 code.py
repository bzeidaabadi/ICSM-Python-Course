#numpy making arrays
import numpy as np

# Create a 1D array with 4 elements
a = np.array([1, 2, 3, 4])

# Create a 2D array with 3 rows and 4 columns
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Create an array with random values
c = np.random.rand(3, 4)

# Create an array of zeros
d = np.zeros((3, 4))

# Create an array of ones
e = np.ones((3, 4))

import numpy as np

# Create a 2D array with random values
a = np.random.rand(3, 4)

# Select the element at the 2nd row and 3rd column. [row, column]
b = a[1, 2]

# Select the 2nd column of the array
c = a[:, 1]

# Select the 2nd and 3rd rows of the array
d = a[1:3, :]

# Select the element at the 2nd row and 3rd column and change its value
a[1, 2] = 0


#create df
#numpy
import numpy as np
import pandas as pd

# Create an array of values
data = np.array([[1, 2, 3], [4, 5, 6]])

# Create a DataFrame from the array
df = pd.DataFrame(data, columns=['a', 'b', 'c'])

# Print the DataFrame
print(df)


#pandas
import pandas as pd

# Create a dictionary of values
data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Print the DataFrame
print(df) 


#data input


#input, read, write

import csv

# Open the CSV file in read mode
with open('../cereal.csv', 'r') as file:
  # Use the csv.reader() function to read the file
  reader = csv.reader(file)
  
  # Print each row in the file
  for row in reader:
    print(row)
    
# Open the file in write mode
with open('filename.txt', 'w') as file:
  # Write to the file
  file.write('Some text')




#TRY and EXCEPT

import pandas as pd

# Read the CSV file into a DataFrame using the read_csv() function
df = pd.read_csv('../cereal.csv')

import pandas as pd

try:
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv("cereal1.csv")

except FileNotFoundError:
    # If the file is not found, print an error message
    print("The file 'data.csv' was not found. Please make sure the file exists and is in the correct location.")

except Exception as e:
    # For any other errors, print the error message
    print("An error occurred while reading the file:", e)

try:
    x = 5 / 0
except ZeroDivisionError:
    print("Division by zero is not allowed!")
except Exception as e:
    print("An error occurred:", e)





import pandas as pd

# Read the CSV file into a DataFrame using the read_csv() function
df = pd.read_csv('cereal.csv')

# Print the first 5 rows of the DataFrame
print(df.head())

# Print the shape of the DataFrame
print(df.shape) #79 rows 1 column

import pandas as pd
import numpy as np
# Read the CSV file into a DataFrame using the read_csv() function
# Set the first row as the column names and skip the second row
cereal_df = pd.read_csv('cereal.csv', names=['name', 'mfr', 'type', 'calories', 'protein', 'fat',
                                             'sodium', 'fiber', 'carbo', 'sugars', 'potass', 'vitamins',
                                             'shelf', 'weight', 'cups', 'rating'], skiprows=2)

# Print the first 5 rows of the DataFrame
print(cereal_df.head())
print(cereal_df.shape) #78 rows, 16 columns


# # Print the column names of the DataFrame
print(cereal_df.columns)

# # Print the data types of the columns in the DataFrame
print(cereal_df.dtypes)

# # Print the summary statistics of the DataFrame
print(cereal_df.describe())

# Select a specific column from the DataFrame and print its unique values
print(cereal_df['name'].unique())

# Remove the 'Shelf' and 'Weight' columns from the DataFrame
df = df.drop(columns=['Shelf', 'Weight'])
print(cereal_df.dtypes) #object/string

# # Drop the 'B' column
# df = df.drop(columns=['B'])
# Remove row 1 from the DataFrame
cereal_df = cereal_df.drop(index=0)
#print(cereal_df.head())
#turn to numeric
cereal_df['rating'] = pd.to_numeric(cereal_df['rating']) #row 1 cannot turn to numeric

# Round the 'rating' column to 1 decimal place - np.round - expects array
cereal_df['rating'] = np.round(cereal_df['rating'], 1)

# Sort the DataFrame by the 'Cereal Rating' column in descending order
cereal_df_sorted = cereal_df.sort_values('rating', ascending=False)

print(cereal_df_sorted.head())

# Print the first 5 rows of the DataFrame
print(df.head())








import numpy as np

# Create a 2D array with random values
a = np.random.rand(3, 4)

b = a[1, 2]

print(b)


