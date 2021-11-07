import csv;
import math;

def sortArray(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if(arr[i][1] > arr[j][1]):
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp


    return arr

def parseElements(str):
    arr = []
    while(len(str) > 0):
        i = 0;
        while(i < len(str) and str[i] != ','):
            i = i + 1
        curr = str[0:i]
        if(len(arr) < 1 or len(arr) > 5):
            curr = int(curr)
        arr.append(curr)
        str = str[i+1:]


    return arr

data = open('/Users/eddiekubit/Documents/HackOHI:O2021/hackOHIO2021/Prescriber_Data.csv');

header = []
header = next(data);

rows = [];
for row in data:
    rows.append(parseElements(row));



cholecap = []
nasalclear = []
novaitch = []
zapapain = []
for i in range(0,len(rows)):
    if("Cholecap" == rows[i][4]):
        cholecap.append(rows[i])
    elif("NasalClear" in rows[i][4]):
        nasalclear.append(rows[i])
    elif("Nova-itch" in rows[i][4]):
        novaitch.append(rows[i])
    elif("Zap-a-Pain" in rows[i][4]):
        zapapain.append(rows[i])



cholecapTotalRx = []
for(row) in cholecap:
    cholecapTotalRx.append([row[0],sum(row[11:17])])
nasalclearTotalRx = []
for(row) in nasalclear:
    nasalclearTotalRx.append([row[0], sum(row[11:17])])
novaitchTotalRx = []
for(row) in novaitch:
    novaitchTotalRx.append([row[0], sum(row[11:17])])
zapapainTotalRx = []
for(row) in zapapain:
    zapapainTotalRx.append([row[0], sum(row[11:17])])

cholecapTotalRx = sortArray(cholecapTotalRx)
nasalclearTotalRx = sortArray(nasalclearTotalRx)
novaitchTotalRx = sortArray(novaitchTotalRx)
zapapainTotalRx = sortArray(zapapainTotalRx)

cc90thIndex = math.ceil(len(cholecapTotalRx) * .9)
nc90thIndex = math.ceil(len(nasalclearTotalRx) * .9)
ni90thIndex = math.ceil(len(novaitchTotalRx) * .9)
zp90thIndex = math.ceil(len(zapapainTotalRx) * .9)

cc90th = cholecapTotalRx[cc90thIndex:len(cholecapTotalRx) - 1]
nc90th = nasalclearTotalRx[nc90thIndex:len(nasalclearTotalRx) - 1]
ni90th = novaitchTotalRx[ni90thIndex:len(novaitchTotalRx) - 1]
zp90th = zapapainTotalRx[zp90thIndex:len(zapapainTotalRx)- 1]

print(cc90th)

data.close();
