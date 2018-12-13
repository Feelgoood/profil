import os
import re
d= os.getcwd()
dir_list = str(os.listdir(d))
print(dir_list)
date_list = re.findall(r'\d{2}.\d{2}.\d{4}', dir_list)
print(date_list)
import pymorphy2
import nltk
from string import punctuation
from nltk.corpus import stopwords
from pymorphy2 import MorphAnalyzer
from nltk import bigrams
from nltk import trigrams
from nltk import ngrams
nltk.download('stopwords')
nltk.download('punkt')
morph = MorphAnalyzer()
punct = punctuation+'«»—…“”*№–'
stops = stopwords.words('russian')
from nltk.tokenize import word_tokenize
#вот так можно расширить стоп-слова
stops.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', 'к', 'на', 'хоть', 'после', 'год', 'ноябрь', '2018', '2019', 'декабрь', 'январь', 'февраль' , 'март' , 'апрель', 'май' , 'июнь', 'июль'])
def normalize(text):
    words = [word.strip(punct) for word in word_tokenize(text.lower())]
    words = [morph.parse(word)[0].normal_form for word in words]
    words = [word for word in words if word not in stops]
    words = list(filter(None,words))
    #return ' '.join(words)
    return words

#n = 6
#sixgrams = ngrams(text.split(), n)

#for grams in sixgrams:
#  print grams
for i in date_list:
    with open(d + '/' + i + '/' +i + '.txt', 'r') as openfile:
        contents = openfile.read()
        contents_normalised = normalize(contents) # лематизация см функция выше
        tokenized = contents_normalised #
        bigrams = list(nltk.bigrams(tokenized)) #
        freqdict = {i:bigrams.count(i) for i in set (bigrams)} # составляем словарь ключ- биграма и значение - количество уникальных биграм
        sorted_freq = sorted(freqdict.items(), key=lambda items: items[1], reverse=True) #
        print(sorted_freq)
        sorted_str = str(sorted_freq)
        with open (d + '/' + i + '/' +i + 'frq' + '.txt','w') as out:
            out.write(sorted_str)