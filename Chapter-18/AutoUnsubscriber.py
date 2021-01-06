import imapclient,pyzmail,bs4,webbrowser

YOUREMAIL='YOUREMAIL@someMail.com'
YOURPASSWORD='PASSWORD'
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login(YOUREMAIL,YOURPASSWORD)
imapObj.select_folder('INBOX', readonly=True)
UIDs=imapObj.search('ALL')

for UID in UIDs:
    rawMessages = imapObj.fetch([UID], ['BODY[]'])
    message = pyzmail.PyzMessage.factory(rawMessages[UID][b'BODY[]'])
    if message.html_part != None:
        try:
            htmlBody=message.html_part.get_payload().decode(message.html_part.charset)
            soup=bs4.BeautifulSoup(htmlBody,'html.parser')
            allLinks = soup.select('a')
            for link in allLinks:
                if 'unsubscribe' in link.text.lower():
                    webbrowser.open(link.get('href'))
        except:
            print('--->Could not read the Email with UID '+UID)

imapObj.logout()