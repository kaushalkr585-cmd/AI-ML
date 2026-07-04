#import requests
#from bs4 import BeautifulSoup

#url = "https://timesofindia.indiatimes.com/india"
#response=requests.get(url)

#soup=BeautifulSoup(response.text,'html.parser')
#print(soup.title.text)

#print(soup.find("h1").text)

import requests
def fetchAndSaveToFile(url,path):
    r=requests.get(url)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(r.text)
URL = "https://timesofindia.indiatimes.com/india"

fetchAndSaveToFile(URL, "india_news.html")
