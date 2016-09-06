# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 22:22:37 2016

@author: kushan
"""
import itertools

def prepare_list():
    words = open("words","r")
    s_words = [w.lower().strip("\n") for w in words]
    set_words = list(set(s_words))
    ss_words = sorted(set_words)
    list_words = [list(w) for w in ss_words]
    return list_words

def input_word():
    word = input("Enter a word")
    return list(word)
    
def sequence_generator(iterable):
    perms = []
    for i in range(2, len(iterable)+1):
        perms.append(set(itertools.permutations(iterable,i)))
    perms_list = []
    for p in perms:
        for i in p:
            perms_list.append(list(i))
    return perms_list
        
def check_in_dict(word_list, combo_list):
    anagrams = []
    for c in combo_list:
        if(c in word_list):
            anagrams.append(c) 
    return anagrams
    
def list_to_str(anagrams):
    words = []
    for a in anagrams:
        words.append("".join(a))
    return words

w = input_word()
combos = sequence_generator(w)
wordlist = prepare_list()
anagram_list = check_in_dict(wordlist,combos)
anagrams = list_to_str(anagram_list)

print("The list of anagrams is", anagrams)
