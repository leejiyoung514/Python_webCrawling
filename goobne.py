import time
from selenium import webdriver
from bs4 import BeautifulSoup
from itertools import  count
import pandas as pd

def goobneStore():
    wd=webdriver.Chrome("D:/spring/webdriver/chromedriver.exe")
    wd.get("https://www.goobne.co.kr/store/search_store.jsp")
    #wd.execute_script("store.getList(%s)" % 100)
    #time.sleep(100)
    goobneStoreList = []

    for page in count(start=100): #무한루프

        wd.execute_script("store.getList(%s)" % page)
        time.sleep(5)
        html=wd.page_source
        soup=BeautifulSoup(html, "html.parser")

        tbody_tag=soup.find("tbody",{"id":"store_list"})
        tr_tags=tbody_tag.find_all("tr")
        test=tr_tags[0].get("class")
        print(test)

        if tr_tags[0].get("class") is None:
            break

        for tr_tag in tr_tags:
            stringList=list(tr_tag.strings)
            name=stringList[1]
            tel=stringList[3]
            address=stringList[5] if stringList[3] == ' ' else stringList[6]
            goobneStoreList.append([name, tel, address])
            #print(stringList)

    wd.quit() #브라우저 강제로 닫기

    table = pd.DataFrame(goobneStoreList, columns=["name", "tel", "address"])
    table.to_csv("D:/spring/webdata/goobne_table.csv", encoding="utf-8-sig", mode="w", index=True)
    return goobneStoreList

result=goobneStore()
print(result)