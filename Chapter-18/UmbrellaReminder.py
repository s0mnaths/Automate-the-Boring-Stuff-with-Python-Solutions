from twilio.rest import Client
import requests,bs4

def checkWeather():
    #weather for my location
    url='https://weather.com/en-IN/weather/today/l/c4f563fc66d4273f615efd8ff16cbc4c0f09afe96cd6af254caf40a9934e88d3' 
    res=requests.get(url)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text, "html.parser")
    weather=soup.select('.CurrentConditions--phraseValue--2xXSr')
    weatherDescription=weather[0].getText()
    if 'rain' in weatherDescription.lower() or 'drizzle' in weatherDescription.lower():
        twilioCli.messages.create(body='Might Rain today! Remember to carry an umbrella!', from_=myTwilioNumber, to=myCellPhone)


accountSID = 'YOUR-ACC-SID'
authToken  = 'YOUR-AUTH TOKEN'
twilioCli = Client(accountSID, authToken)
myTwilioNumber = 'YOUR-TWILIO-NUMBER'
myCellPhone = 'YOUR-NUMBER-REGISTERED-WITH-TWILIO'

checkWeather()