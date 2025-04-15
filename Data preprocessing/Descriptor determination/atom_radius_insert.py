#多项式插值预测任何原子序数对应的原子半径（使用np.polyfit函数拟合一个多项式）
import numpy as np
import matplotlib.pyplot as plt

# 假设我们有一些已知的原子序数和对应的原子半径
atomic_numbers = np.array([89,90,91,92,93,94,95,96,98,99])
radii = np.array([188,179,163,156,155,159,173,174,186,186])

# 使用numpy的polyfit函数拟合一个多项式
degree = 3 # 这是多项式的阶数，可以根据需要调整
coefficients = np.polyfit(atomic_numbers, radii, degree)

# 创建一个多项式函数
polynomial = np.poly1d(coefficients)

# 使用这个函数预测其他原子的半径
predicted_radii = polynomial(100)

# 绘制结果
plt.scatter(atomic_numbers, radii, color='blue') # 绘制原始数据点
plt.plot(atomic_numbers, predicted_radii, color='red') # 绘制拟合的曲线
plt.show()

