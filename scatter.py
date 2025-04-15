import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 假设 matched_ligands_df 是你的数据框，读取它
matched_ligands_df = pd.read_csv("train_selected.csv")

# 需要绘制散点图的列名，按顺序排列
columns_to_plot = [
    'VSA_EState2', 'SMR_VSA1', 'Kappa3', 'Chi1n', 'HOMO_metal', 
    'BCUT2D_MWLOW', 'pKa', 'Ionic strength', 'NumHDonors', 's+', 
    'BCUT2D_MRLOW', 'Chi4v', 'VIP', 'Electrophilicity_index', 'Chi4n'
]

# 获取最后一列的列名，假设它是目标列
target_column = matched_ligands_df.columns[-1]

# 设置全局的字体为 Times New Roman
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']

# 绘制每一列与最后一列的散点图
for column in columns_to_plot:
    plt.figure(figsize=(9, 8))  # 可以根据需要调整图的大小
    sns.scatterplot(data=matched_ligands_df, x=column, y=target_column, color='black')
    
    # 设置标题和轴标签，字体大小为28
    plt.xlabel(column, fontsize=28, fontweight='bold')
    
    # 设置纵坐标标签为 logK₁，K 为斜体，1 为下标，字体仍为 Times New Roman
    plt.ylabel(r'log$K_1$', fontsize=28, fontweight='bold')
    
    # 设置坐标轴刻度标签的字体大小和加粗
    plt.tick_params(axis='both', which='major', labelsize=28, width=2)  # 增大字体和加粗坐标轴刻度
    
    # 保存图像为文件，文件名为 `column_target_column.png`
    plt.savefig(f"{column}_{target_column}_scatter_plot.png", dpi=300, bbox_inches='tight')
    
    # 显示图形
    plt.show()

    print(f"图像已保存为 {column}_{target_column}_scatter_plot.png")

