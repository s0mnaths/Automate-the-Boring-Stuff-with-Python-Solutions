#THIS PROGRAM IS NOT YET COMPLETE!!!!!!

import os,requests, bs4

def getImgur(searchQuery):
    os.makedirs('Imgur-Downloads', exist_ok=True)
    baseURL='https://imgur.com'
    res=requests.get(baseURL+'/search?q='+searchQuery)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text, 'html.parser')
    postElems = soup.select('.post a')

    for post in postElems:
        imgPostLink=baseURL+post.get('href')
        res=requests.get(imgPostLink)
        res.raise_for_status()
        soup=bs4.BeautifulSoup(res.text,'html.parser')
        print('checkpoint-1')
        imgElem=soup.findAll('.imageContainer zoomable > img.image-placeholder')  #GETTING ISSUE WITH SELECTORS
        if imgElem==[]:
            print('empty')
            continue
        for img in imgElem:
            print(img.get('src'))



#searchQuery=input('Enter search query: ')
searchQuery='python programming'
getImgur(searchQuery)
