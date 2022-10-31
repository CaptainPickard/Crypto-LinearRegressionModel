import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression


data_frame = pd.read_csv('data\ADA_1day_data_1800day.csv')

time_frame = data_frame.open_time
pd_cp = data_frame.close

x = time_frame.to_numpy()
y = pd_cp.to_numpy()

x = x.reshape(-1,1)
y = y.reshape(-1,1)

regressor = LinearRegression()
regressor.fit(x, y)

y_pred = regressor.predict(x)

plt.scatter(x, y, color = 'blue')
plt.plot(x, y_pred, color = 'black')
plt.title('BTC Linear Regression Model')
plt.xlabel('Time')
plt.ylabel('Price Data in $Dollars')
plt.xticks(())
plt.yticks(())
plt.show()


