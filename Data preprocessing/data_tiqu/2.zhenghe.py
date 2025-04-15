import pandas as pd

# 要处理的元素名称列表
elements = ['La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu']

# 遍历每个元素
for element in elements:
    # 读取 CSV 文件
    df = pd.read_csv(f'{element}.csv')
    
    # 新建一列，并初始化为空字符串
    new_column_data = [''] * len(df)
    df.insert(0, 'New_Column', new_column_data)

    # 遍历第二列中的每一行
    for index, row in df.iterrows():
        # 如果第二列中的单元格内容不以当前元素名称开头
        if not str(row[df.columns[1]]).startswith(element):
            # 获取要添加内容的行和列的索引
            new_row_index = index + 1
            new_col_index = 1
            # 如果要添加内容的行索引超出了 DataFrame 的范围，则跳过
            if new_row_index >= len(df):
                continue
            # 获取要添加内容的行和列的索引，并将内容添加到相应的单元格中
            df.at[new_row_index, df.columns[new_col_index - 1]] = row[df.columns[new_col_index]]
            # 删除原来单元格内容
            df.at[index, df.columns[new_col_index]] = ''

    df.to_csv(f'{element}_modified.csv', index=False)
    df = pd.read_csv(f'{element}_modified.csv')

    # 删除第二列中包含空白单元格的行
    df = df.dropna(subset=[df.columns[1]])

    # 重置索引
    df.reset_index(drop=True, inplace=True)

    # 对第一列中的空白单元格进行填充，使用上一个单元格的内容
    df[df.columns[0]] = df[df.columns[0]].fillna(method='ffill')

    # 保存修改后的 DataFrame 到相应的文件中
    df.to_csv(f'{element}_modified.csv', index=False)

# 创建一个 ExcelWriter 对象
writer = pd.ExcelWriter('SC.xlsx')

# 遍历每个元素
for element in elements:
    # 读取对应的修改后的 CSV 文件
    df = pd.read_csv(f'{element}_modified.csv')
    
    # 将 DataFrame 写入 Excel 文件的不同工作表中
    df.to_excel(writer, sheet_name=element, index=False)

# 保存 Excel 文件
writer.save()
