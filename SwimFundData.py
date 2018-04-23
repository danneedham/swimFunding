import csv

def readDB(database):
    "Reads in csv file"
    result = []
    with open(database, 'r') as f:
        csvf = csv.reader(f)
        f.readline()
        for line in csvf:
            result.append(line)
    return result

print(readDB("SwimFundingData.csv"))
