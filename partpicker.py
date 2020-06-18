#partpicker.py
#%%
import bs4 
import urllib

def getPartsFromWebsite(partname, timeout = 500):
    website = r'https://baza.drom.ru/sell_spare_parts/?query='
    fullpath = website + partname
    loaded_page = urllib.request.urlopen(fullpath)
    loaded_page = loaded_page.read()
    soup = bs4.BeautifulSoup(loaded_page, 'html.parser')
#%%
website = r'https://baza.drom.ru/sell_spare_parts/?query='
fullpath = website + urllib.parse.quote('Зеркало')
loaded_page = urllib.request.urlopen(fullpath)
loaded_page = loaded_page.read()
soup = bs4.BeautifulSoup(loaded_page, 'html.parser')
#%%
part_names = [x.get_text() for x in soup.find_all(class_ = 'bulletinLink bull-item__self-link auto-shy')]
part_links = ['https://baza.drom.ru' + x['href'] for x in soup.find_all(class_ = 'bulletinLink bull-item__self-link auto-shy') ]
part_price = [x.get_text() for x in soup.find_all(class_ = 'price-block__final-price finalPrice tooltip-element tooltip-s')]
#%%
a[1].get_text()