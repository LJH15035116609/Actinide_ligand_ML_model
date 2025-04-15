import pandas as pd
import numpy as np

# 读取CSV文件
df = pd.read_csv("find_clustering_center.csv")

# 按Cluster_Label分组
grouped = df.groupby('Cluster_Label')

# 存储每个簇的质心及其对应的SMILES
centroid_info = []

# 遍历每个簇
for cluster_label, group in grouped:
    # 计算质心 (PCA_Component_1, PCA_Component_2) 坐标
    centroid_pca_1 = group['PCA_Component_1'].mean()
    centroid_pca_2 = group['PCA_Component_2'].mean()
    
    # 计算与质心的距离
    distances = np.sqrt((group['PCA_Component_1'] - centroid_pca_1)**2 + 
                        (group['PCA_Component_2'] - centroid_pca_2)**2)
    
    # 找到离质心最近的点
    closest_point_index = distances.idxmin()
    
    # 获取对应的SMILES
    closest_smiles = group.loc[closest_point_index, 'SMILES']
    
    # 存储结果
    centroid_info.append({
        'Cluster_Label': cluster_label,
        'Centroid_PCA_Component_1': centroid_pca_1,
        'Centroid_PCA_Component_2': centroid_pca_2,
        'Closest_SMILES': closest_smiles
    })

# 将结果转换为DataFrame并输出
centroid_df = pd.DataFrame(centroid_info)
print(centroid_df)
