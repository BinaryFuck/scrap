
import requests
from bs4 import BeautifulSoup

target ="https://gizmodo.com/tag/science"
res = requests.get(target).text
soup = BeautifulSoup(res, "html.parser")
section = soup.find('div', class_="sc-17uq8ex-0 iLteOs")
for article in section.find_all('article', class_="cw4lnv-0 iTueKC js_post_item"):
    type = article.find('span', class_="vxl3c2-0 ebYGmw")
    title = article.find('h2', class_="sc-759qgu-0 iSjOfj cw4lnv-6 fGbMFF")
    description=article.find('p', class_="sc-77igqf-0 bOfvBY")
    print(title.text)
    print(type.text)
    print(description.text)
    print()
    
    #fuck It Take almost 2 hours Lolz
