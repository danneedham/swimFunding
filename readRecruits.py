import urllib.request
import pprint
import csv
from bs4 import BeautifulSoup


url = 'https://www.collegeswimming.com/recruiting/rankings/'
page = urllib.request.urlopen(url)
listm = [url + '2018/M/'];
for i in range(2,50):
    url2 = url + '2018/M/?page=' + str(i)
    listm.append(url2)
    url3 = url + '2017/M/?page=' + str(i)
    listm.append(url3)
    url4 = url + '2016/M/?page=' + str(i)
    listm.append(url4)

listw = [url + '2018/W/'];
for i in range(2,50):
    url2 = url + '2018/F/?page=' + str(i)
    listw.append(url2)
    url3 = url + '2017/F/?page=' + str(i)
    listw.append(url3)
    url4 = url + '2016/F/?page=' + str(i)
    listw.append(url4)



schoolDictM = dict()
schoolDictW = dict()

def add(school, index, dic):
    if school in dic:
        dic[school].add(index)
    else:
        dic[school]= set()
        dic[school].add(index)

def mean(set):
    return sum(set)/len(set)

def printList(dic):
    pp = pprint.PrettyPrinter()
    pp.pprint(sorted(dic.items(),key=lambda x:x[1]))

#Finds all information for a recruit page
def soupItUp (link, dic):
    page = urllib.request.urlopen(link)
    soup = BeautifulSoup(page, 'html.parser')
    swimmers = soup.find_all('tr')
    for swimmer in swimmers:
        if swimmer is not None:
            index = swimmer.find('td', {"class":"c-table-clean__power-index"})
            school = swimmer.find('a', {"class":"u-inline-block"})
            if index is not None:
                if school is not None:
                    add(school['title'],float(index.text), dic)

def runItUP():
    for i in range(0, len(listm) - 1):
        soupItUp(listm[i], schoolDictM)
        soupItUp(listw[i], schoolDictW)
    for key in schoolDictM:
        schoolDictM[key] = mean(schoolDictM[key])
    for key in schoolDictW:
        schoolDictW[key] = mean(schoolDictW[key])
    with open('mensIndex.csv','w') as f:
        w = csv.writer(f)
        w.writerows(schoolDictM.items())
    with open('womensIndex.csv','w') as f:
        w = csv.writer(f)
        w.writerows(schoolDictW.items())

runItUP()
print("Men's Teams: \n")
printList(schoolDictM)
print("Women's Teams: \n")
printList(schoolDictW)
