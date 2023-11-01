#!/usr/bin/python
# -*- coding: utf8 -*-
import os, sys

import nltk
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import string


#1 - Сгущенное молоко - Варлам Шаламов
#2 - Мастер и Маргарита - Михаил Булгаков
#3 - Мы - Евгений Замятин

def print_hi():
    # -*- coding: utf-8 -*-
    # nltk.download('punkt')  # скачиваем токенизатор, обязательно при 1 запуске
    # nltk.download('stopwords')  # скачиваем стопслова, обязательно при 1 запуске
    print("Введите номер книги, отрывок которой хотите проанализоровать\n1 : Сгущенное молоко - Варлам Шаламов\n2 : Мастер и Маргарита - Михаил Булгаков\n3 : Мы - Евгений Замятин\n-------------------\n0 : заверешить анализ\n")

    book = input()
    while book!='0':
        text = ''

        f = None
        if book == '1':
            f = open('text.txt', 'r')
        elif book == '2':
            f = open('text1.txt', 'r')
        elif book == '3':
            f = open('text2.txt', 'r')
        elif book =='0' :
            print("Анализ завершен")
            break
        for line in f:
            text = text + line

        print("Вывести анализируемый текст?\n0 : нет\n1 : да")
        if (input() == '1'):
            print(text)

        print(f"Всего символов {len(text)}")
        text = text.lower() #приводим к нижнему регистру
        spec = string.punctuation  # !" #$%&\'()*+,-. /:;<=>? @[\\]^_`{|}~

        text = "".join([ch for ch in text if ch not in spec])  #очищаем строку и добавляем символы, не являющиеся специальными
        text = text.replace('–', '')
        print(f"Без специальных {len(text)}")

        text_tokens = word_tokenize(text) #составляем список слов
        print(f"Слов в тексте {len(text_tokens)}\n")

        toText = nltk.Text(text_tokens)

        fdist = FreqDist(toText)
        print("Популярные слова:")
        print(f"{fdist.most_common(20)}") #список 20-ти наиболее часто встречающихся слов в тексте

        fdist.plot(35, cumulative = False, title='Частотный анализ текста')
        plt.show()#Отображаем график частотных слов

        russian_stopwords = stopwords.words("russian") #определяем стоп-слова, загразняющие анализ

        text_tokens_clear = ([token for token in text_tokens if token not in russian_stopwords]) #убираем стоп-слова
        toTextClear = nltk.Text(text_tokens_clear)
        fdist2 = FreqDist(toTextClear)
        fdist2.plot(25, cumulative=False, title='Частотный анализ текста без стоп-слов')
        plt.show() # Отображаем график частотных слов
        print("Популярные чистые слова:")
        print(f"{fdist2.most_common(20)}")

        print("\nВведите номер книги, отрывок которой хотите проанализоровать\n1 : Сгущенное молоко - Варлам Шаламов\n2 : Мастер и Маргарита - Михаил Булгаков\n3 : Мы - Евгений Замятин\n-------------------\n0 : заверешить анализ\n")
        book = input()

    print('Анализ завершен')

if __name__ == '__main__':
    print_hi()
