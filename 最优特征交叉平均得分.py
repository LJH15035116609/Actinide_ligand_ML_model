import os
import pandas as pd

# 文件夹路径
folder_path = 'rf_importance'

# 存储所有符合条件的文件数据
all_data = []

# 遍历文件夹中的文件
for filename in os.listdir(folder_path):
    if filename.endswith('_cross_validation_results.csv'):
        file_path = os.path.join(folder_path, filename)
        # 提取数据集名称
        dataset_name = filename.replace('_cross_validation_results.csv', '')
        # 读取 CSV 文件
        df = pd.read_csv(file_path)
        # 添加文件名列
        df['Filename'] = filename
        # 添加数据集名称列
        df['Dataset Name'] = dataset_name
        # 提取 Dataset、R^2、Mean Squared Error、Mean Absolute Error 列的数据
        df = df[['Filename', 'Dataset Name', 'Dataset', 'R^2', 'Mean Squared Error', 'Mean Absolute Error']]
        # 根据 Dataset 列的值分组，并计算均值
        df_grouped = df.groupby(['Filename', 'Dataset Name', 'Dataset']).mean().reset_index()
        # 将处理后的数据添加到列表中
        all_data.append(df_grouped)

# 合并所有数据
merged_data = pd.concat(all_data)

# 将结果保存到新的 CSV 文件中
output_file = 'combined_results.csv'
merged_data.to_csv(output_file, index=False)

print("处理完成，结果保存到", output_file)
