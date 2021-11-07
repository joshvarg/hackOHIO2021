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

currentRow = int; currentCol = int;
currentRow = 0; currentCol = 11
currentTotalSum = 0; maxTotalSum = 0;
cholecap = []
nasalclear = []
novaitch = []
zapapain = []

while currentRow < len(rows):
    while currentCol < 17:
        currentTotalSum = currentTotalSum + int(rows[currentRow][currentCol])
        currentCol += 1
    rows[currentRow].insert(currentCol,currentTotalSum)
        
    if maxTotalSum < currentTotalSum :
        maxTotalSum = currentTotalSum
    currentCol = 11
    currentRow += 1
    currentTotalSum = 0
    
currentRow = 0
while currentRow < len(rows):
    if rows[currentRow][4] == 'Cholecap':
        cholecap.append(rows[currentRow])
    if rows[currentRow][4] == 'Nasalclear':
        nasalclear.append(rows[currentRow])
    if rows[currentRow][4] == 'Nova-itch':
        novaitch.append(rows[currentRow])
    if rows[currentRow][4] == 'Zap-a-Pain':
        zapapain.append(rows[currentRow])

    currentRow += 1
# sort by total perscriptions
zapapain.sort(key=lambda x: x[17])
novaitch.sort(key=lambda x: x[17])
cholecap.sort(key=lambda x: x[17])
nasalclear.sort(key=lambda x: x[17])

zapa10 = []
zapaRow = math.floor(len(zapapain) * .9)
while zapaRow < len(zapapain):
    zapa10.append(zapapain[zapaRow])
    zapaRow += 1
nova10 = []
novaRow = math.floor(len(novaitch) * .9)
while novaRow < len(novaitch):
    nova10.append(novaitch[novaRow])
    novaRow += 1
chole10 = []
choleRow = math.floor(len(cholecap) * .9)
while choleRow < len(cholecap):
    chole10.append(cholecap[choleRow])
    choleRow += 1
nasal10 = []
nasalRow = math.floor(len(nasalclear) * .9)
while nasalRow < len(nasalclear):
    nasal10.append(nasalclear[nasalRow])
    nasalRow += 1


json = open("topDoctors.json", "x")
json.write("{\"medicine\": \"Cholecap\",")
json.write("    \"90th percentile\":[")
for i in range(0,len(chole10)):
    json.write("        {\"name\": \"" + chole10[i][1] + " " + chole10[i][2] + "\",")
    json.write("        \"state\": \"" + chole10[i][3] + "\",")
    json.write("        \"tRx\":" + int(chole10[i][17]) + ",")
    json.write("        \"ID#\":" + int(chole10[i][0]) + "," )
    json.write("        }")
json.write("    ]")
json.write("}")
json.write("{\"medicine\": \"Nasalclear\",")
json.write("    \"90th percentile\":[")
for i in range(0,len(nasal10)):
    json.write("        {\"name\": \"" + nasal10[i][1] + " " + nasal10[i][2] + "\",")
    json.write("        \"state\": \"" + nasal10[i][3] + "\",")
    json.write("        \"tRx\":" + int(nasal10[i][17]) + ",")
    json.write("        \"ID#\":" + int(nasal10[i][0]) + "," )
    json.write("        }")
json.write("    ]")
json.write("}")
json.write("{\"medicine\": \"Nova-itch\",")
json.write("    \"90th percentile\":[")
for i in range(0,len(nova10)):
    json.write("        {\"name\": \"" + nova10[i][1] + " " + nova10[i][2] + "\",")
    json.write("        \"state\": \"" + nova10[i][3] + "\",")
    json.write("        \"tRx\":" + int(nova10[i][17]) + ",")
    json.write("        \"ID#\":" + int(nova10[i][0]) + "," )
    json.write("        }")
json.write("    ]")
json.write("}")
json.write("{\"medicine\": \"Zap-a-Pain\",")
json.write("    \"90th percentile\":[")
for i in range(0,len(zapa10)):
    json.write("        {\"name\": \"" + zapa10[i][1] + " " + zapa10[i][2] + "\",")
    json.write("        \"state\": \"" + zapa10[i][3] + "\",")
    json.write("        \"tRx\":" + int(zapa10[i][17]) + ",")
    json.write("        \"ID#\":" + int(zapa10[i][0]) + "," )
    json.write("        }")
json.write("    ]")
json.write("}")




