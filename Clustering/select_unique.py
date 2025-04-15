
import pandas as pd

# 读取csv文件
df = pd.read_csv('smiles.csv')

# 删除重复的SMILES
df_unique = df.drop_duplicates(subset='smiles')

# 将结果保存到新的csv文件
df_unique.to_csv('unique_smiles.csv', index=False)
