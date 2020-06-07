# 크롤링 라이브러리
import requests
from bs4 import BeautifulSoup

def kor(keyword):


    req = requests.get(
        "https://s.search.naver.com/n/csearch/content/eprender.nhn?where=nexearch&pkid=252&q="+keyword+"영문주소&key=address_eng")

    soup = BeautifulSoup(req.text, 'html.parser')

    list_kor = []
    list_eng = []
    list_post = []


    for i in soup.select("#content > div > div.ds_box > div.result > div.result.result_v1 > div > table > tbody > tr > td > dl > dd > span"):
        list_kor.append(i.text)

    for j in soup.select("#content > div > div.ds_box > div.result > div.result.result_v1 > div > table > tbody > tr > td > strong"):
        list_eng.append(j.text)

    for r in soup.select("#content > div > div.ds_box > div.result > div.result.result_v1 > div > table > tbody > tr > td.tc"):
        list_post.append(r.text)

    return list_kor , list_eng , list_post

