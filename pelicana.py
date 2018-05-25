import requests
from bs4 import BeautifulSoup
from itertools import count

def pericanaStore():

    pStorelist=[]

    for page in range(1,117): #count(start=1):

        url="http://pelicana.co.kr/store/stroe_search.html?page=%s" % page
        html=requests.get(url).content
        soup=BeautifulSoup(html,"html.parser")
        table=soup.find("table", {"class":"table mt20"})
        table_tbody=table.find("tbody")
        tr_tags=table_tbody.find_all("tr")

        for tr_tag in tr_tags:
            storeData=list(tr_tag.strings)
            name=storeData[1]
            tel=storeData[5].strip()
            address=storeData[3]

            print(name,tel,address)
            pStorelist.append([name,tel,address])

    return pStorelist

result=pericanaStore()
print(result)