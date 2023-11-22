# webs-scraping notes

os.system("pip install requests")
os.system("pip install lxml")
os.system("pip install bs4")
os.system("pip install beautifulsoup4")

ws1 = "https://en.wikipedia.org/wiki/Jonas_Salk"
ws2 = "https://www.example.com"

import requests

res = requests.get(ws2)

type(res)
res.text

import bs4

soup = bs4.BeautifulSoup(res.text, "lxml")

title_tag = soup.select('title')
title_tag[0]
type(title_tag[0])

title_tag[0].getText()

soup.select('h1')
soup.select('h1')[0].getText()


bs4.BeautifulSoup(requests.get(ws1).text, "lxml").select('title')[0].getText()
bs4.BeautifulSoup(requests.get(ws1).text, "lxml").select('h3')[0].getText()


soup.select('p')

bs4.BeautifulSoup(requests.get(ws1).text, "lxml").select('p')[4]

res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(res.text, "lxml")
soup.select(".toctext")

#-- image

res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text, 'lxml')
image_info = soup.select('.mw-file-description')
soup.select('img')

len(image_info)
computer = image_info[0]
type(computer)
computer['class']
computer['href']
computer['src']

c2 = computer.select('.mw-file-element')
c3 = c2[0]['src']

image_link = requests.get(f'https:{c3}')
image_link.content

f = open('my_new_file_name.jpg', 'wb')
f.write(image_link.content)
f.close()

#----------------------------------
#https://toscrape.com/
#http://books.toscrape.com/

# Goal: get title of every book that has a 2-star rating

import requests
import bs4

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
base_url.format('20')

res = requests.get(base_url.format('1'))
soup = bs4.BeautifulSoup(res.text, 'lxml')
soup.select('.product_pod')
soup.select('.star-rating Two')

products = soup.select(".product_pod")
example = products[0]
example.attrs
list(example.children)
example.select('.star-rating.Three')
example.select('.star-rating.Two')
example.select('a')
example.select('a')[1]
example.select('a')[1]['title']



two_star_titles = []

for n in range(1, 51):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select(".product_pod")
    
    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            two_star_titles.append(book.select('a')[1]['title'])

two_star_titles
len(two_star_titles)

# Web scraping exercises
import requests
import bs4

base_url = 'http://quotes.toscrape.com/'

res = requests.get(base_url)
soup = bs4.BeautifulSoup(res.text, 'lxml')

xx = soup.select('.author')[0]
xx['author']
xx.attrs['itemprop']
aut = list(xx.children)


alist = []
qlist = []
obj = soup.select('.author')
obj_len = len(obj)
for i in range(0, obj_len):
    alist.append(list(soup.select('.author')[i].children)[0])
    alist.sort()
    qlist.append(list(soup.select('.quote')[i].select('.text')[0].children)[0])
    qlist.sort()

authors = set(alist)
quotes = qlist

xx = soup.select('.quote')[0].select('.text')[0]
type(xx)
xx.attrs
list(xx.children)[0]


soup.select('h2')
soup.select('.tag-item').select('a')
list(soup.select('.tag-item')[0].select('a')[0].children)[0]

x3 = [x for list(soup.select('.tag-item')[x].select('a')[0].children)[0] in range(0, 10)]

tag_list = []
for x in range(0, 10):
    tag_list.append(list(soup.select('.tag-item')[x].select('a')[0].children)[0])
    
tag_list

# Solution
authors = set() 
for name in soup.select(".author"):
    authors.add(name.text)
    
quotes = set() 
for name in soup.select(".text"):
    quotes.add(name.text)

tag_list = set()
for name in soup.select(".tag-item"):
    tag_list.add(name.text)

