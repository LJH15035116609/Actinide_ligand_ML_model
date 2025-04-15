import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 指定文件夹路径
folder_path = "spearman"

# 获取文件夹中以'_r2_and_selected_features.csv'结尾的所有文件
file_names = [file for file in os.listdir(folder_path) if file.endswith('_r2_and_selected_features.csv')]

# 创建一个空DataFrame来存储结果
result_data = pd.DataFrame()

# 遍历每个文件
for file_name in file_names:
    # 构建完整路径
    file_path = os.path.join(folder_path, file_name)
    
    # 读取 CSV 文件
    result_df = pd.read_csv(file_path)

    # 提取每个折的数据
    fold_values = result_df['Fold'].unique()

    # 存储每个折的 R^2 值
    fold_r2_scores = []

    # 计算每个折的 R^2 值并存储
    for fold in fold_values:
        fold_data = result_df[result_df['Fold'] == fold]
        fold_r2_scores.append(fold_data['R^2'])

    # 计算五折的平均 R^2 值
    mean_r2_scores = np.mean(fold_r2_scores, axis=0)

    # 构建当前文件的数据框
    file_data = pd.DataFrame({'Max Features': list(range(1, 21)), 'Mean R^2': mean_r2_scores})
    file_data['File'] = file_name[:-4]

    # 重新排列列的顺序
    file_data = file_data[['File', 'Max Features', 'Mean R^2']]

    # 将当前文件的数据追加到结果数据框
    result_data = pd.concat([result_data, file_data], ignore_index=True)

# 将结果保存为CSV文件
result_data.to_csv('spearman_r2_scores.csv', index=False)





