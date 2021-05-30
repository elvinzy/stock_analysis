# -*- coding: utf-8 -*-
"""
Created on Sun May 30 10:23:41 2021

@author: echua
"""
# This code is used to analyze the stock ticker JNJ

# Import relevant package
import pandas as pd
import matplotlib.pyplot as plt

# Read historical data
directory = r"C:\Users\echua\Documents\Python\stock_analysis\JNJ.csv"
raw_data = pd.read_csv(directory)
raw_data['Date'] = pd.to_datetime(raw_data['Date'])

stock_ticker = directory.split('\\')[-1].split('.')[0]

# Add new columns for 20 days and 100 days MA
raw_data['20 Days MA'] = raw_data['Adj Close'].rolling(window=20).mean()
raw_data['100 Days MA'] = raw_data['Adj Close'].rolling(window=100).mean()

# Add info for today's data
today_date = raw_data.iloc[-1,:]['Date'].strftime('%Y-%m-%d')
today_open_price = round(raw_data.iloc[-1,:]['Open'],2)
today_close_price = round(raw_data.iloc[-1,:]['Adj Close'],2)
today_highest_price = round(raw_data.iloc[-1,:]['High'],2)
today_lowest_price = round(raw_data.iloc[-1,:]['Low'],2)
today_volume = int(raw_data.iloc[-1,:]['Volume'])

# Fundamental Calculation
high_52_weeks = round(raw_data.iloc[-254:,:]['Adj Close'].max(),2)
low_52_weeks = round(raw_data.iloc[-254:,:]['Adj Close'].min(),2)
avg_vol_52_weeks = int(raw_data.iloc[-254:,:]['Volume'].mean())

# User input start_date and end_date
start_date = input('Please insert the start date (YYYY-MM-DD): ')
end_date = input('Please insert the end date (YYYY-MM-DD): ')

after_start_date = raw_data['Date'] >= start_date
before_end_date = raw_data['Date'] <= end_date
between_two_dates = after_start_date & before_end_date
filtered_dates = raw_data.loc[between_two_dates]
filtered_dates.set_index('Date',inplace=True)

# Plot 'Adj Close' chart
print('')
print('System is generating ticker plot......')
filtered_dates['Adj Close'].plot()
filtered_dates['20 Days MA'].plot(linestyle='--', linewidth=1.0)
filtered_dates['100 Days MA'].plot(linestyle='--', linewidth=1.0)

# Configure plot
plt.xticks(rotation=90)
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.title('Stock Price for ' + stock_ticker +' between ' + str(start_date) + ' and ' + str(end_date),
          fontsize=10,
          fontweight='bold')
plt.legend(loc=4, fontsize=8)

plt.show()

# Print analysis info
print('')
print("===== Today's (" + today_date + ") " + stock_ticker + " Summary =====")
print('')
print('Open Price: $' + str(today_open_price))
print('Close Price: $' + str(today_close_price))
print('Daily Highest Price: $' + str(today_highest_price))
print('Daily Lowest Price: $' + str(today_lowest_price))
print('Daily Volume: ' + str(today_volume))
print('')
print('===== ' + stock_ticker + ' Past 52 Weeks Summary =====')
print('')
print('52 weeks highest price: $' + str(high_52_weeks))
print('52 weeks lowest price: $' + str(low_52_weeks))
print('52 weeks average volume: ' + str(avg_vol_52_weeks))