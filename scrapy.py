import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import time
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests


no_pages = 2

def get_data(pageNo):
    header = {"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    r = requests.get("https://www.amazon.in/gp/bestsellers/books/")
    content = r.content
    soup = BeautifulSoup(content)
    print(soup)

    alls = []
    for d in soup.findAll('div', attrs={'class':'a-section a-spacing-none aok-relative'}):
        name = d.find('span', attrs={'class': 'zg-text-center-align'})
        n = name.find_all('img', alt=True)
        author = d.find('a', attrs={'class': 'a-size-small a-link-child'})
        rating = d.find('span', attrs={'class': 'a-icon-alt'})
        user_rated = d.find('a', attrs={'class': 'a-size-small a-link-normal'})
        price = d.find('span', attrs={'class': 'p13n-sc-price'})

        all1 = []
        if name is not None:
            all1.append(n[0]['alt'])
        else :
            all1.append("Unknown Product")

        if author is not None:
            all1.append(author.text)
        elif author is None:
            author = d.find ('span', attrs={'class': 'a-size-small a-color-base'})
            if author is not None:
                all1.append(author.text)
            else:
                all1.append('0')

        if rating is not None:
            all1.append(rating.text)
        else:
            all1.append('-1')
        if user_rated is not None:
            all1.append(user_rated.text)
        else :
            all1.append('0')
        if price is not None:
            all1.append(price.text)
        else:
            all1.append('0')
        alls.append(all1)

    return alls

results = []
for i in range(1, no_pages+1):
    results.append(get_data(i))
flatten = lambda l: [item for sublist in l for item in sublist]
df = pd.DataFrame(flatten(results),columns=['Book Name','Author','Rating','Customers_Rated', 'Price'])
df.to_csv('amazon_products.csv', index=False, encoding='utf-8')
