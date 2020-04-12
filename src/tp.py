# coding=utf-8
from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    print "===========     20161122    =========="
    # 20150508  327
    # 20150821  401
    # 20161122  704
    # [-120 -6]
    index = 704
    from_index = index - 60
    to_index = index - 6
    dim = to_index - from_index

    # 读取数据并查看数据的前五行,sheetname=n，其中n表示excel中的工作表的索引（即第n+1个工作表）
    df_pi = pd.read_csv('D:\\temp\\history_A_stock_k_data_000936.csv')
    df_pm = pd.read_csv('D:\\temp\\history_A_stock_k_data_399001.csv')

    # 计算x,y的平均值
    pi_close = df_pi['close']
    pm_close = df_pm['close']

    x = []
    y = []
    for i in range(from_index, to_index + 10):
        y.append((pi_close[i] - pi_close[i-1])/pi_close[i-1])

    for i in range(from_index, to_index + 10):
        x.append((pm_close[i] - pm_close[i-1])/pm_close[i-1])

    # 画出x与y的散点图
    plt.scatter(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('the linear regression')
    # 线性回归拟合
    x_m = np.mean(x)
    y_m = np.mean(y)
    x1 = (x - x_m)
    y1 = y - y_m
    x2 = sum((x - x_m) ** 2)
    xy = sum(x1 * y1)

    # 回归参数的最小二乘估计
    beta1 = xy / x2
    beta0 = y_m - beta1 * x_m
    # 输出线性回归方程
    print '线性回归方程: ', 'y=', beta0, '+', beta1, '*x'
    # 画出回归方程的函数图
    a = np.linspace(min(x), max(x), 1000)  # b表示在(1000,5000)上生成1000个a值
    b = [beta0 + beta1 * i for i in a]
    plt.plot(a, b, 'r')

    # 方差
    e = []
    for i in range(from_index, to_index):
        e.append((y[i-from_index] - (beta0 - beta1 * x[i-from_index])) ** 2)
    sigma2 = sum(e) / (dim)
    # 标准差
    sigma = np.sqrt(sigma2)
    # 求t值
    t = beta1 * np.sqrt(x2) / sigma
    print 'T值=', t
    # 已知临界值求p值
    p = stats.t.sf(t, dim)
    print 'P值=', p

    # 输出检验结果
    if p < 0.05:
        print ('the linear regression between x and y is significant')
    else:
        print('the linear regression between x and y is not significant')

    # ARI
    ari = []
    print "===========     ARI    =========="
    print "i", "ARI", "CARI"
    for i in range(to_index, to_index + 10):
        ari_i = (y[i-from_index] - (beta0 - beta1 * x[i-from_index]))
        ari.append(ari_i)
        print i-to_index, ari_i, sum(ari)

    plt.show()