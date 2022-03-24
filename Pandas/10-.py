import pandas as pd
import numpy as np

#11
ds = pd.Series(['200', '100', 'python', '300.12', '400'])
ds1 = pd.Series(ds).sort_values(ascending=True)
print(ds1)

#12
ds2 = ds1.append(pd.Series(['500', 'php']))
print(ds2)

#13
ds = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
n = 6
new = ds[ds < n]
print(new)

#14
s = pd.Series(data = [1,2,3,4,5], index = ['A', 'B', 'C', 'D', 'E'])
print(s)
s = s.reindex(index = ['B', 'A', 'C', 'D', 'E'])
print(s)

#15
s = pd.Series([1,2,3,4,5,6,7,8,9,5,3])
print(s.mean())
print(s.std())

#16
s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([2,4,6,8,10])
s3 = s1[~s1.isin(s2)]
print(s3)

#17
s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([2,4,6,8,10])
s11 = pd.Series(np.union1d(s1, s2))
s22 = pd.Series(np.intersect1d(s1, s2))
sr = s11[~s11.isin(s22)]
print(sr)

#19
# s = pd.Series(np.random.randint(1, 10, size=20))
# print(s)
# r = s.value_counts()
# print(r)

#20
# s = pd.Series(np.random.randint(1, 5, [15]))
# print(s)
# print("frecv", s.value_counts())
# result = s[~s.isin(s.value_counts().index[:1])] = 'Other'
# print(s)

#24
s = pd.Series(['php', 'python', 'java', 'ana'])
s1 = s.map(lambda x: x[0].upper() + x[1:-1] + x[-1].upper())
print(s1)

#26
s2 = pd.Series([2,4,6,8,10])
print(s2.diff().tolist())

#33
str = "ana are mere"
sr = pd.Series(list(str))
frecve = sr.value_counts()
value = frecve.dropna().index[-1]
print(frecve)
print(value)
result = "".join(sr.replace(' ', value))
print(result)

#36
s = list('ABCDEFGHIJKLMNOPQRSTUVW')
dict = dict(zip(s, np.arange(5)))
ser = pd.Series(dict)
df = ser.to_frame().reset_index()
print(df)

#37
s1 = pd.Series(range(6))
s2 = pd.Series(list('abcdef'))
df = pd.concat([s1, s2], axis = 1)
print(df)

