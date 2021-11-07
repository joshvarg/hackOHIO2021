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

for i in range(0, len(stateAndSums)):
    ratio = 1.0*stateAndSums[i][1]/stateAndSums[i][2]
    stateAndSums[i].append(ratio)

stateAndSums.sort(key = lambda x : x[3])
lowerBound = math.floor(len(stateAndSums) * .6)
upperBound = math.ceil(len(stateAndSums) * .8)

emergingMarkets = stateAndSums[lowerBound:upperBound]
maxRatio = stateAndSums[len(stateAndSums)-1][3]
for i in range(0, len(emergingMarkets)):
    proj = emergingMarkets[i][2] * maxRatio
    emergingMarkets[i].append(proj)
    target = proj - emergingMarkets[i][1]
    emergingMarkets[i].append(target)



#JSON output includes the market classification as emerging, the lower bound of market percentiles, the upper bound
#of the same thing, and the maximum ratio of new prescriptions to total prescriptions. Also included are the states
#that are emerging markets. The state objects contain data with the name of the state, the current new prescriptions
#over 6 months, the current total prescriptions over 6 months, the ratio of new to total, the projected new 
#prescriptions, and the target of new prescriptions. The projection is calculated by multiplying the current total
#prescriptions by the maximum ratio, essentially maximizing new prescriptions per state. The target is then 
#calculated by subtracting the current prescriptions from the projection, giving a change in prescriptions, thus
#representing the target increase

json = open("stateAnalysis.json", "w")
json.write("{\"markets\": \"Emerging\",")
json.write("\"lower bound\": 60,")
json.write("\"upper bound\": 80,")
json.write("\"max ratio\": " + str(maxRatio) + ",")
json.write("\"targets\":[")

for i in range(0, len(emergingMarkets)):
    json.write("{\"name\": \"" + emergingMarkets[i][0] + "\",")
    json.write("\"nRx\": " + str(emergingMarkets[i][1]) + ",")
    json.write("\"tRx\": " + str(emergingMarkets[i][2]) + ",")
    json.write("\"ratio\": " + str(emergingMarkets[i][3]) + ",")
    json.write("\"proj\": " + str(emergingMarkets[i][4]) + ",")
    json.write("\"target\": " + str(emergingMarkets[i][5]))
    json.write("}")
    if i < len(emergingMarkets) - 1:
        json.write(",")

json.write("]}")

