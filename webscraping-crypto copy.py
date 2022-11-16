

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



row_count = 1
for x in range(1,50):
    #td = currency_rows[x]
    name = currency_rows[row_count+1].text

    price = currency_rows[row_count+2].text



    percent = currency_rows[row_count+4].text



    print(f"Currency: {name}")


    print(f"Current Price: {price}")



    print(f"Percent change over 24 hours: {percent}")

    row_count+=11

    #input()




   