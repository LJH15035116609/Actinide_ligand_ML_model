from rdkit import Chem
import pandas as pd

# 读取包含 SMILES 的 CSV 文件
df = pd.read_csv('unique_smiles.csv')

# 添加一列来存储规范化后的 SMILES
df['Canonical_SMILES'] = None

# 遍历 DataFrame 中的每一行，计算规范 SMILES
for index, row in df.iterrows():
    original_smiles = row['smiles']

    # 利用 RDKit 计算规范 SMILES
    mol = Chem.MolFromSmiles(original_smiles)
    canonical_smiles = Chem.MolToSmiles(mol, isomericSmiles=False) if mol is not None else None

    # 将规范 SMILES 存储到 DataFrame
    df.at[index, 'Canonical_smiles'] = canonical_smiles

# 将结果保存到新的 CSV 文件
df.to_csv('canonical_smiles.csv', index=False)
