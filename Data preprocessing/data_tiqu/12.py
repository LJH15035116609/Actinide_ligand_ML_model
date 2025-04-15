import pubchempy as pcp
import pandas as pd

# 从CSV文件中读取CAS号
df = pd.read_csv('CAS_no_duplicates.csv')

# 定义要获取的属性
properties = ['CanonicalSMILES']

# 创建一个空的SMILES列
df['SMILES'] = ''

# 对每个CAS号进行操作
for i, cas in enumerate(df["CAS"]):
    # 获取属性
    try:
        info = pcp.get_properties(properties, cas, 'name')
        smiles = info[0]["CanonicalSMILES"]
    except:
        smiles = "NaN"
    # 将SMILES添加到列表中
    df.at[i, 'SMILES'] = smiles

# 将结果保存到新的CSV文件中
df.to_csv('CAS_with_SMILES.csv', index=False)

print("SMILES have been added to the CSV file.")
