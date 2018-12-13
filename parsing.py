from bs4 import BeautifulSoup
import requests
# requsts обращается к серверу чтобы получить информацию
#  нужно установить их речез file - settings - project interpreter - на плюсик нажать и добавить эти пакеты.
page = requests.get ("http://dataquestio.github.io/web-scraping-pages/simple.html")


print(page)
# ответ <Response [200]> значит запрос прошел
#print(page.content)
soup= BeautifulSoup(page.content,'html.parser') # делаем суповой объект
#print(soup.prettify()) # показываем красиво
#print(list(soup.children)) # body и head это дети, показываем все хдетей в виде списка,
soup2=list(soup.children) #дальше идем по списку и достаем нужный элемент
#print(soup2[2]) # достаем второй элемент списка
soup3=list(soup2[2].children) # достаем второй элемент во втором ребенке, идем по списку и после каждой запятой новый элемент списка
print(soup3[3]) # напечатает весь html
print(soup3[3].get_text()) # вытащить текст из элемента без тэгов html
