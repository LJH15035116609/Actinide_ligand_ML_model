#从rdkit导出物理化学描述符代码
import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors
df = pd.read_csv('unique_generated_smiles.csv')
desc_list = [x[0] for x in Descriptors.descList]
df_out = pd.DataFrame()
for i, row in df.iterrows():
    # 从smiles字符串创建分子对象
    m = Chem.MolFromSmiles(row['smiles'])
    descrs = Descriptors.CalcMolDescriptors(m)
    df_out.loc[i, desc_list] = descrs
df_out.to_csv('descriptors.csv', index=False)