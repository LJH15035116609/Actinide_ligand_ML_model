from sklearn.model_selection import KFold
import pandas as pd

# 读取数据集
data = pd.read_csv("train.csv")

# 根据KFold进行划分并创建kfold列
kf = KFold(n_splits=5, shuffle=True, random_state=42)
for fold, (_, test_index) in enumerate(kf.split(data)):
    data.loc[test_index, 'kfold'] = fold

# 保存包含kfold列的数据集
data.to_csv("train_kfold.csv", index=False)
