import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler

# 读取数据集
data = pd.read_csv("train_kfold.csv")

# 提取指定列
selected_columns = ['Pka', 'Ionic strength', 'HOMO_metal', 'BCUT2D_MWLOW', 'BCUT2D_MRLOW', 'Chi1n', 'Chi4n', 'Chi4v', 'Kappa3', 'SMR_VSA1', 'VSA_EState2', 'NumHDonors', 's+', 'VIP', 'Electrophilicity_index','logK','kfold']

data = data[selected_columns]

# 获取特征和标签
features = data.columns[:-2]
target = 'logK'

# 存储所有折的R²分数和估计器数量
all_r2_scores = []

# 定义学习率列表
random_state = np.arange(1,6,1)

# 循环进行交叉验证
for test_value in range(5):
    # 将第 kfold 列值为 test_value 的数据作为测试集，其他列的数据作为训练集
    test_set = data[data.kfold == test_value]
    train_set = data[data.kfold != test_value]

    # 提取训练集和测试集的特征和标签
    X_train, y_train = train_set[features], train_set[target]
    X_test, y_test = test_set[features], test_set[target]

    # 标准化训练集
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_train_scaled = pd.DataFrame(X_train_scaled, columns=X_train.columns)

    # 使用同一标准化器转化测试集
    X_test_scaled = scaler.transform(X_test)
    X_test_scaled = pd.DataFrame(X_test_scaled, columns=X_test.columns)

    # Initialize lists to store R2 scores for this fold
    r2_scores = []

    for rate in random_state:
        gb = GradientBoostingRegressor(learning_rate=rate)
        model = gb.fit(X_train_scaled, y_train)
    
        # 计算测试集的预测值
        predictions_test = model.predict(X_test_scaled)

        # 计算测试集的R²分数
        r2_test = r2_score(y_test, predictions_test)
    
        # Append R2 score to fold-specific list
        r2_scores.append(r2_test)

    # Append fold-specific R2 scores to list of all scores
    all_r2_scores.append(r2_scores)

    # 将all_r2_scores列表转换为DataFrame
    df_all_r2_scores = pd.DataFrame(all_r2_scores)

    # 将DataFrame保存为CSV文件
    df_all_r2_scores.to_csv('all_r2_scores.csv', index=False)

# 计算平均R²分数
avg_r2_scores = [sum(scores) / len(scores) for scores in zip(*all_r2_scores)]

df_avg_r2_scores = pd.DataFrame(avg_r2_scores)

df_avg_r2_scores.to_csv('LearningRate_avg_r2_scores.csv', index=False)

# 绘制R²分数与学习率的图表
plt.plot(random_state, avg_r2_scores)
plt.xlabel('Learning Rate')
plt.ylabel('Average R2 Score')
plt.title('Gradient Boosting Average R2 Score vs. Learning Rate')
plt.savefig('GradientBoostingRegressor_r2_Learning Rate.png', bbox_inches='tight')  # 保存图像并且调整边界
plt.show()