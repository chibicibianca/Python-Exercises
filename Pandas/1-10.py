#Write a Pandas program to create and display a one-dimensional array-like
# object containing an array of data using Pandas module

import pandas as pd
import numpy as np

ds = pd.Series([1, 2, 3, 4, 5, 6])
print(ds)

# Write a Pandas program to convert a Panda module Series to Python list and it's type.

print(ds.tolist())
print(type(ds.tolist()))

#5. Write a Pandas program to convert a dictionary to a Pandas series.
# Original dictionary:
# {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
# Converted series:
# a 100
# b 200
# c 300
# d 400
# e 800
# dtype: int64

d1 = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
print(d1)

new_series = pd.Series(d1)
print(new_series)

#6. Write a Pandas program to convert a NumPy array to a Pandas series.
# NumPy array:
# [10 20 30 40 50]
# Converted Pandas series:
# 0 10
# 1 20
# 2 30
# 3 40
# 4 50

np_arr = np.array([10, 20, 30, 40, 60])

series = pd.Series(np_arr)
print(series)

# 7. Write a Pandas program to change the data type of given a column or a Series.
# Original Data Series:
# 0 100
# 1 200
# 2 python
# 3 300.12
# 4 400
# Change the said data type to numeric:
# 0 100.00
# 1 200.00
# 2 NaN
# 3 300.12
# 4 400.00

ds = pd.Series(['100', '200', 'python', '300.12', '400'])
s = pd.to_numeric(ds, errors = 'coerce')
print(s)

#8. Write a Pandas program to convert the first column of a DataFrame as a Series.
# Original DataFrame
# col1 col2 col3
# 0 1 4 7
# 1 2 5 5
# 2 3 6 8
# 3 4 9 12
# 4 7 5 1
# 5 11 0 11
# 1st column as a Series:
# 0 1
# 1 2
# 2 3
# 3 4
# 4 7
# 5 11
# Name: col1

d = {'col1' : [1,2,3,4,7,11], 'col2' : [4,5,6,9,5,0], 'col3' : [7,5,8,12,1,11]}
df = pd.DataFrame(data=d, columns=['col1'])
print(df)
s1 = df.iloc[:, 0]  # instead of ix
print(s1)
print(type(df))

#9. Write a Pandas program to convert a given Series to an array.
# Original Data Series:
# 0 100
# 1 200
# 2 python
# 3 300.12
# 4 400
# dtype: object
# Series to an array
# ['100' '200' 'python' '300.12' '400']

ds = pd.Series(['100', '200', 'python', '300.12', '400'])
arr = np.array(ds.tolist())
print(arr)

#10. Write a Pandas program to convert Series of lists to one Series.
# Original Series of list
# 0 [Red, Green, White]
# 1 [Red, Black]
# 2 [Yellow]
# dtype: object
# One Series
# 0 Red
# 1 Green
# 2 White
# 3 Red
# 4 Black
# 5 Yellow
# dtype: object

ds = pd.Series([['Red', 'Green', 'White'], ['Red', 'Black'], ['Yellow']])
ds = ds.apply(pd.Series).stack().reset_index(drop=True)
print(ds)
