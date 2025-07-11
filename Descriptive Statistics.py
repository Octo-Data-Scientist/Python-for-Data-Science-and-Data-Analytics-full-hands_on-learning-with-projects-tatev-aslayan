import pandas as pd
import numpy as np
from scipy import stats


data = [100, 20, 5, 20, 45, -100, 46]
mean_ = np.mean(data)
print("Mean of array:", mean_)

median_ = np.median(data)
print("Median of array:", median_)

mode_ = stats.mode(data)
print("Mode of array:", mode_)

variance_ = np.var(data)
print("Variance of array:", variance_)

std_ = np.std(data)
print("Standard Deviation of array:", std_)

data_csv = pd.read_csv("./Python-For-Data-Science-main/Data/percent_bachelors_degrees_women_usa.csv")
print(data_csv.describe())
print(data_csv)