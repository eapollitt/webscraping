

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import openpyxl as xl
from openpyxl.styles import Font






url = 'https://coinmarketcap.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}


req = Request(url, headers=headers)

webpage = urlopen(req).read()


soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title


currency_rows = soup.findAll('td')
#print(currency_rows)


counter = 0
row_count = 1
for x in range(1,6):
    #td = currency_rows[x]
    rank = currency_rows[row_count+1].text
    counter +=1
    name = currency_rows[row_count+1].text
    symbol = currency_rows[row_count+1].text
    price = currency_rows[row_count+2].text



    percent = currency_rows[row_count+4].text

    #new_price = ((((float(price))(float(percent)))/(100)) + (float(price)))


    print(f"Rank: {counter}")
   
    print(f"Currency: {name}")
  
    print(f"Symbol: {symbol}")
   
    print(f"Current Price: {price}")

  
    
    print(f"Percent change over 24 hours: {percent}")
    print()
    print()
    print()
    #print(f"Price changee over 24 hours: {new_price}")

    row_count+=12

    #input()


import keys
from twilio.rest import Client


message1 = (f"{name} has fallen below $40,000")
message2 = (f"{name} has fallen below $3000")
client = Client(keys.accountSID, keys.authToken)

TwilioNumber = '+13236153874'

myCellPhone = "+18502612015"


if price < 40000 and name =="Bitcoin":

    textmessage1 = client.messages.create(to=myCellPhone,from_=TwilioNumber, body=message1)

    print(textmessage1.status)

if price < 3000 and name=="Ethereum":
    textmessage2 = client.messages.create(to=myCellPhone,from_=TwilioNumber, body=message2)
    print(textmessage2.status)

