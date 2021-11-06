import csv
import math
import json
file = open('Prescriber_Data.csv');
csvreader = csv.reader(file)
header = []
header = next(csvreader)
rows = []
for row in csvreader:
        rows.append(row)

stateAndSums = []

for i in range(0, len(rows)):
    currNewSum = 0;
    currTotalSum = 0;
    currN = 5;
    currT = 11;
    while currN < 11:
        currNewSum+=int(rows[i][currN])
        currTotalSum+=int(rows[i][currT])
        currN = currN + 1
        currT = currT + 1
    rows[i].append(str(currNewSum))
    rows[i].append(str(currTotalSum))

rows.sort(key = lambda x:x[3])


stateNewSum = int(rows[0][17]);
stateTotalSum = int(rows[0][18]);
for i in range(1,len(rows)):
    if(i == len(rows) - 1):
        stateNewSum+=int(rows[i][17])
        stateTotalSum+=int(rows[i][18])
        stateAndSums.append([rows[i][3],stateNewSum,stateTotalSum])
    elif(rows[i][3] != rows[i-1][3]):
        stateAndSums.append([rows[i-1][3], stateNewSum, stateTotalSum])
        stateNewSum = int(rows[i][17])
        stateTotalSum = int(rows[i][18])
    else:
        stateNewSum+=int(rows[i][17])
        stateTotalSum+=int(rows[i][18])

emergingMarkets = []
slowingMarkets = []
for i in range(0, len(stateAndSums)):
    ratio = 1.0*stateAndSums[i][1]/stateAndSums[i][2]
    stateAndSums


print(emergingMarkets)
print(slowingMarkets)


