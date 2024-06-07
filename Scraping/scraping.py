from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

url="https://en.wikipedia.org/wiki/List_of_floods_in_Pakistan"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
soup.prettify()
des=[]
ur=[]
b=soup.find('ul')
for x in b.find_all('li'): 
    des.append(x.text)

for x in range(0,14): 
    ur.append(url)

d = {
    'url': ur,
    'description':des
}
df = pd.DataFrame.from_dict(d)
df.to_csv("scraping.csv")
print(df['description'])
df1=pd.read_csv('scraping.csv')

kpk_year=[]
pun_year=[]
sindh_year=[]
bol_year=[]
gil_year=[]
fed_year=[]

mon=["June","July","August"]
for i in df1['description']:
    mflag=0
    if "Khyber" in i :
        n=i.split()
        for j in n:
            if(re.findall('[0-9]{4}',j)):
                qq=j
                pass
            elif(j=="monsoon" and mflag==0):       
                for w in mon:
                    kpk_year.append(w+" "+qq)
                mflag=mflag+1
            elif(j=="Janruary"):
                kpk_year.append(j+" "+qq)
            elif(j=="February"):
                kpk_year.append(j+" "+qq)
            elif(j=="March"):
                kpk_year.append(j+" "+qq)
            elif(j=="April"):
                kpk_year.append(j+" "+qq)
            elif(j=="May"):
                kpk_year.append(j+" "+qq)
            elif(j=="June" and mflag==0):
                kpk_year.append(j+" "+qq)
            elif(j=="July" and mflag==0):
                kpk_year.append(j+" "+qq)
            elif(j=="August" and mflag==0):
                kpk_year.append(j+" "+qq)
            elif(j=="September"): 
                kpk_year.append(j+" "+qq)
            elif(j=="October"):
                kpk_year.append(j+" "+qq)
            elif(j=="November"):
                kpk_year.append(j+" "+qq)
            elif(j=="December"):         
                kpk_year.append(j+" "+qq)                  

for i in df1['description']:
    mflag=0
    if "Punjab" in i :
        n=i.split()
        for j in n:
            if(re.findall('[0-9]{4}',j)):
                qq=j
                pass
            elif(j=="monsoon" and mflag==0):       
                for w in mon:
                    pun_year.append(w+" "+qq)
                mflag=mflag+1
            elif(j=="Janruary"):
                pun_year.append(j+" "+qq)
            elif(j=="February"):
                pun_year.append(j+" "+qq)
            elif(j=="March"):
                pun_year.append(j+" "+qq)
            elif(j=="April"):
                pun_year.append(j+" "+qq)
            elif(j=="May"):
                pun_year.append(j+" "+qq)
            elif(j=="June" and mflag==0):
                pun_year.append(j+" "+qq)
            elif(j=="July" and mflag==0):
                pun_year.append(j+" "+qq)
            elif(j=="August" and mflag==0):
                pun_year.append(j+" "+qq)
            elif(j=="September"): 
                pun_year.append(j+" "+qq)
            elif(j=="October"):
                pun_year.append(j+" "+qq)
            elif(j=="November"):
                pun_year.append(j+" "+qq)
            elif(j=="December"):         
                pun_year.append(j+" "+qq)

for i in df1['description']:
    mflag=0
    if "Balochistan" in i :
        n=i.split()
        for j in n:
            if(re.findall('[0-9]{4}',j)):
                qq=j
                pass
            elif(j=="monsoon" and mflag==0):       
                for w in mon:
                    bol_year.append(w+" "+qq)
                mflag=mflag+1
            elif(j=="Janruary"):
                bol_year.append(j+" "+qq)
            elif(j=="February"):
                bol_year.append(j+" "+qq)
            elif(j=="March"):
                bol_year.append(j+" "+qq)
            elif(j=="April"):
                bol_year.append(j+" "+qq)
            elif(j=="May"):
                bol_year.append(j+" "+qq)
            elif(j=="June" and mflag==0):
                bol_year.append(j+" "+qq)
            elif(j=="July" and mflag==0):
                bol_year.append(j+" "+qq)
            elif(j=="August" and mflag==0):
                bol_year.append(j+" "+qq)
            elif(j=="September"): 
                bol_year.append(j+" "+qq)
            elif(j=="October"):
                bol_year.append(j+" "+qq)
            elif(j=="November"):
                bol_year.append(j+" "+qq)
            elif(j=="December"):         
                bol_year.append(j+" "+qq)                  

for i in df1['description']:
    mflag=0
    if "Islamabad" in i :
        n=i.split()
        for j in n:
            if(re.findall('[0-9]{4}',j)):
                qq=j
                pass
        fed_year.append("July 2021")

for i in df1['description']:
    if "Islamabad" in i :
        n=i.split()
        for j in n:
            if(re.findall('[0-9]{4}',j)):
                qq=j
                pass
        fed_year.append("July 2021")

gil_year.append("September 2014")
gil_year.append("July 2018")

for i in df1['description']:
    mflag=0
    if "Sindh" in i or "Karachi" in i :
        n=i.split()
        for j in n:
            if(re.findall('[0-9]{4}',j)):
                qq=j
                pass
            elif(j=="monsoon" and mflag==0):       
                for w in mon:
                    sindh_year.append(w+" "+qq)
                mflag=mflag+1
            elif(j=="Janruary"):
                sindh_year.append(j+" "+qq)
            elif(j=="February"):
                sindh_year.append(j+" "+qq)
            elif(j=="March"):
                sindh_year.append(j+" "+qq)
            elif(j=="April"):
                sindh_year.append(j+" "+qq)
            elif(j=="May"):
                sindh_year.append(j+" "+qq)
            elif(j=="June" and mflag==0):
                sindh_year.append(j+" "+qq)
            elif(j=="July" and mflag==0):
                sindh_year.append(j+" "+qq)
            elif(j=="August" and mflag==0):
                sindh_year.append(j+" "+qq)
            elif(j=="September"): 
                sindh_year.append(j+" "+qq)
            elif(j=="October"):
                sindh_year.append(j+" "+qq)
            elif(j=="November"):
                sindh_year.append(j+" "+qq)
            elif(j=="December"):         
                sindh_year.append(j+" "+qq)                  
    

