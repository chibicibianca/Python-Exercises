
import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
            'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
            'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
            'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data=exam_data, index=labels)

#4
print(df[:3])
#5
print(df[['name', 'score']])
#6
print('Specifici columns and rows:', df.iloc[[1,3,5], [1,3]])
#7
print('Attempts >2:', df[df['attempts']>2])
#8
print('Coloane si linii:', len(df.axes[1]), len(df.axes[0]))
#9
print(df[df['score'].isnull()])
#10
print(df[df['score'].between(15,20)])
#12
df.loc['d', 'score'] = 11.5
print(df)
#13
print(df['attempts'].sum())
#14
print(df['score'].mean())
#15
df.loc['k'] = ['Suresh', 15.5, 1, 'yes']
print(df)
df = df.drop('k')
print(df)
#17
ds = df['qualify'].replace('yes', 'True').replace('no', 'False')
print(ds)
#22
print(list(df.columns.values))
#23
df = df.rename(columns={'score': 'scores'})
print(df)

#24
print(df.loc[df['scores'] >10])
#25
df = df[['name', 'attempts', 'scores', 'qualify']]
print(df)

#32
df = df.fillna(0)
print(df)

#34
