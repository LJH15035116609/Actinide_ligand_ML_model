import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler

# 读取训练集和测试集数据
df_train = pd.read_csv('train_selected.csv')
df_test = pd.read_csv('test_selected.csv')
df_pre = pd.read_csv('pre_all_1.csv')


# 提取特征和标签
X_train = df_train.drop(columns=['logK']).values
y_train = df_train['logK'].values
X_test = df_test.drop(columns=['logK']).values
y_test = df_test['logK'].values
X_pre = df_pre.drop(columns=['logK']).values
y_pre = df_pre['logK'].values

# 训练模型
rf = GradientBoostingRegressor(random_state=0)
model = rf.fit(X_train, y_train)

# 计算训练集和测试集的预测值
predictions_train = model.predict(X_train)
predictions_test = model.predict(X_test)
predictions_pre = model.predict(X_pre)

# 计算训练集和测试集的评估指标
r2_train = r2_score(y_train, predictions_train)
rmse_train = mean_squared_error(y_train, predictions_train, squared=False)
mae_train = mean_absolute_error(y_train, predictions_train)

r2_test = r2_score(y_test, predictions_test)
rmse_test = mean_squared_error(y_test, predictions_test, squared=False)
mae_test = mean_absolute_error(y_test, predictions_test)

r2_pre = r2_score(y_pre, predictions_pre)
rmse_pre = mean_squared_error(y_pre, predictions_pre, squared=False)
mae_pre = mean_absolute_error(y_pre, predictions_pre)

#print(predictions_pre)
#print(r2_train,r2_test,r2_pre)
print(r2_pre,rmse_pre,mae_pre)

