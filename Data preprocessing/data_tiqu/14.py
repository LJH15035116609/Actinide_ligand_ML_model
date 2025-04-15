import pandas as pd

# 读取csv文件
df = pd.read_csv('all.csv')

# 删除smiles列中包含NaN的行
df = df.dropna(subset=['smiles'])

# 保存到新的csv文件
df.to_csv('all_clean.csv', index=False)
