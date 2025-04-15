import re

# 读取txt文件
def read_txt(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    return lines

path = './extract_all.txt'
lines = read_txt(path)

# 用正则表达式匹配‘E(N):’的行，并导出整行
extract_list = []
for line in lines:
    match = re.match(r'^\s*Chemical potential: (.+)', line.strip())
    if match:
        extract_list.append(match.group(1).strip())

# 将提取出的列表中的元素中间的空格替换为’,‘后存入csv文件，表头为‘E(N)’
with open('./Chemical_potential.csv', 'w') as f:
    f.write('Chemical_potential\n')
    for line in extract_list:
        f.write(re.sub(r'\s\s+', ',', line) + '\n')






