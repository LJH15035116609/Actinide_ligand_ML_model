import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import AdaBoostRegressor, RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler

# Read the data
data = pd.read_csv("train_kfold.csv")

# Define different subsets of columns
datasets = {
"data1": data[ ['hydration energy/kcalmol-1', 'HOMO_metal', 'FpDensityMorgan1', 'FpDensityMorgan3', 'BCUT2D_MWHI', 'BCUT2D_CHGLO', 'BalabanJ', 'Chi2v', 'Chi3v', 'HallKierAlpha', 'PEOE_VSA2', 'TPSA', 'EState_VSA1', 'VSA_EState2', 'VSA_EState8', 'NHOHCount', 's+', 's-/s+', 'HOMO(N-1)','logK','kfold']],
"data2": data[ ['Ionic strength', 'HOMO_metal', 'FpDensityMorgan1', 'FpDensityMorgan2', 'FpDensityMorgan3', 'BCUT2D_MWHI', 'BalabanJ', 'HallKierAlpha', 'PEOE_VSA2', 'SMR_VSA1', 'SlogP_VSA2', 'TPSA', 'EState_VSA1', 'VSA_EState2', 'VSA_EState5', 'NHOHCount', 's+', 's-/s+', 'HOMO(N-1)','logK','kfold']],
"data3": data[ ['Ionic radii/A', 'hydration energy/kcalmol-1', 'Pka', 'FpDensityMorgan1', 'FpDensityMorgan2', 'FpDensityMorgan3', 'BCUT2D_MWHI', 'Chi2v', 'Chi4v', 'HallKierAlpha', 'PEOE_VSA14', 'PEOE_VSA2', 'SMR_VSA1', 'EState_VSA4', 'VSA_EState2', 'VSA_EState9', 'NOCount', 's-/s+.1', 'HOMO(N-1)','logK','kfold']],
"data4": data[ ['charge', 'hydration energy/kcalmol-1', 'FpDensityMorgan1', 'Chi2v', 'HallKierAlpha', 'Kappa1', 'PEOE_VSA14', 'PEOE_VSA2', 'SlogP_VSA2', 'TPSA', 'EState_VSA1', 'VSA_EState2', 'VSA_EState3', 'VSA_EState9', 'NHOHCount', 'NumHDonors', 's-/s+', 'q(N-1).2', 'HOMO(N-1)','logK','kfold']],
"data5": data[ ['charge', 'Ionic radii/A', 'Ionic strength', 'First IE_metal  (kJ/mol)', 'HOMO_metal', 'FpDensityMorgan1', 'BCUT2D_MWHI', 'BCUT2D_CHGHI', 'Chi2v', 'Kappa1', 'TPSA', 'EState_VSA1', 'VSA_EState2', 'NHOHCount', 'NumHDonors', 'NumRotatableBonds', 'q(N-1).2', 'HOMO(N-1)', 'Softness','logK','kfold']]
}

# 提取特征和标签
target = 'logK'

# 创建空列表，用于存储每折的结果
results = []

# 交叉验证循环
for test_value in range(5):
    for dataset_name, dataset in datasets.items():
        # 将第 kfold 列值为 test_value 的数据作为测试集，其他列的数据作为训练集
        test_set = dataset[dataset.kfold == test_value]
        train_set = dataset[dataset.kfold != test_value]

        # 提取训练集和测试集的特征和标签
        features = dataset.columns[:-2]
        X_train, y_train = train_set[features], train_set[target]
        X_test, y_test = test_set[features], test_set[target]

        # 初始化标准化器
        scaler = StandardScaler()

        # 使用训练集拟合标准化器并对训练集和测试集进行转换
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        # 创建AdaBoostRegressor，使用RandomForestRegressor作为基础估计器
        model = AdaBoostRegressor(estimator=RandomForestRegressor)
        model.fit(X_train_scaled, y_train)

        # 预测
        y_pred = model.predict(X_test_scaled)

        # 计算评估指标
        r2 = r2_score(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)

        # 将每折的结果存储到字典中
        fold_result = {
            'Dataset': dataset_name,
            'Fold': test_value + 1,
            'R^2': r2,
            'Mean Squared Error': mse,
            'Mean Absolute Error': mae
        }
        
        # 添加到结果列表
        results.append(fold_result)

# 将结果列表转换为DataFrame
results_df = pd.DataFrame(results)

# 保存结果到CSV文件
results_df.to_csv('AdaBoostRegressor_with_RandomForestRegressor_cross_validation_results.csv', index=False)












