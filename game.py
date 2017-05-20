#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Word Cookies game Cheat with python Edit

https://ahmadly.com

"""
import pickle

all_words = pickle.load(open('all_words.pickle', 'rb'))


def seek_word(words: set):
    for word in words:
        yield word


while True:
    try:
        get_char = input('\nenter chars:').strip().split()
        for item in seek_word(all_words):
            if 2 <= len(item) <= len(get_char):
                valid = 0
                for char in item:
                    if char in get_char:
                        if item.count(char) == 1:
                            valid += 1
                if len(item) == valid:
                    print(item, end=', ')
    except KeyboardInterrupt:
        print('\nbye !')
        exit(0)
