import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from regression_plot import *

# Read in the data
data_frame = pd.read_csv('data\ADA_1day_data_360day.csv')
model = sm.OLS.from_formula('open_time ~ close', data = data_frame)
results = model.fit()
print(results.params)
