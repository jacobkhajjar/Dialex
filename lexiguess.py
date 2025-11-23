import json

from objects.vowels import Vowel
from objects.consonants import Consonant
from guess_lexical_sets import guess_lexical_sets
from build_phone import build_phone

def lexiguess(word):
    
    # define dict
    with open("dictionaries/us.json", "r" , encoding="utf-8") as f:
        lookup = json.load(f)

    vowel_sets = []
    consonant_sets = []
    
    # check if word is in CMU dict
    try:
        tokens = lookup[word]
    except:
        return "NOT_IN_CMU_DICT", "NOT_IN_CMU_DICT", 500, False

    # loop for each homonym found in dict
    homonyms = 0

    homonyms_found = len(tokens) > 1

    while homonyms < len(tokens):
        
        # convert dict tokens into Phone objects
        phones = []
        for token in tokens[homonyms]:
            new_phone = build_phone(token)
            phones.append(new_phone)

        # guess lexical sets

        score = guess_lexical_sets(word, phones)
        
        # loop through each phone for final analysis
        for phone in phones:

            # build lexical set list
            if isinstance(phone, Vowel) and phone.lexical_set not in vowel_sets:
                vowel_sets.append(phone.lexical_set)
            
            if isinstance(phone, Consonant) and phone.lexical_set and phone.lexical_set not in consonant_sets:
                consonant_sets.append(phone.lexical_set)
        
        homonyms += 1

    vowels = " ".join(vowel_sets)
    consonants = " ".join(consonant_sets)

    return vowels, consonants, score, homonyms_found