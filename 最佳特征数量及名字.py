import os
import pandas as pd

# 读取 final_average_r2_scores_with_folder.csv 文件
final_results_with_folder = pd.read_csv('final_average_r2_scores_with_folder.csv')

# 创建一个空 DataFrame 来存储最终结果
final_data = pd.DataFrame()

# 遍历每一行
for index, row in final_results_with_folder.iterrows():
    folder = row['Folder']
    file = row['File']
    num = row['num']

    # 读取对应文件夹下的文件
    file_path = os.path.join(folder, file+'.csv')
    print("Processing file:", file_path)  # 打印文件路径
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        print(df.columns)

        # 在文件中找到对应的行并提取
        match_row = df[df['num'] == num]
        print("Matched row:", match_row)  # 打印匹配行
        if not match_row.empty:
            # 添加 Folder 和 File 列信息
            match_row['Folder'] = folder
            match_row['File'] = file
            # 将匹配到的行添加到最终结果中
            final_data = pd.concat([final_data, match_row])

# 保存结果到 CSV 文件
final_data.to_csv('final_data_with_num.csv', index=False)
