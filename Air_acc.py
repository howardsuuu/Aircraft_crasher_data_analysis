import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import date, timedelta, datetime

Data = pd.read_csv(r"/Users/howardsu666/Github/Data_analysis"
                   r"/Aivation Accident"
                   r"/Airplane_Crashes_and_Fatalities_Since_1908.csv")

print(Data.isnull().sum())

# Cleaning
Data['Time'] = Data['Time'].replace(np.nan, '00:00') 
Data['Time'] = Data['Time'].str.replace('c: ', '')
Data['Time'] = Data['Time'].str.replace('c:', '')
Data['Time'] = Data['Time'].str.replace('c', '')
Data['Time'] = Data['Time'].str.replace('12\'20', '12:20')
Data['Time'] = Data['Time'].str.replace('18.4', '18:40')
Data['Time'] = Data['Time'].str.replace('0943', '09:43')
Data['Time'] = Data['Time'].str.replace('22\'08', '22:08')
Data['Time'] = Data['Time'].str.replace('114:20:00', '00:00')
Data['Time'] = Data['Time'].str.replace('009:43', '0943')
Data['Time'] = Data['Time'].str.replace('18:400', '18:40')
Data['Time'] = Data['Time'].str.replace('18:401', '18:41')
Data['Time'] = Data['Time'].str.replace('18:402', '18:42')
Data['Time'] = Data['Time'].str.replace('18:403', '18:43')
Data['Time'] = Data['Time'].str.replace('18:404', '18:44')
Data['Time'] = Data['Time'].str.replace('18:405', '18:45')
Data['Time'] = Data['Time'].str.replace('18:406', '18:46')
Data['Time'] = Data['Time'].str.replace('18:407', '18:47')
Data['Time'] = Data['Time'].str.replace('18:408', '18:48')
Data['Time'] = Data['Time'].str.replace('18:409', '18:49')
Data['Time'] = Data['Time'].str.replace('114:20', '00:00')



#print(set(Data['Time']))
Data['Time'] = Data['Date'] + ' ' + Data['Time'] #joining two rows

# integrate two col 
def todate(a):
    return datetime.strptime(a, '%m/%d/%Y %H:%M')

Data['Time'] = Data['Time'].apply(todate)



print('Date ranges from ' + str(Data.Time.min()) + ' to ' + str(Data.Time.max()))
print(Data['Time'])
Data.Operator = Data.Operator.str.upper()

# Visual the data
temporary_data = Data.groupby(Data.Time.dt.year)[['Date']].count()
print(temporary_data.head(5))
