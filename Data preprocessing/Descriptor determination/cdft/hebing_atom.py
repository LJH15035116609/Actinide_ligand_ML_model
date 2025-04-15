import pandas as pd

df1 = pd.read_csv('./extract_atom1.csv')
df2 = pd.read_csv('./extract_atom2.csv')
df3 = pd.read_csv('./extract_atom3.csv')

df = pd.concat([df1, df2, df3], axis=1, join='inner')
df.to_csv('./extract_atom.csv', index=False)
