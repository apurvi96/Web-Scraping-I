#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WEB SCRAPING:Extract 10-12 features of 500 mobile phones from flipkart
using Beautiful soap
"""
def go_to_each_link(url1):
    
    li=[]
    
    base_url="https://www.flipkart.com"
    actual_url=base_url+url1
    r1=requests.get(actual_url)
    
    #remove bad character from name of mobile 
    bad_char='\xa0'
    print("-----")
    soupn=BeautifulSoup(r1.content,'html5lib')
    phone=soupn.find("span",{"class":"_35KyD6"})
    pname=phone.text
    pname=pname.replace(bad_char,' ')
    li.append(pname)
    features=soupn.find_all("div",{"class":"_2RngUh"})
    
    for i in features:
        
        v1=i.find_all("td",{"class":"_3-wDH3 col col-3-12"})
        
        for j in v1:
            if(j.text=="Model Number"):
               li.append(j.nextSibling.ul.li.text)#nextSibling 
               
            if(j.text=="SIM Type"):
                li.append(j.nextSibling.ul.li.text)
                
            elif(j.text=="Display Size"):
                li.append(j.nextSibling.ul.li.text)
             
            elif(j.text=="Resolution"):
                li.append(j.nextSibling.ul.li.text)
               
            elif(j.text=="Processor Type"):
                li.append(j.nextSibling.ul.li.text)
               
            elif(j.text=="Processor Core"):
                li.append(j.nextSibling.ul.li.text)
               
            elif(j.text=="Internal Storage"):
                li.append(j.nextSibling.ul.li.text)
               
            elif(j.text=="RAM"):
                li.append(j.nextSibling.ul.li.text)
               
            elif(j.text=="Primary Camera"):
                li.append(j.nextSibling.ul.li.text)
              
            elif(j.text=="Network Type"):
                li.append(j.nextSibling.ul.li.text)
            
            elif(j.text=="Battery Capacity"):
                li.append(j.nextSibling.ul.li.text)
               
        
        
    #writing to csv file   
    with open('mobiles.csv','a') as wfile:
        filew=csv.writer(wfile,delimiter=',')
        filew.writerow(li)

    
import os
import requests
import csv
from bs4 import BeautifulSoup

os.system("clear")

n=0
k=1

#NAME OF FEATURES BEING EXTRACTED WRITTEN TO CSV FILE
with open('mobiles.csv','w') as readfile:
    filew=csv.writer(readfile,delimiter=',')
    filew.writerow(['mobile','Model','sim type','display size','resolution','processor type','processor core','internal storage','ram','camera','network type','battery'])

while(n<=500):
    #url to mobile section of flipkart
    url="https://www.flipkart.com/search?q=mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_5_na_na_pr&otracker1=AS_QueryStore_OrganicAutoSuggest_0_5_na_na_pr&as-pos=0&as-type=HISTORY&suggestionId=mobiles&requestId=41431f4c-d3e9-4a18-9732-3f88215084e1&page="+str(k);
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html5lib')
    
    #stores link of all the mobiles present at one page
    links=soup.find_all("a",{"class":"_31qSD5"})
    
        
    #open link of each phone and extract features     
    for i in links:
     go_to_each_link(i['href'])
    
    #maintain no. of phones
    n=n+len(links)
    k=k+1
    
