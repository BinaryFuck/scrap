import urllib.request
from bs4 import BeautifulSoup
import json

url = 'https://old.reddit.com/top/'

request = urllib.request.Request(url)
html = urllib.request.urlopen(request).read()

soup = BeautifulSoup(html, 'html.parser')
main_table = soup.find('div', attrs={'id': 'siteTable'})

links = main_table.find_all("a", class_="title")
extracted_links = []
for link in links:
    title = link.text
    url = link['href']
    if not url.startswith('http'):
        url = "https://reddit.com/" + url
    records = {
        'title': title,
        'Url': url
    }
    extracted_links.append(records)
print(extracted_links)
with open('data.json', 'w') as outfile:
    json.dump(extracted_links, outfile)
