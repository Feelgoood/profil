import os
import nltk
from nltk.corpus import stopwords
import csv
import re
import pymorphy2
import nltk
from string import punctuation
from nltk.corpus import stopwords
from pymorphy2 import MorphAnalyzer

d = 'C:\\test programm\\Тексты'
name_list = os.listdir(d)
#data = {}
# poets = {'Пушкин': {'sent':10, 'words':100, 'soyuz':300},
#         'Лермонов':{'sent':16, 'words':190, 'soyuz':300}}
authors_list = os.listdir(d)
#print(authors_list)

#date_list = re.findall(r'\d{2}.\d{2}.\d{4}', dir_list)

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
stops.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', 'к', 'на', 'хоть', 'после'])


def normalize(text):
    words = [word.strip(punct) for word in word_tokenize(text.lower())]
    words = [morph.parse(word)[0].normal_form for word in words]
    words = [word for word in words if word not in stops]
    words = list(filter(None,words))
    #return ' '.join(words)
    return words
#
# for i in authors_list:
#     print(i)
#     a= os.listdir(d+'/'+i)
#     print(a)
#     a= str(a)
#     a=a.replace("'",'')
#     a=a.replace("[","")
#     a=a.replace(']','')
#     print(a)
#     with open(d + '/'+i +'/' + a, 'r', encoding='UTF-8') as openfile:
#         contents = openfile.read()
#         contents_normalised = normalize(contents) # лематизация см функция выше
#         tokenized = contents_normalised #
#         bigrams = list(nltk.bigrams(tokenized)) #
#         freqdict = {i:bigrams.count(i) for i in set (bigrams)} # составляем словарь ключ- биграма и значение - количество уникальных биграм
#         sorted_freq = sorted(freqdict.items(), key=lambda items: items[1], reverse=True) #
#         #print(sorted_freq)
#         sorted_str = str(sorted_freq)
#         with open (d + '/' + i + '/' +a + 'frq' + '.txt','w',encoding="UTF-8") as out:
#             out.write(sorted_str)

def get_author (d):
    data = {}
    author_list = os.listdir(d)
    for i in author_list:
        data[i] = {}
    return data

# 1 среднее количество слов в преложениии = количество слов в предложении / количество предложений
def preprocess_sents(document):
    sentences = nltk.sent_tokenize(document)
    sentences=[i.replace('\ufeff','') for i in sentences]
    sentences = [i.replace('\n', '') for i in sentences]
    stop_words = stopwords.words('russian')
    stop_words.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', '—', 'к', 'на'])
    words = sum(1 for sent in sentences
                for word in nltk.word_tokenize(sent)
                if word not in stop_words)
    cnt = 0
    for sent in sentences:
        cnt += 1
       #print('[{}]{}'.format(cnt, sent))
    #print(sentences)
    return words/len(sentences)


# средняя длина слов =  количесто букв / количество слов
def preprocess_words(document):
    sentences = nltk.sent_tokenize(document)
    stop_words = stopwords.words('russian')
    stop_words.extend(['и', ''])
    words = sum(1 for sent in sentences
                for word in nltk.word_tokenize(sent)
                if word not in stop_words)
    letters= ' '.join(sentences)
    words = letters.replace(' '' ','').split(' ')
    #print(words)
    lengthlist = [len(i) for i in words]

    return sum(lengthlist)/len(lengthlist)

def count_words(name_list):
    words_dict={}
    for i in name_list:
        title = os.listdir(d+'/'+i)
        for n in title:
           # print('N=',n)
            with open(d+ '/'+i+'/'+n, 'r', encoding='UTF-8') as out:
                document=out.read()
                words = preprocess_words(document)
                words_dict[i] = words
    return words_dict

#print("words=", preprocess_words(d))

data = get_author(d)
#print(data)


def count_sents(name_list):
    sent_dict={}
    for i in name_list:
        title = os.listdir(d+'/'+i)
        for n in title:
           # print('N=',n)
            with open(d+ '/'+i+'/'+n, 'r', encoding='UTF-8') as out:
                document=out.read()
                sent = preprocess_sents(document)
                sent_dict[i] = sent
    return sent_dict

def preprocess_conj(document):
    sentences = nltk.sent_tokenize(document)
    sentences = [words.replace("\n", " ") for words in sentences]
    punct = punctuation + '«»—…“”*№–'
    stop_words = stopwords.words('russian')
    words = [word for sent in sentences
        for word in nltk.word_tokenize(sent)
        if word not in stop_words
        and word != "1" and word.strip(punct)!= '']
    words = [word.lower() for word in words]
    morph = MorphAnalyzer()
    words_tags = [morph.parse(word)[0].tag.POS for word in words]
    cnt_tags=0
    for tag in words_tags:
        if tag=="CONJ":
            cnt_tags= cnt_tags+ 1
    words = sum(1 for word in words)
    conj_percent = float('{:.4f}'.format(cnt_tags/words*100))
    return conj_percent

def count_conj(name_list):
    conj_dict={}
    for i in name_list:
        title = os.listdir(d+'/'+i)
        for n in title:
           # print('N=',n)
            with open(d+ '/'+i+'/'+n, 'r', encoding='UTF-8') as out:
                document=out.read()
                conj = preprocess_conj(document)
                conj_dict[i] = conj
    return conj_dict


sum_dict = zip_dictionaries(result, result_w, result_c,result_m)
sum_sum=[]
def get_sum (dictionary):
    for t in dictionary.keys():
        for i in dictionary.values():
            a = 0
            cnt = 0
            for n in i.values():
                #print(n)
                a=a+n
                # print(a)
                cnt+=1
                sum=a/cnt
            sum_sum.append(sum)
        return sum_sum
get_sum(sum_dict)

# middle = get_sum(sum_dict)

def count_middle(name_list):
    middle_dict={}
    for i in name_list:
        title = os.listdir(d+'/'+i)
        for n in title:
                middle = get_sum(sum_dict)
                middle_dict[i] = middle
    return middle_dict

print(sum_dict)




def zip_dictionaries(first_dict, second_dict, third_dict, forth_dict):
    dict_={}
    for key, value in first_dict.items():
        dict_[key] = {'sent': value, 'words':second_dict[key], 'conj': third_dict[key],'middle': forth_dict[key]}
    return dict_


result=count_sents(name_list)
result_w=count_words(name_list)
result_c=count_conj(name_list)
result_m=count_middle(data)
#print(result)
# k=1

data=zip_dictionaries(result, result_w, result_c, result_m)
zip_dictionaries(result, result_w, result_c,result_m)

def save_file_(csvfile, content):
    with open(csvfile, 'w') as savefile:
        for i in content.keys():
            strtowrite=[i,str(content[i]['sent']),str(content[i]['words']),str(content[i]['conj'], str(content[i]['middle']))]
            # strtowrite = str(strtowrite)
            savefile.write(','.join(strtowrite))
            savefile.write('\n')

save_file_('result.csv', data)


