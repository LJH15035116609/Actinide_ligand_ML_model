import os
import pandas as pd

# 要处理的文件夹列表
folders = ['ab_importance', 'dt_importance', 'gb_importance', 'rf_importance', 'mutual_info', 'spearman', 'rfe']

# 创建一个空 DataFrame 来存储结果
final_results = pd.DataFrame()

# 遍历每个文件夹
for folder in folders:
    # 读取 average_r2_scores.csv 文件
    file_path = os.path.join(folder, 'average_r2_scores.csv')
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)

        # 按照 'File' 列分组并找到每组中 'Mean R^2' 最大的行
        grouped_max = df.groupby(df.index // 20)['Mean R^2'].idxmax()

        # 根据索引提取这些行并添加到结果 DataFrame 中
        result_df = df.loc[grouped_max]

        # 添加一个列来表示文件来自哪个文件夹
        result_df['Folder'] = folder

        # 将结果添加到最终结果中
        final_results = pd.concat([final_results, result_df])

# 重置索引并保存结果到 CSV 文件
final_results.reset_index(drop=True, inplace=True)
final_results.to_csv('final_average_r2_scores_with_folder.csv', index=False)
