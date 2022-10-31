import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from get_data import *



def formatted_data():
     # # Pulling the data we want to base our prediction on
    data_frame = pd.read_csv('data\ETH_1day_data_1800day.csv')

    # # Extracting the notable columns from the data frame
    time_frame = data_frame.open_time
    pd_cp = data_frame.close

    # # Converting those data columns into numpy arrays in order to be use by sklearn, 
    # and making the variable coordinates global as to be accesssed by the following funtion
    global x, y
    x = time_frame.to_numpy()
    y = pd_cp.to_numpy()


    # # Reshaping the 1D array into 2D arrays per the SKlearn algorithm instructions
    x = x.reshape(-1,1)
    y = y.reshape(-1,1)



def linearRegression():
    getData()
    formatted_data()

    regressor = LinearRegression()
    regressor.fit(x, y)

    # Plotting the data using matplotlib
    y_pred = regressor.predict(x)
    plt.scatter(x, y, color = 'black')
    plt.plot(x, y_pred, color = 'orange')
    plt.title('BTC Linear Regression Model')
    plt.xlabel('Time')
    plt.ylabel('Price Data in $Dollars')
    plt.xticks(())
    plt.yticks(())
    plt.show()


if __name__ == '__main__':
    linearRegression()