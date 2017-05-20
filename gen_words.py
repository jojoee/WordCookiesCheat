#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

reading big text file sample
https://ahmadly.com

"""
import glob
import multiprocessing
import pickle


def read_files_list(file_list: list):
    for get_file in file_list:
        yield get_file


def read_file(file_name: str):
    for line in open(file_name).readlines():
        yield line


all_words = set()
with multiprocessing.Pool(8) as pool:
    for file in read_files_list(glob.glob('files/*.txt')):
        for i in read_file(file):
            all_words.add(i.strip().lower())

print(len(all_words))
pickle.dump(all_words, open('all_words.pickle', 'wb'))
