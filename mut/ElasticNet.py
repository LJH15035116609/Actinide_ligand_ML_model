import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import ElasticNet
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler

# Read the data
data = pd.read_csv("train_kfold.csv")

# Define different subsets of columns
datasets = {
"data1": data[ ['HallKierAlpha', 'SMR_VSA1', 'TPSA', 'Chi0v', 'Softness', 's+', 'BCUT2D_CHGLO', 'q(N).1', 'MolWt', 'Chi0n', 'ExactMolWt', 'HOMO(N-1)', 'q(N-1).2', 'q(N).2', 'PEOE_VSA1', 'E(N+1)', 'EN', 'Chi0', 'NumValenceElectrons', 'Kappa1','logK','kfold']],
"data2": data[ ['HallKierAlpha', 'SMR_VSA1', 'TPSA', 'HOMO(N-1)', 'Chi0v', 'PEOE_VSA1', 'q(N).2', 'Kappa2', 'Kappa1', 'q(N).1', 'BCUT2D_CHGLO', 'Chi0n', 'Chi1n', 'HeavyAtomMolWt', 'MolWt', 's+', 'ExactMolWt', 'Chi2n', 'BCUT2D_LOGPLOW', 'VSA_EState2','logK','kfold']],
"data3": data[ ['HallKierAlpha', 'SMR_VSA1', 'Chi0v', 'Kappa1', 'q(N).1', 'BCUT2D_CHGLO', 'TPSA', 'HOMO(N-1)', 'BCUT2D_LOGPLOW', 'HeavyAtomMolWt', 'MolWt', 'VIP', 's+', 'Chi0n', 'q(N).2', 'ExactMolWt', 'Kappa2', 'PEOE_VSA1', 'q(N-1).2', 'Chi1','logK','kfold']],
"data4": data[ ['HallKierAlpha', 'SMR_VSA1', 'TPSA', 'PEOE_VSA1', 'HOMO(N-1)', 'q(N).2', 'FpDensityMorgan1', 'Chi0v', 'VIP', 'Kappa1', 'Chi0n', 'f-.2', 'Kappa2', 'f+.2', 'q(N).1', 'SlogP_VSA2', 'Electrophilicity_index', 's+', 'MolWt', 'HeavyAtomMolWt','logK','kfold']],
"data5": data[ ['HallKierAlpha', 'TPSA', 'SMR_VSA1', 'Kappa2', 'PEOE_VSA1', 'Chi0v', 'BCUT2D_CHGLO', 'HOMO(N-1)', 'q(N-1).2', 'HeavyAtomMolWt', 'SlogP_VSA2', 'q(N).1', 'q(N).2', 'Kappa1', 's+', 'MolWt', 'Chi0n', 'Chi2v', 'ExactMolWt', 'VIP','logK','kfold']]
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

        model = ElasticNet()  # 使用ElasticNet
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
results_df.to_csv('ElasticNet_cross_validation_results.csv', index=False)













