from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

html_content = urlopen('https://www.apple.com/itunes/charts/songs/').read().decode('utf-8')
soup = BeautifulSoup(html_content, 'html.parser')

section = soup.find('section', 'section chart-grid')
ul = section.div.find('ul')
li_list = ul.find_all('li')

songs_list = []
for li in li_list:
    name = li.h3.a
    author = li.h4.a
    songs = {
        'name': name.string,
        "author": author.string
    }
    songs_list.append(songs)

print(songs_list)
# pyexcel.save_as(records = songs_list, dest_file_name = 'itunes_top_songs.xlsx')

options = {
    'default_search': 'ytsearch',
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
for song in songs_list:
    music = song['name'] + ' - ' + song['author']
    dl.download([music])
