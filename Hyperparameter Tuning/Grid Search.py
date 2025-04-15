from sklearn.model_selection import GridSearchCV
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler
from sklearn import model_selection

# 读取数据集
data = pd.read_csv("train_kfold.csv")

# 提取指定列
selected_columns = ['Pka', 'Ionic strength', 'HOMO_metal', 'BCUT2D_MWLOW', 'BCUT2D_MRLOW', 'Chi1n', 'Chi4n', 'Chi4v', 'Kappa3', 'SMR_VSA1', 'VSA_EState2', 'NumHDonors', 's+', 'VIP', 'Electrophilicity_index','logK','kfold']
data = data[selected_columns]

# 获取特征和标签
features = data.columns[:-2]
target = 'logK'
X, y = data[features], data[target]

def create_rfolds(data, target, n_splits):
    # 创建一个新列叫做kfold，并用-1来填充
    data["kfold"] = -1

    # 随机打乱数据的行
    data = data.sample(frac=1).reset_index(drop=True)

    # 使用Sturge规则计算bin的数量
    num_bins = int(np.floor(1 + np.log2(len(data))))

    # 使用pandas的cut函数进行目标变量（target）的分箱
    data.loc[:, "bins"] = pd.cut(
        data[target], bins=num_bins, labels=False
    )

    # 初始化StratifiedKFold类
    kf = model_selection.StratifiedKFold(n_splits=n_splits)

    # 填充新的kfold列
    # 注意：我们使用的是bins而不是实际的目标变量（target）！
    for f, (t_, v_) in enumerate(kf.split(X=data, y=data.bins.values)):
        data.loc[v_, 'kfold'] = f

    # 删除bins列
    data = data.drop("bins", axis=1)

    # 返回包含folds的数据
    return data

param_grid = {
    'loss': ['ls', 'lad', 'huber', 'quantile'],
    'learning_rate': [0.1, 0.05, 0.01],
    'n_estimators': [100, 200, 300],
    'subsample': [1.0, 0.5],
    'criterion': ['friedman_mse', 'mse'],
    'min_samples_split': [2, 4, 6],
    'min_samples_leaf': [1, 2, 3],
    'max_depth': [3, 5, 7],
}

# 创建随机森林回归器
model = GradientBoostingRegressor()

# 创建 GridSearchCV 对象，传递自定义的分层K折交叉验证函数作为 cv 参数
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, scoring='r2', cv=5)

# 拟合数据
grid_search.fit(X, data[target])

# 输出最佳参数
print("Best parameters found: ", grid_search.best_params_)

# 输出最佳得分
print("Best R2 score found: ", grid_search.best_score_)

