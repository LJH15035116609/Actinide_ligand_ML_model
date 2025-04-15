import pandas as pd

# 读取 cluster_ligand_match_logk.csv 文件
cluster_df = pd.read_csv("cluster_ligand_match_logk.csv")

# 读取 ligand_match_logk.csv 文件
ligand_df = pd.read_csv("ligand_match_logk.csv")

# 在 cluster_ligand_match_logk 中提取 SMILES 列
smiles_list = cluster_df['cluster1'].tolist()

# 从 ligand_match_logk 中根据 SMILES 值提取对应的行
matched_rows = ligand_df[ligand_df['SMILES'].isin(smiles_list)]

# 保存结果到新的 CSV 文件
matched_rows.to_csv("matched_ligands1.csv", index=False)

# 输出完成提示
print("结果已保存到 'matched_ligands.csv'")
