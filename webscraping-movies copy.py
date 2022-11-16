
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
#import openpyxl as xl
#from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
url = 'https://www.boxofficemojo.com/year/2022/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
#print(webpage)
#req = Request(webpage, headers=headers)
#webpage = urlopen(req).read()
#soup = BeautifulSoup(webpage,'html.parser')

#page = urlopen(webpage)			

#soup = BeautifulSoup(page, 'html.parser')
#print(page)

req = Request(url, headers=headers)

webpage = urlopen(req).read()

#print(webpage)
soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

#print(title.text)


movie_rows = soup.findAll('tr')
for x in range(1,6):
    td = movie_rows[x].findAll('td')
    rank = td[0].text
    movie_name = td[1].text
    theater = int(td[6].text.replace(',',''))
    gross = int(td[7].text.replace(',','').replace('$',''))
    dis = td[9].text

    avg = gross / theater

    print(f"Rank: {rank}")
    print(f"Movie Name: {movie_name}")
    print(f"Total Gross {gross:,.2f}")
    print(f"Distributor: {dis}")
    print(f"Average per theater: {avg:,.2f}")
    print()


#movie_name = soup.findAll('a',class_='a-
#link-normal')
#print(str(movie_name))

#table = soup.findAll('tr',class_="a-bordered a-horizontal-stripes a-size-base a-span12 mojo-body-table mojo-table-annotated mojo-body-table-compact scrolling-data-table")
#print(table)





#movie_ranks = soup.findAll('td',class_='"a-text-right mojo-header-column mojo-truncate mojo-field-type-rank mojo-sort-column"')
#print(movie_ranks)


#<a class="a-link-normal" href="/release/rl2500036097/?ref_=bo_yld_table_1">Top Gun: Maverick</a>
#<td class="a-text-right mojo-header-column mojo-truncate mojo-field-type-rank mojo-sort-column"
 #style="width: 50px; height: 31px; min-width: 50px; min-height: 31px;">1</td>

#webpage = urlopen(req).read()
#print(webpage)
#soup = BeautifulSoup(webpage,'html.parser')
#title = soup.title

#print(title.text)
##
##
##

#rank, movie name, total gross, distributor, average gross per theater
##


#movie_rank = soup.findAll('td',class_="a-text-right mojo-header-column mojo-truncate mojo-field-type-rank mojo-sort-column")

#print(movie_rank)

#movie_ranks = soup.findAll('tr',class_='tbody')
#print(movie_ranks)