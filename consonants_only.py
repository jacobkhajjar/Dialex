import json
from objects.consonants import Consonant, Action
from objects.vowels import Vowel
from build_phone import build_phone

def lexiguess(word):
    
    # define dict
    with open("dictionaries/us.json", "r" , encoding="utf-8") as f:
        lookup = json.load(f)

    consonant_sets = []
    
    # check if word is in CMU dict
    try:
        tokens = lookup[word]
    except:
        return "NOT_IN_CMU_DICT"

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

        guess_consonants(phones)
        
        # loop through each phone for final analysis
        for phone in phones:

            if isinstance(phone, Consonant) and phone.lexical_set and phone.lexical_set not in consonant_sets:
                consonant_sets.append(phone.lexical_set)
        
        homonyms += 1

    consonants = " ".join(consonant_sets)

    return consonants

def guess_consonants(phones):
    
    # loop over each phone
    for i, phone in enumerate(phones):

        
        if isinstance(phone, Vowel):
            continue
        elif phone.arpa not in ("TH", "DH", "L", "T", "NG", "R", "HH"):
            continue

        # define first / previous
        first = (i == 0)
        
        if not first:
            prev = phones[i - 1]
        else:
            prev = None

        # define next / last
        if i < len(phones) - 1:
            next = phones[i + 1]
            last = False
        else:
            next = None
            last = True

        consonant: Consonant = phone

        #CONSONANTS

        match consonant.arpa:

            case "TH":
                consonant.lexical_set = "THINK"
            
            case "DH":
                consonant.lexical_set = "THIS"

            case "L":
                if next and (isinstance(next, Vowel) or next.arpa == "Y"):
                    consonant.lexical_set = "LOOK"
                else:
                    consonant.lexical_set = "RAIL"

            case "T":
                if last:
                    consonant.lexical_set = "GET"
                if prev and next and isinstance(prev, Vowel) and isinstance(next, Vowel) and not next.is_stressed:
                    consonant.lexical_set = "WATER"
            
            case "NG":
                if not next or next.arpa != "K":
                    consonant.lexical_set = "TALKING"

            case "R":
                if next and isinstance(next, Vowel):
                    consonant.lexical_set = "RUN"
            
            case "HH":
                consonant.lexical_set = "HOUSE"

    return