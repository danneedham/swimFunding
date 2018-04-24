import csv

def readDB(database, parser):
    "Reads in csv file"
    result = []
    with open(database, 'r') as f:
        csvf = csv.reader(f)
        f.readline()
        for line in csvf:
            result.append(parser(line))
    return result

    #iterate through string and if char is a number (in 0-9) print string from that point on.


def parseScholarship(scholarship):
    for i in range(len(scholarship)-1):
        if scholarship[i] in {'0','1','2','3','4','5','6','7','8','9'}:
            return scholarship[i:]
        
            
def parseSchool(l):
    """Takes the list printed out for each school and returns a list with the variables we care about.
    """
    school = l[0]
    division = l[3][:4] + ' ' + l[3][6:8]
    return [school, division, parseScholarship(l[6])]

print(readDB("SwimFundingData.csv", parseSchool))

    
