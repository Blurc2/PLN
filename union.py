#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 15:31:36 2018
PuTO
@author: alan
"""

import nltk
import re
from bs4   import BeautifulSoup
from write import writeList
from compare_lists import compare_lists
 
def get_text_string(fname):
    '''Receives an html file with a Spanish text, deletes html tags, deletes the em-dash character,
    and convert text to lowercase. Returns text as a string.'''
     
    f=open(fname, encoding='latin-1')
    text_string=f.read()
    f.close()
 
    soup = BeautifulSoup(text_string, 'lxml')
    text_string = soup.get_text()
    text_string = text_string.replace('\x97', ' ')
    text_string=text_string.lower()
     
    print('The text in', fname, 'has', len(text_string), 'characters.\n')
    return text_string
 
def get_raw_tokens(text_string):
    '''Receives a text string and returns a list of tokens obtained with nltk.word_tokenize(str).'''
 
    raw_tokens=nltk.Text(nltk.word_tokenize(text_string))
    print('There are', len(raw_tokens), 'raw tokens.\n')
    return raw_tokens
 
def get_clean_tokens(raw_tokens):
    '''Receives a list of raw tokens and returns tokens of letters only.'''
    clean_tokens=[]
    for tok in raw_tokens:
        t=[]
        for char in tok: 
            if re.match(r'[a-záéíóúñüA-ZÁÉÍÓÚÑ]', char):#for Spanish alphabet
                t.append(char)
        letterToken=''.join(t)
        if letterToken !='':
            clean_tokens.append(letterToken)
     
    print('There are', len(clean_tokens), 'clean tokens.\n')
    return clean_tokens
 
def delete_stopwords(fname_stopwords, clean_tokens):
    f=open(fname_stopwords)
    words=f.read()
    stopwords=words.split()
    f.close()
     
    tokens_without_stopwords=[]
    for tok in clean_tokens:
        if tok not in stopwords:
            tokens_without_stopwords.append(tok)
     
    print('There are', len(tokens_without_stopwords), 'tokens without stopwords.\n')
    return tokens_without_stopwords
 
def get_vocabulary(alist):
    vocabulary=sorted(set(alist))
    print('There are', len( vocabulary), 'words in  vocabulary.\n')
    return vocabulary
     
if __name__=='__main__':
    fname='e960401.htm'
    text_string=get_text_string(fname)
    raw_tokens=get_raw_tokens(text_string)
    clean_tokens=get_clean_tokens(raw_tokens)
    #writeList(clean_tokens, 'e960401_clean_tokens.txt')
     
    fname_stopwords='stopwords_es.txt'
    tokens_without_stopwords=delete_stopwords(fname_stopwords, clean_tokens)
     
    vocabulary=get_vocabulary(tokens_without_stopwords) 
    print(str(len(vocabulary)))
     
    #difference=compare_lists(raw_tokens, clean_tokens)
    #writeList(sorted(difference), 'e960401_difference.txt')
