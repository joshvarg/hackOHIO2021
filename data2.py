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
chloe10 = []
chloeRow = math.floor(len(cholecap) * .9)
while chloeRow < len(cholecap):
    chloe10.append(cholecap[chloeRow])
    chloeRow += 1
nasal10 = []
nasalRow = math.floor(len(nasalclear) * .9)
while nasalRow < len(nasalclear):
    nasal10.append(nasalclear[nasalRow])
    nasalRow += 1



# find the trend per drug per month

zapa1 = 0; zapa2 = 0; zapa3 = 0; zapa4 = 0; zapa5 = 0; zapa6 = 0
i = 0; 
while i < len(zapapain):
    zapa1 = int(zapapain[i][11]) + zapa1
    zapa2 = int(zapapain[i][12]) + zapa2
    zapa3 = int(zapapain[i][13]) + zapa3
    zapa4 = int(zapapain[i][14]) + zapa4
    zapa5 = int(zapapain[i][15]) + zapa5
    zapa6 = int(zapapain[i][16]) + zapa6
    i += 1

nova1 = 0; nova2 = 0; nova3 = 0; nova4 = 0; nova5 = 0; nova6 = 0
i = 0; 
while i < len(novaitch):
    nova1 = int(novaitch[i][11]) + nova1
    nova2 = int(novaitch[i][12]) + nova2
    nova3 = int(novaitch[i][13]) + nova3
    nova4 = int(novaitch[i][14]) + nova4
    nova5 = int(novaitch[i][15]) + nova5
    nova6 = int(novaitch[i][16]) + nova6
    i += 1

chloe1 = 0; chloe2 = 0; chloe3 = 0; chloe4 = 0; chloe5 = 0; chloe6 = 0
i = 0; 
while i < len(cholecap):
    chloe1 += int(cholecap[i][11])
    chloe2 += int(cholecap[i][12])  
    chloe3 += int(cholecap[i][13]) 
    chloe4 += int(cholecap[i][14]) 
    chloe5 += int(cholecap[i][15])
    chloe6 += int(cholecap[i][16]) 
    i += 1
nasal1 = 0; nasal2 = 0; nasal3 = 0; nasal4 = 0; nasal5 = 0; nasal6 = 0
i = 0; 
while i < len(nasalclear):
    nasal1 += int(nasalclear[i][11])
    nasal2 += int(nasalclear[i][12])  
    nasal3 += int(nasalclear[i][13]) 
    nasal4 += int(nasalclear[i][14]) 
    nasal5 += int(nasalclear[i][15])
    nasal6 += int(nasalclear[i][16]) 
    i += 1
