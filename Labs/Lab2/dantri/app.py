from urllib.request import urlopen
from bs4 import BeautifulSoup #Camel case
import pyexcel

# 1. Download dantri homepage
webpage = urlopen('http://dantri.com.vn/') # Open connection
data = webpage.read()
html_content = data.decode('utf-8')

# 2. Analyze ROI (Region of interest)
# 2.1 Create beautiful soup
soup = BeautifulSoup(html_content, 'html.parser')
# print(soup.prettify) -> lam dep decode
ul = soup.find('ul', 'ul1 ulnew') #find one
li_list = ul.find_all('li')
# print(li_list[0].prettify())

# for li in li_list:
#     print(li.prettify())

#li = li_list[0]
news_list = []

for li in li_list:
    h4 = li.h4 # find('h4')
    a = h4.a # find('a')
    # = a = li.h4.a
    news = {
        'title': a.string,
        'link': 'http://dantri.com.vn' + a['href']
    }
    news_list.append(news)

pyexcel.save_as(records = news_list, dest_file_name = 'dantri.xlsx')


# 3. Extract data from ROI
