import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from get_data import *


def format_data_input():
    print('--------------------------------CHOOSE A FILE-------------------------------------')
    global input_abbrev
    global input_value
    input_abbrev = input('Please Enter Crypto Abbreviation: >>> ')
    input_value = input('Please Enter a number in days: >>> ')
    input_abbrev = str(input_abbrev.upper())
    input_value = str(input_value)
     # # Pulling the data we want to base our prediction on


def formatted_data():
    format_data_input()
     # # Pulling the data we want to base our prediction on
    data_frame = pd.read_csv(f'data\{input_abbrev}_1day_data_{input_value}day.csv')
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
    plt.scatter(x, y, color = "#073642")
    plt.plot(x, y_pred, color = 'orange')
    plt.title(f'{input_abbrev} Linear Regression Model')
    plt.xlabel('Time')
    plt.ylabel('Price Data in $Dollars')
    plt.xticks(())
    plt.yticks(())
    plt.show()


if __name__ == '__main__':
    linearRegression()