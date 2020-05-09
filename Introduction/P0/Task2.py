"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
from datetime import datetime
timeSpentOnPhone = {}
for record in calls:
    date = datetime.strptime(record[2], "%d-%m-%Y %H:%M:%S")
    if date.year == 2016 and date.month == 9:
        if record[0] not in timeSpentOnPhone:
            timeSpentOnPhone[record[0]] = int(record[3])
        else:
            timeSpentOnPhone[record[0]] += int(record[3])
        if record[1] not in timeSpentOnPhone:
            timeSpentOnPhone[record[1]] = int(record[3])
        else: 
            timeSpentOnPhone[record[1]] += int(record[3])
maxPhoneNum = max(timeSpentOnPhone, key=timeSpentOnPhone.get)
print("%s spent the longest time, %s seconds, on the phone during September 2016." %(maxPhoneNum, timeSpentOnPhone[maxPhoneNum]))