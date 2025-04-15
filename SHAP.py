import pandas as pd
import shap
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingRegressor
from matplotlib import rcParams

# 设置字体和字号
rcParams['font.family'] = 'Times New Roman'
rcParams['font.size'] = 29

# 加载训练集和测试集数据
train_data = pd.read_csv("train_selected.csv")
test_data = pd.read_csv("test_selected.csv")

# 提取特征和标签
X_train = train_data.iloc[:, :-1]
y_train = train_data.iloc[:, -1]

X_test = test_data.iloc[:, :-1]

# 训练模型
model = GradientBoostingRegressor(random_state=0)
model.fit(X_train, y_train)

# 使用 SHAP 解释器计算 SHAP 值
explainer = shap.Explainer(model, X_train)
shap_values = explainer.shap_values(X_test)

# 绘制 SHAP summary plot
summary_plot = shap.summary_plot(shap_values, X_test)

# 保存 SHAP 值到文件
shap_df = pd.DataFrame(shap_values, columns=X_test.columns)
shap_df.to_csv("shap_values.csv", index=False)

# 保存 SHAP summary plot 到文件
plt.savefig("SHAP summary plot.png")
plt.close()

# 绘制 bar plot
summary_bar_plot = shap.summary_plot(shap_values, X_test, plot_type="bar", color='steelblue')
plt.savefig("bar plot.png")
plt.close()



