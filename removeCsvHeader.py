#! /usr/bin/env python3

import csv, os

os.makedirs('headerRemoved', exist_ok=True )
for csvFile in os.listdir('.'):
    if not csvFile.endswith('.csv'):
        continue 
    print('Removing headline from file '+ csvFile + '...')
    csvRows = []
    csvFileObj  = open(csvFileObj)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num ==1:
            continue 
        csvRows.append(row)
    csvFileObj.close()

    csvFileObj = open(os.path.join('headerRemved', csvFile), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()