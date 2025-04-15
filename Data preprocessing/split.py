import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# 读取数据集，划分并保存训练集，测试集
data = pd.read_csv("data.csv")
y = data.logK
features = data.columns[:-1]  # 选择除了最后一列之外的所有列作为特征
X = data[features].values
train, test= train_test_split(data,test_size=0.2, random_state=42)
train.to_csv('train.csv', index=False)
test.to_csv('test.csv', index=False)

