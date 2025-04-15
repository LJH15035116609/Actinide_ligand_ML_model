import pandas as pd

# 读取 Excel 文件
xlsx = pd.ExcelFile('SC_modified.xlsx')

# 创建一个 ExcelWriter 对象
writer = pd.ExcelWriter('SC_modified2.xlsx')

# 遍历每个工作表
for sheet_name in xlsx.sheet_names:
    # 读取工作表
    df = pd.read_excel(xlsx, sheet_name)
    
    # 在第一列后插入16列空白列
    for i in range(16):
        df.insert(1, f'Blank_Column_{i+1}', '')

    # 保存处理后的结果
    df.to_excel(writer, sheet_name=sheet_name, index=False)

# 保存 Excel 文件
writer.save()
