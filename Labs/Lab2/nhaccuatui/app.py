# html = beautiful soup, html ajax = selenium
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

raw_data = urlopen('https://www.nhaccuatui.com/').read()

# cách để get data thành html file về máy
# file = open('nct.html', 'wb') # w = write, b = binary (raw)
# file.write(raw_data)
# file.close()

html_content = raw_data.decode('utf-8')
soup = BeautifulSoup(html_content, 'html.parser')
div = soup.find('div', 'list_chart_music')
ul = div.find('ul')
li_list = ul.find_all('li')

songs_list = []
for li in li_list:
    name = li.div.h3.a
    h4 = li.div.h4
    authors = h4.find_all('a')
    tac_gia = ''
    for author in authors:
        tg = author.string
        tac_gia += tg + ', '
    tac_gia = tac_gia[:-2]
    songs = {
        'name': name.string,
        'author': tac_gia
    }
    songs_list.append(songs)

print(songs_list)
pyexcel.save_as(records = songs_list, dest_file_name = 'nhaccuatui.xlsx')
