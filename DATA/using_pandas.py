import pandas

df = pandas.read_table('../DATA/customerdata1.txt')
print(df.info())
print(df.describe())

print(df)