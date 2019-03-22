#!/usr/local/bin/python3.6
# _*_ coding:UTF-8 _*_
# create a test dataset
import numpy as np
import os
import pandas as pd

HOUSING_PATH = os.path.join("datasets", "housing")


# define a function to load data
def load_housing_data(housing_path=HOUSING_PATH):
    cvs_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(cvs_path)


housing = load_housing_data()     # 调用函数，加载数据


# define a function create a test dataset
def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

print(housing.info())
# train_set, test_set = split_train_test(housing, 0.2)
# print(len(train_set), "train +", len(train_set), "test")
