import os,requests, bs4, pprint

def getImgur(searchQuery):
    print('--->Starting Scraping')
    os.makedirs('Imgur-Downloads', exist_ok=True)
    baseURL='https://imgur.com'
    res=requests.get(baseURL+'/search?q='+searchQuery)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text, 'html.parser')
    
    foundElems=soup.select('.sorting-text-align > i')
    numOfPosts=int(foundElems[0].getText())
    if numOfPosts==0:
        print('No Results Found for the search "'+searchQuery+'".')
        return
    else:
        print('--->'+str(numOfPosts)+' results found for the search "'+searchQuery+'".\n')
    
    postElems = soup.select('.post a')
    for post in postElems:
        imgPostLink=baseURL+post.get('href')
        res=requests.get(imgPostLink)
        res.raise_for_status()
        
        soup=bs4.BeautifulSoup(res.text,'html.parser') 
        imgElems = soup.find("meta",  property="og:image")
        imgElemsLink=imgElems["content"]
        imgURL, trail=imgElemsLink.split('?')

        imageFile = open(os.path.join('Imgur-Downloads', os.path.basename(imgURL)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        print('--->Downloaded : '+ os.path.basename(imgURL))
    
    print('\n--->All results downloaded!')



searchQuery=input('Enter search query: ')
getImgur(searchQuery)