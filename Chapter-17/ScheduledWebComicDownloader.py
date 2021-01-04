import os, bs4, requests

def updateWebComics():
    url = 'https://xkcd.com'
    resp = requests.get(url)
    resp.raise_for_status()
    soup = bs4.BeautifulSoup(resp.text, 'html.parser')
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = comicElem[0].get('src')
        if not os.path.basename(comicUrl) in os.listdir(webComicFolder):
            resp = requests.get('https:' + comicUrl)
            resp.raise_for_status()
            imageFile = open(os.path.join(webComicFolder, os.path.basename(comicUrl)), 'wb')
            for chunk in resp.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()



webComicFolder='/home/somubuntu/Desktop/web-comics'
os.makedirs(webComicFolder, exist_ok=True)

updateWebComics()