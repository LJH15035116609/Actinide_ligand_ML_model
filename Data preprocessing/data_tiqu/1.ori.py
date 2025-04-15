import pandas as pd
from pdfminer.high_level import extract_text

# 读取PDF文件
with open('Lu.pdf', 'rb') as file:
    text = extract_text(file)

# 将文本按行分割
lines = text.split('\n')

# 创建一个空的 DataFrame 用于存储提取的内容
df = pd.DataFrame(columns=['Extracted_Text'])

# 遍历文本行
i = 0
while i < len(lines):
    line = lines[i]
    # 如果当前行包含 "*" 符号，则提取下一行的内容
    if '*' in line:
        if i + 1 < len(lines):
            next_line = lines[i + 1]
            df = df.append({'Extracted_Text': next_line}, ignore_index=True)
        i += 1  # 跳过下一行
    # 如果当前行以"La+++"开头，则提取该行的内容
    elif line.strip().startswith('Lu+++'):
        df = df.append({'Extracted_Text': line}, ignore_index=True)
    i += 1

# 将提取的内容保存到 CSV 文件中
df.to_csv('Lu.csv', index=False)

