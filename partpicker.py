#partpicker.py
#%%
import bs4 
import urllib
import json

def getpageFromWebsite(website, partname, timeout = 500):
    fullpath = website + urllib.parse.quote(partname)
    loaded_page = urllib.request.urlopen(fullpath, timeout=timeout)
    loaded_page = loaded_page.read()
    soup = bs4.BeautifulSoup(loaded_page, 'html.parser')
    return soup
def parseDrom(soup):
    part_frames = [x for x in soup.find_all(class_ = 'descriptionCell bull-item-content__cell bull-item-content__description-cell js-description-block')]
    part_names = [x.find_all(class_ = 'bulletinLink bull-item__self-link auto-shy')[0].get_text() for x in part_frames]
    part_links = ['https://baza.drom.ru' + x.find_all(class_ = 'bulletinLink bull-item__self-link auto-shy')[0]['href'] for x in part_frames ]
    part_price = [x.find_all(class_ = 'price-block__price')[0].get_text() \
    if len(x.find_all(class_ = 'price-block__price')) > 0 \
        else x.find_all(class_ = 'price-block__final-price finalPrice tooltip-element tooltip-s')[0].get_text() \
    for x in part_frames]
    return zip(part_names, part_links, part_price)
def parseAuto(soup):
    part_frames = [x for x in soup.find_all(class_ = 'SerpSnippet__data')]
    part_names = [x.find_all(class_ = 'PartsLink PartsLink_color_black PartsLink_padded SerpSnippet__title')[0].get_text() for x in part_frames]
    part_links = ['https://baza.drom.ru' + x.find_all(class_ = 'PartsLink PartsLink_color_black PartsLink_padded SerpSnippet__title')[0]['href'] for x in part_frames ]
    part_price = [x.find_all(class_ = 'SerpSnippet__price')[0].get_text() for x in part_frames]
    return zip(part_names, part_links, part_price)
def getPriceInfo(request_parameters):
    req = json.loads(request_parameters)
    part_name = req['part_name']
    page = req['page']
    webpages = [r'https://parts.auto.ru/zapchasti/?isNew=all&text=', r'https://baza.drom.ru/sell_spare_parts/?query=']
    parts = []
    for page in webpages:
        soup = getpageFromWebsite(page)
        parts += [parseWebpage(soup)]
    result = []
    
def parseWebpage(soup):
    if len(soup.findall(class_ = 'js no-main0 drom-notouch')) > 0:
        part_frames = [x for x in soup.find_all(class_ = 'descriptionCell bull-item-content__cell bull-item-content__description-cell js-description-block')]
        part_names = [x.find_all(class_ = 'bulletinLink bull-item__self-link auto-shy')[0].get_text() for x in part_frames]
        part_links = ['https://baza.drom.ru' + x.find_all(class_ = 'bulletinLink bull-item__self-link auto-shy')[0]['href'] for x in part_frames ]
        part_price = [x.find_all(class_ = 'price-block__price')[0].get_text() \
        if len(x.find_all(class_ = 'price-block__price')) > 0 \
            else x.find_all(class_ = 'price-block__final-price finalPrice tooltip-element tooltip-s')[0].get_text() \
        for x in part_frames]
        return zip(part_names, part_links, part_price)
    else:
         part_frames = [x for x in soup.find_all(class_ = 'SerpSnippet__data')]
        part_names = [x.find_all(class_ = 'PartsLink PartsLink_color_black PartsLink_padded SerpSnippet__title')[0].get_text() for x in part_frames]
        part_links = ['https://baza.drom.ru' + x.find_all(class_ = 'PartsLink PartsLink_color_black PartsLink_padded SerpSnippet__title')[0]['href'] for x in part_frames ]
        part_price = [x.find_all(class_ = 'SerpSnippet__price')[0].get_text() for x in part_frames]
        return zip(part_names, part_links, part_price)
#%%





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
part_frames = [x for x in soup.find_all(class_ = 'descriptionCell bull-item-content__cell bull-item-content__description-cell js-description-block')]
part_names = [x.find_all(class_ = 'bulletinLink bull-item__self-link auto-shy')[0].get_text() for x in part_frames]
part_links = ['https://baza.drom.ru' + x.find_all(class_ = 'bulletinLink bull-item__self-link auto-shy')[0]['href'] for x in part_frames ]
part_price = [x.find_all(class_ = 'price-block__price')[0].get_text() \
    if len(x.find_all(class_ = 'price-block__price')) > 0 \
        else x.find_all(class_ = 'price-block__final-price finalPrice tooltip-element tooltip-s')[0].get_text() \
    for x in part_frames]
#%%
#%%
a = part_frames[0].find_all(class_ = 'bulletinLink bull-item__self-link auto-shy')[0].get_text()
b = part_frames[0].find_all(class_ = 'price-block__price')[0].get_text()
c 
#%%
soup = getpageFromWebsite('https://parts.auto.ru/zapchasti/?isNew=all&text=', 'зеркало')
#%%
