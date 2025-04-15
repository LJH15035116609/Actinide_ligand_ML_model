import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import AdaBoostRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler

# 读取训练集和测试集数据
df_train = pd.read_csv('train_ori.csv')

# 提取指定列
selected_columns = ['Ionic radii/A', 'FpDensityMorgan1', 'BCUT2D_MWHI', 'Chi2v','Chi4v',
                    'PEOE_VSA2','SMR_VSA1','TPSA','logK']

selected_data1 = df_train[selected_columns]

# 提取特征和标签
X_train = selected_data1.drop(columns=['logK']).values
y_train = selected_data1['logK'].values

# 初始化StandardScaler对象
scaler = StandardScaler()

# 使用训练集拟合标准化器并对训练集和测试集进行转换
X_train_scaled = scaler.fit_transform(X_train)

# 将标准化后的特征数据转换为 DataFrame
scaled_df = pd.DataFrame(X_train_scaled, columns=selected_data1.columns[:-1])

# 保存DataFrame到一个文件
scaled_df.to_csv("X_train_scaled.csv", index=False)






