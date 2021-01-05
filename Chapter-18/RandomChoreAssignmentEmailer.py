import random, smtplib

def sendChores():
    smtpObj = smtplib.SMTP_SSL('smtp.gmail.com')
    smtpObj.ehlo()
    print('---> Connection made with SMTP')
    smtpObj.login(senderEmail, senderEmailPW)
    print('--->Login Done!')
    for email in listOfEmails:
        randomChore = random.choice(listOfChores)
        listOfChores.remove(randomChore)
        print('--->Random chore chosen, now sending the mail')
        message = str('Subject: Your chore for this week\n' + randomChore)
        smtpObj.sendmail(senderEmail, email, message)
        print('--->EMail Sent!')
    smtpObj.quit()


listOfEmails = ['somemail@somemail.com', 'somemail@somemail.com','somemail@somemail.com','somemail@somemail.com']
listOfChores = ['dishes', 'bathroom', 'vacuum', 'walk dog']

senderEmail='yourEmail@somemail.com'
senderEmailPW='YOUR-EMAIL-PW'

sendChores()