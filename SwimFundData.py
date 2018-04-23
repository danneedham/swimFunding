import csv

def readDB(database):
    "Reads in csv file"
    result = []
    with open(database, 'r') as f:
        csvf = csv.reader(f)
        f.readline()
        for line in csvf:
            result.append(parseSchool(line))
    return result



def parseSchool(l):
    """Takes the list printed out for each school and returns a list with the variables we care about.
    """
    school = l[0]
    division = l[3][:4] + ' ' + l[3][6:8]
    scholarship = l[6]
    for i in range(len(scholarship)-1):
        #if scholarship[i] == "\xca":
        #    scholarship = scholarship[:i+1]
        print(scholarship[i])

    return [school, division, scholarship]

test = readDB("SwimFundingData.csv")
print(test)
    
