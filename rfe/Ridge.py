import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
        
# Read the data
data = pd.read_csv("train_kfold.csv")

# Define different subsets of columns
datasets = {
"data1":data[['charge','Chi4n','Kappa2','Kappa3','PEOE_VSA12','PEOE_VSA6','PEOE_VSA8','SMR_VSA5','SlogP_VSA4','VSA_EState2','FractionCSP3','NumHDonors','fr_Al_OH_noTert','fr_N_O','fr_alkyl_halide','fr_amide','fr_benzene','fr_phenol_noOrthoHbond','Nucleophilicity_index','logK','kfold']],
"data2":data[['Ionic radii/A','Chi3n','Kappa2','Kappa3','PEOE_VSA12','SlogP_VSA5','SlogP_VSA6','EState_VSA8','VSA_EState1','FractionCSP3','NumHDonors','fr_Al_OH_noTert','fr_COO2','fr_N_O','fr_benzene','fr_ketone_Topliss','fr_phenol_noOrthoHbond','fr_phos_acid','HOMO(N-1)','logK','kfold']],
"data3":data[['charge','MinPartialCharge','BCUT2D_LOGPLOW','BCUT2D_MRLOW','Chi2v','Kappa2','SMR_VSA5','SMR_VSA7','SlogP_VSA4','SlogP_VSA8','EState_VSA4','EState_VSA8','VSA_EState1','VSA_EState2','fr_alkyl_halide','fr_bicyclic','fr_nitrile','fr_phenol_noOrthoHbond','Nucleophilicity.1','logK','kfold']],
"data4":data[['Ionic radii/A','qed','Chi4n','PEOE_VSA12','SlogP_VSA1','SlogP_VSA8','EState_VSA8','FractionCSP3','NHOHCount','NumHDonors','fr_Al_OH_noTert','fr_N_O','fr_bicyclic','fr_phos_acid','q(N+1).2','HOMO(N)','HOMO(N-1)','Electrophilicity_index','Nucleophilicity_index','logK','kfold']],
"data5":data[['Ionic radii/A','qed','PEOE_VSA8','SMR_VSA7','SlogP_VSA6','EState_VSA8','VSA_EState1','VSA_EState2','VSA_EState9','FractionCSP3','NHOHCount','fr_phenol_noOrthoHbond','CDD','s+','s+/s-','s-/s+.1','s-/s+.2','HOMO(N)','Nucleophilicity_index','logK','kfold']]
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
        model = Ridge()
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
results_df.to_csv('Ridge_cross_validation_results.csv', index=False)











