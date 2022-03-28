import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
df = pd.DataFrame(exam_data)

#39
s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
s2 = pd.Series(['10', '20', 'php', '30.12', '40'])

df1 = pd.concat([s1,s2], axis=1)
print(df1)

#40
print(df.sample(frac=1)) #shuffle

#45
d = {'col1': [1, 2, 3, 4, 7], 'col2': [4, 5, 6, 9, 5], 'col3': [7, 8, 12, 1, 11]}
df1 = pd.DataFrame(data=d)
print(df1['col2'].argmax()) #row where max value is in col2

#47
print(df1.iloc[2]) #row no2

#50
df = df.sort_values(['score', 'attempts'], ascending=[True, True])
print(df)

#53
df1.insert(loc=0, column='col0', value=[0, 0, 0, 0, 0])
print(df1)

#55
df2 = pd.DataFrame( {'col1':['C1','C1','C2','C2','C2','C3','C2'], 'col2':[1,2,3,3,4,6,5]})

df2 = df2.groupby('col1')['col2'].apply(list) #group by column1 with lists in column2
print(df2)

#58
print(df1.loc[:, df1.columns != 'col2'])

#59
print(df1.head(3)) #first 3 rows
print(df1.tail(3))
print(df1.iloc[:4])

#70
#categorize each value in a column

df3 = pd.DataFrame({
        'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Syed Wharton', 'Kierra Gentry'],
        'age': [18, 22, 85, 50, 80, 5]
})

df3["age_group"] = pd.cut(df3["age"], bins = [0, 18, 65, 99], labels = ["kid", "adult", "old"])

print(df3["age_group"])

#80

df4 = pd.DataFrame({'W':[68,75,86,80,None],'X':[78,85,None,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]});
df5 = pd.DataFrame({'W':[78,75,86,80,None],'X':[78,85,96,80,76], 'Y':[84,84,89,83,86],'Z':[86,97,96,72,83]});

print(df4 != df5)
print(df4.ne(df5))

#81
#first 3 rows by smallest values in column specified
print(df1.nsmallest(3, 'col1'))
print(df1.nsmallest(3, 'col2'))
