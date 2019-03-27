import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
# Read csv files
dt = pd.read_csv(r"/Users/howardsu666/Github/Data_analysis"
                 r"/Aivation Accident"
                 r"/Airplane_Crashes_and_Fatalities_Since_1908.csv")
dt['Date'] = dt['Date'].map(pd.to_datetime)
#print(dt['Date'].head())

# Create a new column, weekday based on the history date
def get_weekday(dataWeekday):
    return dataWeekday.weekday()
dt['Weekday'] = dt['Date'].map(get_weekday)# can also using .apply()
#print(dt['Weekday'])

# To see the Freq of the crashing based on the weekdays
def count_row(rows):
    return len(rows)
by_weekdays = dt.groupby('Weekday').apply(count_row)# Groupby - is a DataFrame
#plt.bar(range(0,7), by_weekdays)
#plt.xticks(range(0,7), ('Mon', 'Tue', 'Wen', 'Thu', 'Fri', 'Sat', 'Sun'))
#plt.xlabel('Weekday')
#plt.ylabel('Freq')
#plt.title('Freq by Weekdays')
#plt.show()

# Create a new column, year based on the 'Date' column

dt['Year'] = dt['Date'].dt.year
plt.plot(dt['Year'], '.', ms = 0.5, alpha = .5)
plt.xlabel('Freq')
plt.ylabel('Year')
#ax = plt.gca()
#ax.invert_yaxis() Invert the y axis
plt.title('Freq by Years')
plt.show()
plt.close()
# Dot plot for

# To see which Type of Aircraft 
#print(dt['Type'].describe())
#print(dt['Type'].value_counts())

