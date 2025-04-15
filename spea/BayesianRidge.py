import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import BayesianRidge
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler
   
# Read the data
data = pd.read_csv("train_kfold.csv")

# Define different subsets of columns
datasets = {
"data1": data[['Electrophilicity', 'Mulliken_electronegativity', 'Chemical_potential', 'fr_bicyclic', 'Electrophilicity_index', 'FpDensityMorgan2', 'PEOE_VSA13', 'fr_Al_OH_noTert', 'SlogP_VSA12', 'HOMO(N+1)', 'FpDensityMorgan3', 'NumAromaticHeterocycles', 'PEOE_VSA1', 'fr_alkyl_halide', 'Nucleophilicity', 'Pka', 'qed', 'q(N)', 'VEA', 'VIP','logK','kfold']],
"data2": data[['Nucleophilicity.1', 'HOMO(N)', 'Nucleophilicity_index', 'Nucleophilicity.2', 'SlogP_VSA12', 'Ionic strength', 'VIP', 'CDD.2', 's+/s-.1', 's+.1', 'Nucleophilicity', 'fr_phos_acid', 'CDD.1', 'fr_phenol', 'fr_phenol_noOrthoHbond', 'Hardness', 'Softness', 'fr_Al_COO', 'q(N+1).1', 'PEOE_VSA4','logK','kfold']],
"data3": data[['First IE_metal  (kJ/mol)', 'PEOE_VSA3', 'Pauling electronegativity', 'charge', 'Ionic radii/A', 'hydration energy/kcalmol-1', 'PEOE_VSA11', 'SlogP_VSA4', 'VSA_EState10', 'Atomic Number_metal ', 'Outer shell electrons_metal ', 'BCUT2D_MRHI', 'SlogP_VSA12', 'EState_VSA4', 'fr_C_S', 'HOMO(N)', 'Nucleophilicity_index', 'NumAromaticHeterocycles', 'fr_Ar_N', 'EState_VSA7','logK','kfold']],
"data4": data[['fourth IE_metal  (kJ/mol)', 'Atomic Number_metal ', 'Third IE_metal  (kJ/mol)', 'Outer shell electrons_metal ', 'Relative atomic mass', 'Melting Point_metal  (K)', 'Temperature (C)', 'First IE_metal  (kJ/mol)', 'EState_VSA6', 'NumAromaticCarbocycles', 'Electrophilicity.2', 'NumHAcceptors', 'PEOE_VSA5', 'fr_Al_OH_noTert', 'HOMO_metal', 'EState_VSA7', 'q(N-1).1', 'Kappa3', 'qed', 'fr_alkyl_halide','logK','kfold']],
"data5": data[['EState_VSA9', 'SlogP_VSA1', 'MinEStateIndex', 'q(N).1', 'NumHeteroatoms', 'q(N).2', 'MinPartialCharge', 'MaxAbsPartialCharge', 'SMR_VSA4', 'NumAromaticCarbocycles', 'q(N-1).1', 'fr_ketone', 'fr_ketone_Topliss', 'SlogP_VSA11', 'fr_alkyl_halide', 'q(N+1).2', 'fr_Ar_OH', 'q(N+1).1', 'NumHAcceptors', 'f0.2','logK','kfold']]
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

        model = BayesianRidge()  # 使用BayesianRidge
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
results_df.to_csv('BayesianRidge_cross_validation_results.csv', index=False)













