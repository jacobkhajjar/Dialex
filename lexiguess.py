import streamlit as st
import json

from objects.vowels import Vowel
from guess_lexical_sets import guess_lexical_sets
from build_phone import build_phone

def lexiguess(entry):
    result = []

    # user entry
    entry = entry.lower().split()

    #disable old args
    verbose = False

    # define counters
    word_count = len(entry)
    i = 0
    
    # define dict
    with open("dictionaries/us.json", "r" , encoding="utf-8") as f:
        lookup = json.load(f)

    # loop for each word in entry
    while i < word_count:
        word = entry[i]
        
        # header
        if verbose:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f'\nLexiguessing "{word}" ({i + 1} of {word_count}):\n')

        lexical_sets = []
        override = False
        
        # check if word is in Lexical Set (LS) dict
        
        if not override:
            with open("dictionaries/ls.json", "r") as f:
                ls_dict = json.load(f)
                if word in ls_dict:
                    override = True
                    if verbose:
                        print("LS entry found, overriding other dictionaries.\n")
                    for sets in ls_dict[word]:
                        lexical_sets.append(f"{word}: {", ".join(sets)}")
        
        # check if word is in CMU dict
        try:
            tokens = lookup[word]
        except:
            result.append(f'"{word}" not in CMU dictionary\n')
            i += 1
            continue

        # loop for each homonym found in dict
        homonyms = 0

        while homonyms < len(tokens):
            if verbose:
                print(f"CMU entry found: {tokens[homonyms]}\n")
            
            # convert dict tokens into Phone objects
            phones = []
            for token in tokens[homonyms]:
                new_phone = build_phone(token)
                phones.append(new_phone)

            # guess lexical sets
            if not override:
                lexical_sets = []
                guess_lexical_sets(word, phones, verbose)
            
            transcription = ""
            
            # loop through each phone for final analysis
            for phone in phones:

                # build lexical set list
                if not override:
                    if isinstance(phone, Vowel) and phone.lexical_set not in lexical_sets:
                        lexical_sets.append(phone.lexical_set)
            
            # print results
            if not override:
                if verbose:
                    print(f"Best guess at lexical sets: {", ".join(lexical_sets)}\n")
                else:
                    result.append(f"{word}: {", ".join(lexical_sets)}")
            
            # check for homonyms
            if homonyms != len(tokens) - 1:
                if verbose:
                    print("\n~~~ homonym found, running again ~~~\n")
            homonyms += 1
        
        # increment to check for next word
        i += 1
    
    if override:
        if verbose:
            print("Lexical sets in LS dictionary:")
        result.append("\n".join(lexical_sets))
    
    # footer
    if verbose:
        print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\nLexiguess complete!\n")
    
    return result