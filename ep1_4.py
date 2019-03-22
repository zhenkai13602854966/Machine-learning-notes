#!/usr/local/bin/python3.6
# _*_ coding:UTF-8 _*_
import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt

HOUSING_PATH = os.path.join("datasets", "housing")


# define a function to load the dataset
def load_housing_data(housing_path=HOUSING_PATH):
    cvs_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(cvs_path)


housing = load_housing_data()

# Divide by 1.5 to limit the number of income categories
housing["income_cat"] = np.ceil(housing["median_income"] / 1.5)
# Label those above 5 as 5
housing["income_cat"].where(housing["income_cat"] < 5, 5.0, inplace=True)

housing["income_cat"] = pd.cut(housing["median_income"],
                               bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
                               labels=[1, 2, 3, 4, 5])
print(housing["income_cat"].value_counts())
housing["income_cat"].hist()
plt.show()
