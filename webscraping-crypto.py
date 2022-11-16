#Find a 'scrappable' cryptocurrencies website where you can scrape the top 5 cryptocurrencies 
# and display as a formatted output one currency at a time. The output should display the name of the currency, 
# the symbol (if applicable), the current price and % change in the last 24 hrs and corresponding price 
# (based on % change)

#Furthermore, for Bitcoin and Ethereum, the program should alert you via text if the value falls below 
# $40,000 for BTC and $3,000 for ETH.

#Submit your GitHub URL which should contain all the files worked in class as well as the above.

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
length = len(currency_rows)
#print(length)
#print(currency_rows[3])
#for x in range(1,6):
#td = currency_rows.findAll('p')

#print(td)


#currency_rows[3] = current_price
#currency_rows[2] = rank and name?

#current_price = currency_rows[3].text
#print(current_price)

name = currency_rows[2].text
#row2 = currency_rows[2]
#print(name)
#print(row2)
price = currency_rows[3].text
#print(price)
price_int = currency_rows[3].text.replace(',','').replace('$','')

percent = currency_rows[5].text
#print(percent)
int_percent = currency_rows[5].text.replace('%','')

new_price = ((((price_int)(int_percent))/(100)) + (price_int))
#print(new_price)
#for record in row2:
    #Name = record.findAll('p', class_='div')
    #namee = record[0].text
    #print(namee)
print(name)
#print(row2)

print(price)



print(percent)


print(new_price)

    #print(Rank)
    #ranks = name.findAll('p', class_='div')
    #rankss = ranks[0].text
    #names = record[0]
    #print(names)
    #print(record)
#ranks= rank.textsplit()
#print(name)
#FIGURE OUT HOW TO SPLIT THE TEXT





#soups = soup.findAll('p')
#print(soups.text)

#allText = soup.find(id="title",class="text")
#tablecells = soup.findAll('td', class_='tr')
#print(tablecells)

#statsContainer = soup.find_all("tr", class_= "tbody")
#for s in statsContainer:
    #statsValue = s.find_all("td", class_="tr")
    #print(statsValue)


#test = soup.findAll("table", class_="sc-853bfcae-2 eVOXbZ cmc-table  ")

#for x in test:
    #y = soup.findAll('tr', class_='tbody')
    #for z in y:
        #w = soup.findAll('td', class_='tr')
        #print(w)



#print(test)

#>>> type(table)
#<class 'bs4.element.ResultSet'>
#>>> type(table[0])
#<class 'bs4.element.Tag'>
#>>> len(table[0].find_all('tr'))






#tablecells = soup.find("td", {"class":"tr"})
#print(tablecells)
#movie_rows = soup.findAll('tr')
#for x in range(1,6):
    #td = movie_rows[x].findAll('td')
    #rank = td[0].text
    #movie_name = td[1].text


    #print(f"Theater: {theater}")

#print(tablecells[0].text)
#print(tablecells[1].text)
#print(tablecells[3].text)
#print(tablecells[5].text)
#print(tablecells[6].text)

#page_verses = soup.findAll('tr')
#for x in page_verses:
    #idk = page_verses[x].findALL('td')
    #idk1 = idk.text
    #print(idk1)
    #print(idk)

#print(page_verses)
#print(title.text)


#coin_rows = soup.findAll('td')
#coin_rows = soup.findAll('td')
#for x in range(1,6):
    #div = coin_rows[x].findAll('p')
    #rank = div[0].text
    #dictionary = {rank}
    #print(dictionary)
    #print(rank)
    #print(div)
    #List = list(div[0])
    #print(List)
    #print(List[0])
    #List2 = list(List)
    #print(List2)
    #Dict = div.dict
    #print(Dict)
    #rank = div[0].text
    #currency_name = div[1].text
    #theater = int(td[6].text.replace(',',''))
    #gross = int(td[7].text.replace(',','').replace('$',''))
    #dis = td[9].text

    #avg = gross / theater

    #print(f"Rank: {rank}")

#symbol: 

#page_verses = soup.findAll('p', class_='div')
#print(page_verses)

#for verse in page_verses:
    #verse_list =verse.text.split('.')

#current price


#percent change in the last 24 hours



#corresponding price


    #print(f"Name: {rank}")
    
    #print(f"Name: {currency_name}")
    #print(f"Total Gross {gross:,.2f}")
    #print(f"Distributor: {dis}")
    #print(f"Average per theater: {avg:,.2f}")
   # print()
