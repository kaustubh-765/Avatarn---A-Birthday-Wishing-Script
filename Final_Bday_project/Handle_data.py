import pandas as pd
import requests
import datetime as dtime
import time
import pytz


# Define filepath
filepath_1 = 'Student_List.xlsx'
filepath_2 = 'Faculty_Employees_List.xlsx'
filepath_3 = 'NTS_Employees_List.xlsx'


url = "http://worldtimeapi.org/api/timezone/Asia/Kolkata"

response = requests.get(url)
data = response.json()

timestamp = data['unixtime']
timezone = data['timezone']

tz = pytz.timezone(timezone)
tme = dtime.datetime.fromtimestamp(timestamp, tz)

print(tme, type(tme))

current_date = (tme.strftime("%d-%m"))           
current_month = int(tme.strftime("%m"))

print(current_date, type(current_date))

# Load Excel file using Pandas
f1 = pd.ExcelFile(filepath_1)
f2 = pd.ExcelFile(filepath_2)
f3 = pd.ExcelFile(filepath_3)

# Define an empty list to store individual DataFrames
list_of_dfs = []

# Iterate through each worksheet 
for sheet in f1.sheet_names:
    
    # Parse data from each worksheet as a Pandas DataFrame
    df = f1.parse(sheet)

    # And append it to the list
    list_of_dfs.append(df)
    
for sheet in f2.sheet_names:
    
    # Not include the Master sheet
    if sheet == "Master":
        continue

    # Parse data from each worksheet as a Pandas DataFrame
    df = f2.parse(sheet)

    # And append it to the list
    list_of_dfs.append(df)

for sheet in f3.sheet_names:

    # Parse data from each worksheet as a Pandas DataFrame
    df = f3.parse(sheet)

    # And append it to the list
    list_of_dfs.append(df)


# Combine all DataFrames into one
print(list_of_dfs)

data = pd.concat(list_of_dfs, ignore_index=True)


list_date = data.loc[data['Birth_Date'] == current_date]

print(data['Birth_Date'])
#print(data['DOB'][0], type(data['DOB'][0]))

#print(type(data), data.shape)
print(type(list_date), list_date.shape)
print(list_date)

# Preview first 10 rows
#print(data.head(10))

