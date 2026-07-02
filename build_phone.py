from objects.vowels import vowel_list, Vowel
from objects.consonants import *

def build_phone(token):
    if token[0] in vowel_list:
        new_phone = build_vowel(token)
    else:
        new_phone = build_consonant(token)
    return new_phone

def build_vowel(token):
    arpa = token[:2] # removes stress int

    # check if stressed (default is True)
    if "0" in token:
        is_stressed = False
    else:
        is_stressed = True
    
    vowel = Vowel(arpa, is_stressed)

    return vowel

def build_consonant(token):
    arpa = token

    # check if voiced
    if arpa in unvoiced:
        is_voiced = False
    else:
        is_voiced = True

    # assign action
    if arpa in stops:
        action = Action.STOP
    elif arpa in fricatives:
        action = Action.FRICATIVE
    elif arpa in nasals:
        action = Action.NASAL
    elif arpa in affricates:
        action = Action.AFFRICATE
    elif arpa in liquids:
        action = Action.LIQUID
    elif arpa in semivowels:
        action = Action.SEMIVOWEL

    consonant = Consonant(arpa, is_voiced, action)
   
    return consonant