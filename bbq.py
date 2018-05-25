#ajax--->url을 알아내야함
import requests
from bs4 import BeautifulSoup
from itertools import count
import pandas as pd

def bbqStore():
    bbqstoreList=[]

    for page in count(start=1): # 시작점만 있고 계속 무한 end가 있으면 range와 의미가 같아서 무한루프 개념이 아님
        url = "http://changup.bbq.co.kr/findstore/findstore_ajax.asp?page=%s" % page
        html=requests.get(url).text
        soup=BeautifulSoup(html,"html.parser")
        tbody_tag=soup.find("tbody")
        tr_tags=tbody_tag.find_all("tr")
        #마지막 태그 찾는 조건
        if len(tr_tags)<=1:
           break
        #리스트 0번재 포함시키지 않는 조건
        for i, tr_tag in enumerate(tr_tags):
            if i !=0:
                storeList=list(tr_tag.strings)
                name=storeList[1]
                tel=storeList[5]
                address=storeList[3]
                bbqstoreList.append([name,tel,address])

    table=pd.DataFrame(bbqstoreList,columns=["name", "tel", "address"])
    table.to_csv("D:/spring/webdata/bbq_table.csv",encoding="utf-8-sig",mode="w",index=True)
    return bbqstoreList

result=bbqStore()
print(result)





# def bbq():
#     bStorelist=[]
#
#     for page in range(1, 144):
#         url="http://changup.bbq.co.kr/findstore/findstore_ajax.asp?page=%s" % page
#         html=requests.get(url).text
#         soup=BeautifulSoup(html,"html.parser")
#         table=soup.find("table", {"class":"table01"})
#         tr_tags=table.find_all("tr")
#
#         for tr_tag in tr_tags:
#             storeData=list(tr_tag.strings)
#             name=storeData[1]
#             tel=storeData[5]
#             address=storeData[3]
#             bStorelist.append([name,tel,address])
#
#     return bStorelist
#
# result=bbq()
# print(result)