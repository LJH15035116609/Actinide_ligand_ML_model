import pandas as pd

df = pd.read_csv('./extract_atom.csv')

# 按照不同number的值分别按q(N)的值从小到大排序
def sort_by_qN(df, number):
    return df[df['number'] == number].sort_values('q(N)')

dfs = []
for i in range(0, df['number'].max()+1):
    dfs.append(sort_by_qN(df, i))

dfss = []
for df in dfs:
    # 行数大于三的取前三行
    if df.shape[0] >= 3:
        df1 = df.iloc[:1, :].reset_index(drop=True)
        df2 = df.iloc[1:2, :].reset_index(drop=True)
        df3 = df.iloc[2:3, :].reset_index(drop=True)
        # 将三个表格按列合并，相同的列名会自动合并
        df = pd.concat([df1, df2, df3], axis=1)
        dfss.append(df)

df_final = pd.concat(dfss, axis=0)
df_final.to_csv('./extract_atom_final.csv', index=False)


