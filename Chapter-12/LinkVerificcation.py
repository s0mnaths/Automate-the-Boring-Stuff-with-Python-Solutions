import requests
import bs4

url = 'https://amfoss.in'
res = requests.get(url)
res.raise_for_status()
print('got the website') #

soup = bs4.BeautifulSoup(res.text, 'html.parser')
allLinks=soup.select('a')
for link in allLinks:
    hrefURL = link['href']
    if hrefURL.startswith('/'):
        hrefURL=url+hrefURL
    elif hrefURL.startswith('#'):
        hrefURL=url+hrefURL
    elif hrefURL.startswith('mailto:'):
        continue
        
    try:
        res = requests.get(hrefURL)
        if res.status_code == 404:
            print('Status Code 404 : ' + hrefURL)
    except:
        pass
print('All links checked!')