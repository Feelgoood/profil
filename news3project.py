import re
from bs4 import BeautifulSoup
import requests
import os
d= os.getcwd()
dir_list = str(os.listdir(d))
print(dir_list)
date_list = re.findall(r'\d{2}.\d{2}.\d{4}', dir_list)
print(date_list)
page = requests.get ("http://classic.newsru.com/arch/")
parsed = BeautifulSoup(page.content,'html.parser')
date_arch = parsed.find_all("a", class_="arch-item-date")
#pagelinks_clear1 = [i['href'] for i in date_arch]
for i in date_arch:
    page_day = requests.get("http://classic.newsru.com" + i['href'])
    print(i)
    date=(i.get_text())
    ii=str(i.get_text())
    if date not in os.listdir(d):
        os.mkdir(d+"/"+ii)
        link=str(i['href'])
        print (link)
        page_day = requests.get("http://classic.newsru.com" + link)
        parsed_day = BeautifulSoup(page_day.content, 'html.parser')
        link_get = parsed_day.find_all("a", class_="explaincolumn")
        pagelinks_clear = [l['href'] for l in link_get]
        for iii in pagelinks_clear:
            print(iii)
            page_iii = requests.get("http://classic.newsru.com"+iii)
            parsed_iii = BeautifulSoup(page_iii.content,'html.parser')
            all_function = parsed_iii.find_all('script')
            for a in all_function:
                a.decompose()
            page_text = parsed_iii.find('p')
            page_text_clear = page_text.get_text()
            with open(d+"/"+ date + "/"+ iii.replace("/", ".") + '.txt', 'w') as openfile:
                try:
                    openfile.write(page_text_clear)
                except UnicodeEncodeError:
                    continue

# pagelinks_clear = [l['href'] for l in date_arch]
#     for l in pagelinks_clear:
#     pagelinks_clear_1.append(1['href'])
#     for i in pagelinks_clear:
#     print(i)
#     my_files = os.listdir('.')
#
# for i in pagelinks_clear:
#     page_i = requests.get("http://classic.newsru.com"+i)
#     parsed_i = BeautifulSoup(page_i.content,'html.parser')
#     all_function = parsed_i.find_all('script')
#     for a in all_function:
#         a.decompose()
#     page_text = parsed_i.find('p')
#     page_text_clear = page_text.get_text()
#     with open(i.replace("/", ".") + '.txt', 'w') as openfile:
#         openfile.write(page_text_clear)


#print(parsed.prettify())
#pagelinks = parsed.find_all("a", class_="explaincolumn")
#for i in pagelinks:
   # print(i['href'])
#pagelinks_clear = [i['href'] for i in pagelinks] # это сокращенная формула добавления i в лист