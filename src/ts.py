# coding=utf-8
import pandas as pd
import tushare as ts

if __name__ == '__main__':
    df = ts.get_hist_data('000936', '2015-01-01', '2018-01-01')  # 一次性获取全部日k线数据
    df.to_csv('data.csv')  # 导出数据
    df  # 查看数据