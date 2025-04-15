import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import BayesianRidge
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler
   
# Read the data
data = pd.read_csv("train_kfold.csv")

# Define different subsets of columns
datasets = {
"data1":data[['charge','Chi2v','Chi3v','Chi4v','Kappa2','Kappa3','PEOE_VSA12','PEOE_VSA14','PEOE_VSA8','SMR_VSA5','SlogP_VSA4','VSA_EState1','VSA_EState2','FractionCSP3','fr_Al_OH_noTert','fr_N_O','fr_benzene','fr_halogen','fr_phenol_noOrthoHbond','HOMO(N)','logK','kfold']],
"data2":data[['charge','qed','AvgIpc','PEOE_VSA2','SMR_VSA3','SlogP_VSA1','SlogP_VSA4','SlogP_VSA8','EState_VSA8','VSA_EState1','FractionCSP3','NumHDonors','fr_Al_OH_noTert','fr_bicyclic','fr_phenol_noOrthoHbond','fr_phos_acid','Nucleophilicity','s+','Nucleophilicity.1','Softness','logK','kfold']],
"data3":data[['charge','MinPartialCharge','BCUT2D_MRLOW','Chi4v','Kappa2','Kappa3','SMR_VSA1','SMR_VSA3','SMR_VSA5','SlogP_VSA8','EState_VSA8','VSA_EState1','VSA_EState2','FractionCSP3','NumHDonors','fr_Al_OH','fr_bicyclic','fr_phenol_noOrthoHbond','fr_phos_acid','Nucleophilicity.2','logK','kfold']],
"data4":data[['charge','BCUT2D_MRLOW','Chi4n','Chi4v','Kappa2','PEOE_VSA8','SlogP_VSA2','SlogP_VSA5','EState_VSA8','FractionCSP3','NumHDonors','fr_Al_OH','fr_N_O','fr_alkyl_halide','fr_ether','fr_ketone_Topliss','fr_phenol_noOrthoHbond','fr_phos_acid','HOMO(N-1)','Electrophilicity_index','logK','kfold']],
"data5":data[['charge','BCUT2D_LOGPLOW','Chi2v','PEOE_VSA8','SMR_VSA3','SlogP_VSA4','SlogP_VSA8','EState_VSA10','EState_VSA8','VSA_EState1','VSA_EState2','VSA_EState9','FractionCSP3','fr_C_O','fr_bicyclic','fr_halogen','fr_phenol_noOrthoHbond','Mulliken_electronegativity','Chemical_potential','Nucleophilicity_index','logK','kfold']]
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













