from bs4 import BeautifulSoup
import csv

import urllib
r = urllib.urlopen("https://www.collegeswimming.com/recruiting/rankings/2018/F/")
soup = BeautifulSoup(r)
#print soup.prettify()
letters = soup.find_all("div", class_="ec_statements")


#for link in soup.find_all('a'):
#    print(link.get('href'))

print(soup)

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
    school = l[0].strip('\xca')
    division = l[3][:4] + ' ' + l[3][6:8]
    return [school, division, parseScholarship(l[6])]

def parseTopTimes(l):
    """
Example output by USA Swimming database:

 ['="Princeton Swimming \'Big Al\' Op"', '="3:53.19"', '="12/2/2017"', '="400 Individual Medley SCY Male"', '="BROW"', '="Brown"', 'Sullivan, Coley', '="M"', '="11/24/1997"', '="22"', '="1/1/1900 12:03:53 AM"', '=""', '=""', '="SO"', '="B"', '="98"', '="400 Yards Individual Medley Male SCY"', '="0"', '="Princeton"', '=""', '="N']
    """
    
    return l

test = readDB("TopTimes18.csv", parseTopTimes)
#print(test)

    
