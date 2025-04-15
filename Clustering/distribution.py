import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取 matched_ligands1.csv 文件
matched_ligands_df = pd.read_csv("matched_ligands3.csv")

# 检查数据是否包含 'LgK' 列
if 'LgK' in matched_ligands_df.columns:
    # 提取 'LgK' 列数据
    lgk_data = matched_ligands_df['LgK']
    
    # 设置绘图风格
    sns.set(style="white")  # No grid
    
    # 绘制直方图
    plt.figure(figsize=(9,8))
    sns.histplot(lgk_data, kde=True, bins=30, color='blue', edgecolor='black')  # kde=True添加核密度估计
    
    # 使用 LaTeX 语法格式化标题和轴标签，确保字体为 Times New Roman
    plt.title(r'cluster3', fontsize=31, fontname='Times New Roman', fontweight='bold')
    plt.xlabel(r'log$K_1$', fontsize=29, fontname='Times New Roman', fontweight='bold')
    plt.ylabel('count', fontsize=29, fontname='Times New Roman', fontweight='bold')
    
    # 修改坐标轴刻度标签：加粗且增大字体
    plt.tick_params(axis='both', which='major', labelsize=14, width=2)  # 加大字体和加粗坐标轴刻度
    plt.xticks(fontsize=29, fontweight='bold', fontname='Times New Roman')  # 加粗 X 轴刻度并增大
    plt.yticks(fontsize=29, fontweight='bold', fontname='Times New Roman')  # 加粗 Y 轴刻度并增大
    
    # 保存图像为文件
    plt.savefig("LgK_distribution3.png", dpi=300, bbox_inches='tight')  # 保存为 PNG 文件，300 DPI 高清
    print("图像已保存为 'LgK_distribution3.png'")
    
    # 显示图形
    plt.show()
else:
    print("'LgK' 列未找到，请检查 CSV 文件中的列名。")



