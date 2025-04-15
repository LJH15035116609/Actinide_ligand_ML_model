import re

# 读取txt文件
def read_txt(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    return lines

path = './extract_all.txt'
lines = read_txt(path)

# 用正则表达式匹配‘Atom     q(N)’的行号存入列表
indexs = []
i = 0
for line in lines:
    if re.match(r'^Atom\s+s-', line.strip()):
        index = i
        indexs.append(index)
    i += 1

# 循环提取匹配的行号的下一行除去行首和行尾的空格以及换行符后存入列表，直到匹配到只有换行符的行或者到达文件末尾
extract_list = []
for index in indexs:
    while True:
        index += 1
        if index == len(lines) or re.match(r'^\s*$', lines[index]):
            break
        else:
            extract_list.append(lines[index].strip())

# 将提取出的列表中的元素中间的空格替换为’,‘后存入csv文件，表头为‘Atom,q(N),q(N+1),q(N-1),f-,f+,f0,CDD’
with open('./extract_atom3.csv', 'w') as f:
    f.write('Atom,s-,s+,s0,s+/s-,s-/s+\n')
    for line in extract_list:
        f.write(re.sub(r'\s\s+', ',', line) + '\n')
