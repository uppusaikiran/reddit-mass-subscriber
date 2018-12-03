import time
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests
base_url = "https://snoopsnoo.com/subreddits/technology/"
next_page = base_url
while (next_page):
    print 'Exploring Page {}'.format(next_page)
    resp = requests.get(next_page)
    http_encoding = resp.encoding if 'charset' in resp.headers.get('content-type', '').lower() else None
    html_encoding = EncodingDetector.find_declared_encoding(resp.content, is_html=True)
    encoding = html_encoding or http_encoding
    soup = BeautifulSoup(resp.content, from_encoding=encoding)
    for link in soup.find_all('a', href=True):
        if str(link['href'])[0:3] == '/r/':
            print "Found the URL:", link['href']
            with open('final_reddit.txt','a') as f:
                f.write(link['href'])
                f.write('\n')
        elif str(link['href'])[0:3] == '?c=':
            print 'Next Page : {}'.format(link['href'])
            next_page = base_url + link['href']

        time.sleep(2)

