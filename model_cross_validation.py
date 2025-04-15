import pandas as pd
from sklearn.ensemble import AdaBoostRegressor, BaggingRegressor, GradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import BayesianRidge, ElasticNet, Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.kernel_ridge import KernelRidge
from sklearn.cross_decomposition import PLSRegression
from sklearn.svm import SVR
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler

# 读取数据集
data = pd.read_csv("train_kfold.csv")
target = 'logK'

# 定义模型列表
models = [
    SVR(kernel='linear'),
    SVR(kernel='poly'),
    SVR(kernel='rbf'),
    SVR(kernel='sigmoid'),
    KNeighborsRegressor(),
    KernelRidge(kernel='laplacian'),
    KernelRidge(kernel='poly'),
    KernelRidge(kernel='rbf'),
    KernelRidge(kernel='sigmoid'),
    PLSRegression(n_components=1),
    Ridge(),
    ElasticNet(),
    BayesianRidge(),
    DecisionTreeRegressor(),
    RandomForestRegressor(),
    AdaBoostRegressor(),
    AdaBoostRegressor(base_estimator=RandomForestRegressor()),
    BaggingRegressor(base_estimator=RandomForestRegressor()),
    GradientBoostingRegressor()
]

# 创建一个空DataFrame来存储结果
results = pd.DataFrame(columns=['Model', 'Mean_CV_Score'])

# 循环遍历每个模型
for model in models:
    model_results = []
    for test_value in range(5):
        # 将第 kfold 列值为 test_value 的数据作为测试集，其他列的数据作为训练集
        test_set = data[data.kfold == test_value]
        train_set = data[data.kfold != test_value]

        # 提取训练集和测试集的特征和标签
        features = data.columns[:-2]
        X_train, y_train = train_set[features], train_set[target]
        X_test, y_test = test_set[features], test_set[target]

        # 初始化标准化器
        scaler = StandardScaler()

        # 使用训练集拟合标准化器并对训练集和测试集进行转换
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        # 拟合模型
        model.fit(X_train_scaled, y_train)

        # 预测
        y_pred = model.predict(X_test_scaled)

        # 计算评估指标
        r2 = r2_score(y_test, y_pred)
        model_results.append(r2)

    # 将模型的平均评估指标添加到结果DataFrame中
    model_name = model.__class__.__name__
    mean_score = sum(model_results) / len(model_results)
    results = results.append({'Model': model_name, 'Mean_CV_Score': mean_score}, ignore_index=True)

# 将结果保存到CSV文件
results.to_csv('model_cross_validation_scores.csv', index=False)
print("Results saved to 'model_cross_validation_scores.csv'.")
