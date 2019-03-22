#!/usr/local/bin/python3.6
# _*_ coding:UTF-8 _*_
import numpy as np
import os
import pandas as pd
import hashlib

HOUSING_PATH = os.path.join("datasets", "housing")


# define a function to load the dataset
def load_housing_data(housing_path=HOUSING_PATH):
    cvs_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(cvs_path)


housing = load_housing_data()


def test_set_check(identifier, test_ratio, hash=hashlib.md5):
    return bytearray(hash(np.int64(identifier)).digest())[-1] < 256 * test_ratio


def split_train_test_by_id(data, test_ratio, id_column, hash=hashlib.md5):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio, hash))
    return data.loc[~in_test_set], data.loc[in_test_set]


housing_with_id = housing.reset_index()   # adds an `index` column
train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "index")

print(test_set.head())


