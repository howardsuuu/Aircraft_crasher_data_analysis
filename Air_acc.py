import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import date, timedelta, datetime

Data = pd.read_csv(r"/Users/howardsu666/Github/Data_analysis"
                   r"/Aivation Accident"
                   r"/Airplane_Crashes_and_Fatalities_Since_1908.csv")

#print(Data.isnull().sum())

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


#print(type(set(Data['Time'])))
#print(type(Data['Time']))
Data['Time'] = Data['Date'] + ' ' + Data['Time'] #joining two rows

# integrate two col 
def todate(a):
    return datetime.strptime(a, '%m/%d/%Y %H:%M')

Data['Time'] = Data['Time'].apply(todate)


#print('Date ranges from ' + str(Data.Time.min()) + ' to ' + str(Data.Time.max()))
#print(Data['Time'])
Data.Operator = Data.Operator.str.upper()



# Visual the data: Total accidents 
# dt is to tell the series to use date data type
# [['Date"]]  makes it change from series to dataframe
temporary_data = Data.groupby(Data.Time.dt.year)[['Date']].count()
print(temporary_data)# data frame

# replace name Date into Count in the dataframe
temporary_data = temporary_data.rename(columns = {"Date": "Count"})
plt.style.use('ggplot')
plt.figure(figsize= (11,5))# define a window for barplot
# Need to put index, showing the true year instead of from 0
plt.plot(temporary_data.index, 'Count', data = temporary_data, color = 'red', \
    marker = '.', linewidth = 1.)
plt.xlabel('Year', fontsize = 12)
plt.ylabel('Count', fontsize = 12)
plt.title('Accidents frequency by Years', loc = 'Center', fontsize = 14)
plt.show()



import matplotlib.pylab as pl
import matplotlib.gridspec as gridspec

gG = gridspec.GridSpec(2,2)

pl.figure(figsize= (15,10))
plt.style.use('seaborn-muted')

# count by month
ax = pl.subplot(gG[0, :]) # both row/col are 0
plt.bar(
    Data.groupby(Data.Time.dt.month)[['Date']]
    .count().index, 'Date', data=Data.groupby(Data.Time.dt.month)[['Date']]
    .count(), color='lightskyblue', linewidth=2
)
plt.xticks(Data.groupby(Data.Time.dt.month)[['Date']].count().index, ['Jan', \
     'Feb', 'Mar', 'Apr','May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.xlabel('Month', fontsize=10)
plt.ylabel('Count', fontsize=10)
plt.title('Count of accidents by Month', loc='Center', fontsize=14)

# counts by week
ax = pl.subplot(gG[1, 0])
sns.barplot(Data.groupby(Data.Time.dt.weekday)[['Date']].count().index, 'Date',  \
    data=Data.groupby(Data.Time.dt.weekday) \
        [['Date']].count(), color='lightskyblue', linewidth=2)
plt.xticks(Data.groupby(Data.Time.dt.weekday)[['Date']].count().index, ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
plt.xlabel('Day of Week', fontsize=10)
plt.ylabel('Count', fontsize=10)
plt.title('Count of accidents by Day of Week', loc='Center', fontsize=14)

# counts by hour
ax = pl.subplot(gG[1, 1])
sns.barplot(Data[Data.Time.dt.hour != 0].groupby(Data.Time.dt.hour) \
    [['Date']].count().index, 'Date', data=Data[Data.Time.dt.hour != 0] \
        .groupby(Data.Time.dt.hour)[['Date']].count(),color ='lightskyblue', \
             linewidth=2)
plt.xlabel('Hour', fontsize=10)
plt.ylabel('Count', fontsize=10)
plt.title('Count of accidents by Hour', loc='Center', fontsize=14)
plt.tight_layout()# prvent different subplot stack together
plt.show()


# Compare the civil and military with visual
'''Data_2 = Data.copy()
Data_2['isMilitary'] = Data_2.Operator.str.contains('MILITARY')
Data_2['Military'] = Data_2.groupby('isMilitary')[['isMilitary']].count()
Data_2.index = ['Passenger', 'Military']

Data_3 = Data.copy()
Data_2['isMilitary'] = Data_2.Operator.str.contains('MILITARY')

Data_3 = Data['isMilitary'] == False'''
