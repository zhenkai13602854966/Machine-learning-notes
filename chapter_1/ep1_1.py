#!/usr/local/bin/python3.6
# _*_ coding:UTF-8 _*_
import os
import pandas as pd
import matplotlib.pyplot as plt

HOUSING_PATH = os.path.join("datasets", "housing")


# define a function to load data
def load_housing_data(housing_path=HOUSING_PATH):
    cvs_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(cvs_path)


# define a function to save figure
# def save_fig(fig_id, tight_layout=True):
    # path = os.path.join(HOUSING_PATH, "images", fig_id + ".png")
    # print("Saving figure", fig_id)
    # if tight_layout:
        # plt.tight_layout()
    # plt.savefig(path, format='png', dpi=300)


housing = load_housing_data()     # 调用函数
# print(housing)
# print(housing.head())           # 显示前五行数据
# print(housing.info())           # 快速获取数据集的简答描述
# print(housing.describe())       # 显示数值属性摘要
housing.hist(bins=50, figsize=(20, 15))
plt.savefig("images/chap1_project/attribute_histogram_plots")
plt.show()
