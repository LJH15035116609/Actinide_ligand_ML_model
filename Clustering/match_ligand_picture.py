import pandas as pd
import os
from PIL import Image

# 读取smiles.csv文件
csv_path = '5.csv'  # 将路径替换为实际的smiles.csv文件路径
df = pd.read_csv(csv_path)

# 配体图片文件夹路径
image_folder_path = 'ligand_images'  # 将路径替换为实际的配体图片文件夹路径

# 创建一个新的Excel文件
excel_path = '5.xlsx'  # 将路径替换为实际的输出Excel文件路径
with pd.ExcelWriter(excel_path, engine='xlsxwriter') as writer:
    # 创建一个名为 'Sheet1' 的 sheet
    writer.sheets['Sheet1'] = writer.book.add_worksheet('Sheet1')

    # 遍历每一行，获取SMILES并插入图片
    for index, row in df.iterrows():
        smiles = row['smiles']
        image_path = os.path.join(image_folder_path, f"{smiles}.png")  # 假设图片以smiles命名并以.png为扩展名

        # 检查图片文件是否存在
        if os.path.exists(image_path):
            # 插入图片到Excel
            image = Image.open(image_path)
            image.thumbnail((100, 100))  # 调整图片大小
            writer.sheets['Sheet1'].insert_image(index + 1, df.shape[1], image_path, {'x_scale': 0.5, 'y_scale': 0.5})
        else:
            print(f"Image not found for SMILES: {smiles}")



