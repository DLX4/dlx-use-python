# coding=utf-8
from decimal import *
from sympy import *

if __name__ == '__main__':
    # 输入数据x y 单位万元
    y = map(Decimal, '11463.91 25899.89 20345.11 18621.19 6178.08 7450.71 11328.99 81077.79 24984.51 42230.85'.split())
    # y单位亿元
    y = map(lambda n: n / 10000, y)
    print 'y = ', y

    x = map(Decimal,
            '279169.98 354026.36 301854.93 297405.49 285492.5 347817.28 389815.43 875880.4 1113006.97 1203954.55'.split())
    # x单位亿元
    x = map(lambda n: n / 10000, x)
    print 'x = ', x

    # x1 = x
    x1 = x
    print 'x1 = ', x1

    # x2 = x*x
    x2 = map(lambda n: n ** 2, x)
    print 'x2 = ', x2

    # x1平方
    x1_x1 = map(lambda n: n ** 2, x1)
    print 'x1_x1 = ', x1_x1

    # x2平方
    x2_x2 = map(lambda n: n ** 2, x2)
    print 'x2_x2 = ', x2_x2

    # x1 * x2
    x1_x2 = map(lambda n, m: n * m, x1, x2)
    print 'x1_x2 = ', x1_x2

    # x1 * y
    x1_y = map(lambda n, m: n * m, x1, y)
    print 'x1_y = ', x1_y

    # x2 * y
    x2_y = map(lambda n, m: n * m, x2, y)
    print 'x2_y = ', x2_y

    # sum(y)
    sum_y = sum(y)
    print 'sum_y = ', sum_y

    # sum(x1)
    sum_x1 = sum(x1)
    print 'sum_x1 ', sum_x1

    # sum(x2)
    sum_x2 = sum(x2)
    print 'sum_x2 ', sum_x2

    # sum(x1 * y)
    sum_x1_y = sum(x1_y)
    print 'sum_x1_y ', sum_x1_y

    # sum(x1 * x1)
    sum_x1_x1 = sum(x1_x1)
    print 'sum_x1_x1 ', sum_x1_x1

    # sum(x1 * x2)
    sum_x1_x2 = sum(x1_x2)
    print 'sum_x1_x2 ', sum_x1_x2

    # sum(x2 * y)
    sum_x2_y = sum(x2_y)
    print 'sum_x2_y ', sum_x2_y

    # sum(x2 * x2)
    sum_x2_x2 = sum(x2_x2)
    print 'sum_x2_x2 ', sum_x2_x2

    # 方程1
    print sum_y, ' = ', len(y), ' * a + ', sum_x1, ' * b + ', sum_x2, ' * c'

    # 方程2
    print sum_x1_y, ' = ', sum_x1, ' * a + ', sum_x1_x1, ' * b + ', sum_x1_x2, ' * c'

    # 方程3
    print sum_x2_y, ' = ', sum_x2, ' * a + ', sum_x1_x2, ' * b + ', sum_x2_x2, ' * c'

    # 解方程
    a = Symbol('a')
    b = Symbol('b')
    c = Symbol('c')

    res = solve([len(y) * a + sum_x1 * b + sum_x2 * c - sum_y,
                 sum_x1 * a + sum_x1_x1 * b + sum_x1_x2 * c - sum_x1_y,
                 sum_x2 * a + sum_x1_x2 * b + sum_x2_x2 * c - sum_x2_y],
                [a, b, c])

    a = res[a]
    b = res[b]
    c = res[c]
    # a b c的值
    print 'a = ', a, 'b = ', b, 'c = ', c

    X = Symbol('X')

    # 求导数Y = a + b*X + c*(X**2)
    print diff(c * X ** 2 + b * X + 1 + a, X)
    # 求极值
    res_diff = solve(Eq(diff(c * X ** 2 + b * X + 1 + a, X), 0), X)
    X = res_diff[0]
    print 'X = ', X
    # Y = a + b*X + c*(X**2) 的最大值
    print 'Y = ', a + b*X + c*(X**2)

    # print solve(Eq(c * X ** 2 + b * X + 1 + a, 0), X)
    # for i, v in enumerate(x):
    #     print v
