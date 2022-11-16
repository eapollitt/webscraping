

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


#currency_rows = soup.findAll('td')

currency_rows = soup.findAll('tr')
print(currency_rows.text)



    #name = currency_rows[2].text

    #price = currency_rows[3].text



    #percent = currency_rows[5].text



    #print(name)


    #print(price)



    #print(percent)




   