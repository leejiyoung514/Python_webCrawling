import requests
from bs4 import BeautifulSoup

def naver_movie():

    url="https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
    html=requests.get(url).text
    soup=BeautifulSoup(html,"html.parser")
    tags=soup.find_all("div",{"class":"tit3"})

    for index, tag in enumerate(tags):
        tag.a.get_text() #tag.a.text
        print(index+1, tag.a.get_text())

naver_movie()