from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import datetime
driver=webdriver.Chrome()
l1,l2,l3,l4,l5,l6,l7=[],[],[],[],[],[],[]
for i in range(1,216):
    url="http://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;orderby=player;page="+str(i)+";template=results;type=batting;view=year"
    driver.get(url)
    content=driver.page_source
    soup=BeautifulSoup(content,features="html.parser")
    data=[[b.text for b in a.find_all("td")] for a in soup.find_all("tr",{"class":"data1"})]
    for j in range(len(data)):
        l1.append(data[j][0])
        l2.append(data[j][1])
        l3.append(data[j][4])
        l4.append(data[j][6])
        l5.append(data[j][9])
        l6.append(data[j][10])
        l7.append(data[j][12])
df=pd.DataFrame({"Player":l1,"Matches":l2,"Runs":l3,"Average":l4,"100s":l5,"50s":l6,"Year":l7})
df.to_csv('yearly_stats.csv', index=False, encoding='utf-8')
now = datetime.datetime.now()
df=dict(pd.read_csv("yearly_stats.csv"))
l=[]
for i in range(len(df["Average"])):
    l.append([df["Player"][i],df["Runs"][i],df["Year"][i],df["100s"][i],df["50s"][i]])
cricketer=input("Enter player name with country in braces(Ex. Player (Country)):\nINDIA for india\nAUS for australia\nENG for england\nSA for south africa\nWI for west indies\n and so on\n")
year=int(input("Enter year upto which you want to get runs:"))
r,c,f=0,0,0
fi,h=0,0
list2=[]
for i in l:
    if i[0]==cricketer :
        c+=1
        list2.append(i[2])
        if i[2]<=year:
            r+=int(i[1])
            h+=int(i[3])
            fi+=int(i[4])
        f=1
    if c==list2.count(cricketer) and f==1:
        break
if list2[-1]==now.year:
    print("He is still playing!!")
else:
    print("Last year he played:"+str(list2[-1]))
print("Total no.of runs till "+str(year)+":"+str(r))
print("With "+str(fi)+" fifties and "+str(h)+" hundreds")