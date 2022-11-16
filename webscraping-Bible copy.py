import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request



#webpage = 'https://ebible.org/asv/JHN'
webpage = 'https://biblehub.com/asv/john/2.htm'
#number = random[0,21]


#for numbers in range [0,21]:
    #x = random()

random_chapter = random.randint(1,21)


#if random_chapter < 10:
    #random_chapter = '0' + str(random_chapter)
#else: 
random_chapter = str(random_chapter)



webpage = 'https://biblehub.com/asv/john/' + random_chapter +'.htm'

print(webpage)

#number = (0,21)

#for n in number:
    #if n < 10:
        #webpage = 'https://ebible.org/asv/JHN' +'0'+str(n)+'.htm'
    #if n > 10: 
        #webpage = 'https://ebible.org/asv/JHN'+str(n)+'.htm'
    #print (webpage)


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage = urlopen(req).read()
#print(webpage)
soup = BeautifulSoup(webpage,'html.parser')
page_verses = soup.findAll('span', class_='reftext')
print(page_verses)

for verse in page_verses:
    verse_list =verse.text.split('.')
    #print(verse_list)
    #print(verse.text)


myverse = random.choice(verse_list[:len(verse_list)-5])

print(myverse)

#print(f"Chapter: {random_chapter}, Verse: {myverse}")

message = 'Chapter: ' + random_chapter + ' Verse:' + myverse

print(message)

import keys
from twilio.rest import Client

#TwilioNumber = '+13236153874'

client = Client(keys.accountSID, keys.authToken)

TwilioNumber = '+13236153874'

myCellPhone = "+18502612015"

textmessage = client.messages.create(to=myCellPhone,from_=TwilioNumber, body=message)

print(textmessage.status)
