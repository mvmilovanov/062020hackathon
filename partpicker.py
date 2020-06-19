#partpicker.py
#%%
import bs4 
import urllib
import json

def getpageFromWebsite(website, partname, timeout = 500):
    try:
        fullpath = website + urllib.parse.quote(partname)# '+'.join([urllib.parse.quote(x) for x in partname.lower().strip().split(' ')])
        loaded_page = urllib.request.urlopen(fullpath, timeout=timeout)
        loaded_page = loaded_page.read()
        soup = bs4.BeautifulSoup(loaded_page, 'html.parser')
    except:
        soup = bs4.BeautifulSoup()
    return soup
def parseDrom(soup):
    part_frames = [x for x in soup.find_all(class_ = 'descriptionCell bull-item-content__cell bull-item-content__description-cell js-description-block')]
    part_names = [x.find_all(class_ = 'bulletinLink bull-item__self-link auto-shy')[0].get_text() for x in part_frames]
    part_links = ['https://baza.drom.ru' + x.find_all(class_ = 'bulletinLink bull-item__self-link auto-shy')[0]['href'] for x in part_frames ]
    part_price = [x.find_all(class_ = 'price-block__price')[0].get_text() \
    if len(x.find_all(class_ = 'price-block__price')) > 0 \
        else x.find_all(class_ = 'price-block__final-price finalPrice tooltip-element tooltip-s')[0].get_text() \
    for x in part_frames]
    return part_names #zip(part_names, part_links, part_price)
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
    for webpage in webpages:
        soup = getpageFromWebsite(webpage, part_name)
        parts += [parseWebpage(soup)]
    # return parts
    result = []
    entries = max([len(x) for x in parts])
    step = len(webpages)*3
    for i in range(0, int(entries/3)+1, 1):
        for res in parts:
            result += res[i*3:(i+1)*3]
    # print(page*step)
    # print((page+1)*step)
    return result[page*step:(page+1)*step]

def parseWebpage(soup):
    # return(soup)
    try:
        if len(soup.find_all(class_ = 'descriptionCell bull-item-content__cell bull-item-content__description-cell js-description-block')) > 0:
            part_frames = [x for x in soup.find_all(class_ = 'descriptionCell bull-item-content__cell bull-item-content__description-cell js-description-block')]
            part_names = [x.find_all(class_ = 'bulletinLink bull-item__self-link auto-shy')[0].get_text() for x in part_frames]
            part_links = ['https://baza.drom.ru' + x.find_all(class_ = 'bulletinLink bull-item__self-link auto-shy')[0]['href'] for x in part_frames ]
            part_price = [x.find_all(class_ = 'price-per-quantity__price')[0].get_text() \
            if len(x.find_all(class_ = 'price-per-quantity__price')) > 0 \
            else (x.find_all(class_ = 'priceCell price-block')[0].get_text() \
                if len(x.find_all(class_ = 'priceCell price-block')) > 0 \
                else x.find_all(class_ = 'price-block__final-price finalPrice deal-price-without-discount')[0].get_text())
            for x in part_frames]
        else:
            part_frames = [x for x in soup.find_all(class_ = 'SerpSnippet__data')]
            part_names = [x.find_all(class_ = 'PartsLink PartsLink_color_black PartsLink_padded SerpSnippet__title')[0].get_text() for x in part_frames]
            part_links = [x.find_all(class_ = 'PartsLink PartsLink_color_black PartsLink_padded SerpSnippet__title')[0]['href'] for x in part_frames ]
            part_price = [x.find_all(class_ = 'SerpSnippet__price')[0].get_text() for x in part_frames]
        return list(zip(part_names, part_links, part_price))
    except:
        return []
#%%

#для тестирования
req = '{"part_name":"дверца бензобака", "page":0}'

get_res = getPriceInfo(req)
#%%