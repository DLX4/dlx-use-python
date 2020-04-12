# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

if __name__ == '__main__':
    data = np.array([
        [0.0726, 0.52],
        [0.0976, 0.44],
        [0.0859, 0.38],
        [0.0748, 0.33],
        [0.0246, 0.31],
        [0.0255, 0.32],
        [0.0311, 0.25],
        [0.1241, 0.43],
        [0.0432, 0.58],
        [0.0699, 0.59]
    ])
    # 样本数据
    y = data[:, 0].reshape(-1, 1)
    X = data[:, 1].reshape(-1, 1)

    # 使用多少阶多项式来拟合
    poly_reg = PolynomialFeatures(degree=10, include_bias=False)
    X_poly = poly_reg.fit_transform(X)
    lin_reg = LinearRegression()
    # 拟合多项式线性回归
    lin_reg.fit(X_poly, y)
    # 多项式系数从0次到最高次
    print '多项式系数：', lin_reg.intercept_, (lin_reg.coef_[0])
    print 'y = ', lin_reg.intercept_[0],
    for i, v in enumerate(lin_reg.coef_[0]):
        print ' + ', v, ' * (X^', i+1, ')'

    # Visualising the Polynomial Regression results
    # 将x分成多段，可以使生成的曲线更平滑
    X_grid = np.arange(min(X), max(X), 0.001)
    X_grid = X_grid.reshape(len(X_grid), 1)
    plt.scatter(X, y, c="red")
    plt.plot(X_grid, lin_reg.predict(poly_reg.fit_transform(X_grid)))
    plt.title = "(polynimal regression)"
    plt.xlabel = "资产负债率（x）"
    plt.ylabel = "净资产收益率（y）"
    plt.show()
