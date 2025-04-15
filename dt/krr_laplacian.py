import pandas as pd
import matplotlib.pyplot as plt
from sklearn.kernel_ridge import KernelRidge
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler

    
# Read the data
data = pd.read_csv("train_kfold.csv")

# Define different subsets of columns
datasets = {
"data1": data[ ['Pka', 'Ionic strength', 'HOMO_metal', 'MinEStateIndex', 'FpDensityMorgan1', 'FpDensityMorgan3', 'BCUT2D_MRLOW', 'BalabanJ', 'Ipc', 'SMR_VSA9', 'SlogP_VSA6', 'VSA_EState2', 'q(N-1)', 'Electrophilicity', 's+', 'E(N-1)','logK','kfold']],
"data2": data[ ['hydration energy/kcalmol-1', 'Ionic strength', 'MaxPartialCharge', 'FpDensityMorgan1', 'BCUT2D_MWLOW', 'Kappa2', 'Kappa3', 'SlogP_VSA3', 'VSA_EState2', 'NumHAcceptors', 'NumHeteroatoms', 'fr_amide', 's-', 's+', 'Nucleophilicity.1', 's-.1','logK','kfold']],
"data3": data[ ['hydration energy/kcalmol-1', 'Pka', 'Temperature (C)', 'Ionic strength', 'MinEStateIndex', 'FpDensityMorgan1', 'FpDensityMorgan3', 'SMR_VSA1', 'VSA_EState2', 'VSA_EState5', 'f-', 'Electrophilicity', 's+', 'E(N-1)', 'HOMO(N-1)', 'Mulliken_electronegativity','logK','kfold']],
"data4": data[ ['Ionic radii/A', 'hydration energy/kcalmol-1', 'Ionic strength', 'MaxPartialCharge', 'FpDensityMorgan3', 'BCUT2D_MWLOW', 'BalabanJ', 'Ipc', 'Kappa2', 'Kappa3', 'PEOE_VSA1', 'SMR_VSA9', 'EState_VSA6', 'VSA_EState2', 'q(N+1).2', 'VIP','logK','kfold']],
"data5": data[ ['Ionic radii/A', 'Ionic strength', 'Relative atomic mass', 'MaxPartialCharge', 'FpDensityMorgan3', 'Kappa1', 'PEOE_VSA11', 'PEOE_VSA9', 'SMR_VSA6', 'SlogP_VSA2', 'VSA_EState1', 'VSA_EState2', 'Electrophilicity', 'Nucleophilicity', 's+', 'f0.1','logK','kfold']]
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

        model = KernelRidge(kernel='laplacian')
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
results_df.to_csv('KernelRidge_cross_validation_results.csv', index=False)












