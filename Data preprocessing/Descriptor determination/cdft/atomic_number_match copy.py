import pandas as pd

# 读取两个表格
matching_table = pd.read_csv('finnal_descri.csv')
target_table = pd.read_csv('match.csv')


# 获取第一个表格的第一列（匹配列）
matching_column = matching_table.iloc[:, 0]

# 创建一个 DataFrame 用于存储匹配的行
matched_rows = pd.DataFrame(columns=matching_table.columns)

# 遍历第二个表格的第一列
for index, value in enumerate(target_table.iloc[:, 0]):
    # 检查当前值是否在第一个表格的匹配列中
    if value in matching_column.values:
        # 获取匹配行的索引
        matching_row_index = matching_column[matching_column == value].index[0]

        # 将匹配行添加到新的 DataFrame
        matched_rows = matched_rows.append(matching_table.loc[matching_row_index])

# 将结果保存到新的 CSV 文件
matched_rows.to_csv('matched_rows.csv', index=False)
