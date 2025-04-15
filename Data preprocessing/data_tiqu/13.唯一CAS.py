import pandas as pd

# 从CSV文件中读取数据
df = pd.read_csv('CAS1.csv')

# 记录原始列顺序
original_columns = df.columns.tolist()

# 删除重复的CAS值
df.drop_duplicates(subset='CAS', keep='first', inplace=True)

# 将结果保存到新的CSV文件中，并保持原始列顺序
df.to_csv('CAS_no_duplicates1.csv', index=False, columns=original_columns)

print("Duplicate CAS values have been removed from the CSV file.")
