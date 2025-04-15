import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cross_decomposition import PLSRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler

    
# Read the data
data = pd.read_csv("train_kfold.csv")

# Define different subsets of columns
datasets = {
"data1":data[['NumValenceElectrons','Chi0','Chi0n','Chi2n','Kappa1','HeavyAtomCount','NumRotatableBonds','logK','kfold']],
"data2":data[['NumValenceElectrons','Chi0n','Kappa1','SlogP_VSA2','VSA_EState2','HeavyAtomCount','NumRotatableBonds','logK','kfold']],
"data3":data[['NumValenceElectrons','Chi0n','Kappa1','PEOE_VSA2','SlogP_VSA2','VSA_EState2','NumRotatableBonds','logK','kfold']],
"data4":data[['NumValenceElectrons','Chi0n','Kappa1','PEOE_VSA2','SlogP_VSA2','VSA_EState2','NumRotatableBonds','logK','kfold']],
"data5":data[['NumValenceElectrons','Chi0n','Chi2n','Kappa1','SlogP_VSA2','VSA_EState2','NumRotatableBonds','logK','kfold']]
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

        # Initialize the PLSRegression model with one component
        model = PLSRegression(n_components=1)
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

# Save the results to a CSV file
results_df.to_csv('PLSRegression_1_component_cross_validation_results.csv', index=False)














