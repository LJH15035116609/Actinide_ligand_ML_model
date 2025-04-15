import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 指定文件夹路径
folder_path = "rfe"

# 获取文件夹中以'_r2_and_selected_features.csv'结尾的所有文件
file_names = [file for file in os.listdir(folder_path) if file.endswith('_r2_and_selected_features.csv')]

# 遍历每个文件
for file_name in file_names:
    # 构建完整路径
    file_path = os.path.join(folder_path, file_name)
    
    # 读取 CSV 文件
    result_df = pd.read_csv(file_path)

    # 提取每个折的数据
    fold_values = result_df['Fold'].unique()

    # 提取最大特征数量范围
    max_features_range = range(1, 21)

    # 存储每个折的 R^2 值
    fold_r2_scores = []

    # 计算每个折的 R^2 值并存储
    for fold in fold_values:
        fold_data = result_df[result_df['Fold'] == fold]
        fold_r2_scores.append(fold_data['R^2'])

    # 绘制每个折的 R^2 值
    plt.figure(figsize=(7, 5))  
    for i, r2_scores in enumerate(fold_r2_scores, start=1):
        plt.plot(list(max_features_range), r2_scores, marker='o', label=f"Fold {i}")

    # 计算并绘制五折的平均 R^2 值
    mean_r2_scores = np.mean(fold_r2_scores, axis=0)
    plt.plot(list(max_features_range), mean_r2_scores, marker='o', label='Mean', color='black', linestyle='--')

    # 设置图例、轴标签、标题、网格
    plt.legend(loc='lower right')  
    plt.xticks([1, 3, 5, 7, 9, 11, 13, 15, 17, 19])  
    plt.xlabel('Max Features')
    plt.ylabel('R^2')
    plt.title(f'R^2 vs Max Features')
    plt.grid(True)

    # 保存和显示图像
    plt.savefig(f'{file_name[:-4]}_r2_vs_max_features_with_mean.png', bbox_inches='tight')
    




