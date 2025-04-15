import pandas as pd

# 定义要操作的列数
L = 12  # 替换为你想要操作的列数

# 读取 Excel 文件
excel_file_path = 'SC_modified1.xlsx'  # 替换为你的 Excel 文件路径
excel_data = pd.read_excel(excel_file_path, sheet_name=None)

# 遍历每个 sheet
for sheet_name, df in excel_data.items():
    # 删除第L列数据中所有不含'°C'的行
    df = df[df.iloc[:, L - 1].astype(str).str.contains('°C', na=False)]
    # 保存修改后的数据到原始 Excel 文件中的相应 sheet
    with pd.ExcelWriter(excel_file_path, engine='openpyxl', mode='a') as writer:
        df.to_excel(writer, sheet_name=sheet_name + '_modified1', index=False)
