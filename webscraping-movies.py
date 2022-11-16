
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

print(title.text)

#movie_name = soup.findAll('a',class_='a-link-normal')
#print(str(movie_name))

#table = soup.findAll('tr',class_="a-bordered a-horizontal-stripes a-size-base a-span12 mojo-body-table mojo-table-annotated mojo-body-table-compact scrolling-data-table")
#print(table)

names = soup.findAll('a',class_='a-link-normal')

#print(names)

for name in names:
    name_list =name.text.split('.')
    print(name_list)
    print(name.text)



grosses= soup.findAll('td',class_="a-text-right mojo-field-type-money mojo-estimatable" ) 
#print(grosses)

for gross in grosses:
    gross_list = gross.text.split('.')
    print(gross_list)
    print(gross.text)


total_grosses = soup.findAll('td',class_="a-text-right mojo-field-type-money mojo-estimatable")
#print(total_gross)
for total_gross in total_grosses:
    total_gross_list = total_gross.text.split('.')
    print(total_gross_list)
    print(total_gross.text)

theaters = soup.findAll('td',class_="a-text-right mojo-field-type-positive_integer")
#print(theater)
for theater in theaters:
    theater_list = theater.text.split('.')
    print(theater_list)
    print(theater.text)



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