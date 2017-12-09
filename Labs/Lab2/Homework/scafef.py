from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

html_content = urlopen('http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn').read().decode('utf-8')
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('table', id='tableContent')
trs = table.find_all('tr')
data = []

for tr in trs:
    tds = tr.find_all('td')
#     # for td in tds:
#     #     if td.string != None:
    if tds != []:
        name = {
            'title': tds[0].string,
            'Quy 4': tds[1].string,
            'Quy 1': tds[2].string,
            'Quy 2': tds[3].string,
            'Quy 3': tds[4].string
        }
        data.append(name)
print(data)
pyexcel.save_as(records = data, dest_file_name = 'scafef_vnm.xlsx')
