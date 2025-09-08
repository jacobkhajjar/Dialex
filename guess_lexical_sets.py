import json
import re
from objects.consonants import Consonant, Action
from objects.vowels import Vowel

def guess_lexical_sets(word, phones):
    
    # loop over each phone
    for i, phone in enumerate(phones):
        
        # skip consonants
        if isinstance(phone, Vowel):
            vowel = phone
        else:
            continue

        # define first
        first = (i == 0)

        # define next / last
        if i < len(phones) - 1:
            next = phones[i + 1]
            last = False
        else:
            next = None
            last = True
            
        # begin logic based on CMU ARPA
        match vowel.arpa:
    
    # LOT/START/PALM - COMPLETE - can split based on MFA dict but LOT/PALM often ambiguous
            case "AA":
                if next and next.arpa == "R":
                    vowel.lexical_set = "START"
                elif last:
                    vowel.lexical_set = "PALM"
                elif not isinstance(next, Consonant):
                    vowel.lexical_set = "PALM"
                else:
                    vowel.lexical_set = check_uk_dict(word, phones, vowel, next) # type: ignore
                
                if vowel.lexical_set == "ambiguous LOT or PALM":
                    if re.search(r"ot|otch", word):
                        vowel.lexical_set = "LOT"
                    elif re.search(r"al", word):
                        vowel.lexical_set = "PALM"
            
            # TRAP/BATH - COMPLETE
            case "AE":

                # check if BATH is possible in spelling
                if next and isinstance(next, Consonant):
                    possible_bath = False
                    if next.action == Action.FRICATIVE:
                        if not next.is_voiced or next.arpa in ("DH", "V", "Z"):
                            possible_bath = True
                    elif next.action == Action.NASAL:
                        possible_bath = True
                    elif next.arpa == "L":
                        possible_bath = True

                    # if could be BATH, check MFA dict
                    if possible_bath:
                        vowel.lexical_set = check_uk_dict(word, phones, vowel, next) # type: ignore
                    else:
                        vowel.lexical_set = "TRAP"

                else:
                    raise Exception("expected consonant after AE vowel")
                
                # check for TRAM/DANCE
                if next.action == Action.NASAL:
                    if vowel.lexical_set == "TRAP":
                        vowel.lexical_set += "/TRAM"
                    elif vowel.lexical_set == "BATH":
                        vowel.lexical_set += "/DANCE"
                    else:
                        vowel.lexical_set = "ambiguous TRAP/TRAM or BATH/DANCE"


            # STRUT - COMPLETE
            case "AH":
                if vowel.is_stressed:
                    vowel.lexical_set = "STRUT"
                else:
                    vowel.lexical_set = "commA"
            
            # THOUGHT/CLOTH/NORTH/FORCE -
            case "AO":
                if next and isinstance(next, Consonant):
                    if word == "chocolate":
                        vowel.lexical_set = "CLOTH"
                    if next.arpa == "NG":
                        vowel.lexical_set = "CLOTH"
                    elif next.action == Action.FRICATIVE and next.is_voiced:
                        vowel.lexical_set = "THOUGHT"
                    elif next.action in (Action.STOP, Action.AFFRICATE) and next.arpa != "G":
                        vowel.lexical_set = "THOUGHT"
                    elif next.arpa in ("L", "W"):
                        vowel.lexical_set = "THOUGHT"

                # check MFA dict
                vowel.lexical_set = check_uk_dict(word, phones, vowel, next) # type: ignore
                
                # try spelling rules if not in MFA dict
                if vowel.lexical_set == "not in dict":
                    if next and next.arpa == "R":
                        if (i + 2) < len(phones) and isinstance(phones[i + 2], Vowel) and not phones[i + 2].is_stressed:
                            vowel.lexical_set = "CLOTH"
                        else:
                            vowel.lexical_set = north_or_force(word, phones, vowel, next) # type: ignore
                    elif next and next.arpa in ("L", "W", "M", "SH", "K"):
                        vowel.lexical_set = "THOUGHT"
                    elif next and isinstance(next, Consonant) and next.action == Action.FRICATIVE and next.is_voiced:
                        vowel.lexical_set = "THOUGHT"
                    elif re.search(r"(au)[bcdfghjklmnpqstvwxz]", word) or re.search(r"(ough|al|aw)", word):
                        vowel.lexical_set = "THOUGHT"
                    else:
                        vowel.lexical_set = "ambiguous THOUGHT or CLOTH"


            # MOUTH - COMPLETE
            case "AW":
                vowel.lexical_set = "MOUTH"

            # PRICE - COMPLETE
            case "AY":
                vowel.lexical_set = "PRICE"

            # DRESS - assumes DRESS + R is always SQUARE?
            case "EH":
                if next and next.arpa == "R":
                    vowel.lexical_set = "SQUARE"
                elif vowel.is_stressed:
                    vowel.lexical_set = "DRESS"
                else:
                    vowel.lexical_set = "commA"
            
            # NURSE/LETTER - COMPLETE
            case "ER":
                if vowel.is_stressed:
                    vowel.lexical_set = "NURSE"
                else:
                    vowel.lexical_set = "lettER"

            # FACE - COMPLETE
            case "EY":
                vowel.lexical_set = "FACE"

            # KIT / NEAR - assumes NEAR is never unstressed and KIT + R is always NEAR
            case "IH":
                if vowel.is_stressed:
                    if next and next.arpa == "R":
                        vowel.lexical_set = "NEAR"
                    else:
                        vowel.lexical_set = "KIT"
                else:
                    vowel.lexical_set = "commA"

            # FLEECE / happY / commA / NEAR - assumes NEAR is never unstressed and FLEECE + R is always NEAR
            case "IY":
                if not vowel.is_stressed:
                    if first:
                        vowel.lexical_set = "commA"
                    else:
                        vowel.lexical_set = "happY"
                elif next and next.arpa == "R":
                    vowel.lexical_set = "NEAR"
                else:
                    vowel.lexical_set = "FLEECE"
            
            # GOAT/GOAL - COMPLETE
            case "OW":
                vowel.lexical_set = "GOAT"
                if next and next.arpa == "L":
                    vowel.lexical_set += "/GOAL"

            # CHOICE - COMPLETE
            case "OY":
                vowel.lexical_set = "CHOICE"

            # FOOT/CURE - assumes FOOT + R is always CURE
            case "UH":
                if next and next.arpa == "R":
                    vowel.lexical_set = "CURE"
                elif vowel.is_stressed:
                    vowel.lexical_set = "FOOT"
                else:
                    vowel.lexical_set = "commA"

            # GOOSE/CURE - assumes GOOSE + R is always CURE
            case "UW":
                if next and next.arpa == "R":
                    vowel.lexical_set = "CURE"
                elif vowel.is_stressed:
                    vowel.lexical_set = "GOOSE"
                else:
                    vowel.lexical_set = "commA"

def check_uk_dict(word, phones, vowel, next):

    lexical_set = ""
    
    # Split sets that are merged in GenAM, accessing MFA RP dictionary
    with open("dictionaries/uk.json", "r" , encoding="utf-8") as f:
        lookup = json.load(f)
        
        # check if word is in MFA dictionary
        try:
            transcriptions = lookup[word]
        except KeyError:
            lexical_set = "ambiguous"
        
        # split base on GenAm ARPA
        match vowel.arpa:

            # split LOT/PALM
            case "AA":
                if lexical_set == "ambiguous":
                    return "ambiguous LOT or PALM"
                possible_lot = False
                possible_palm = False
                for transcription in transcriptions:
                    if any('OX' in t for t in transcription):
                        possible_lot = True
                    if any('AA' in t for t in transcription):
                        possible_palm = True
                if possible_lot and not possible_palm:
                    return "LOT"
                elif possible_palm and not possible_lot:
                    return "PALM"
                else:
                    return "ambiguous LOT or PALM"
                
            # split TRAP/BATH
            case "AE":
                if lexical_set == "ambiguous":
                    return "ambiguous TRAP or BATH"
                possible_trap = False
                possible_bath = False
                for transcription in transcriptions:
                    if any('AE' in t for t in transcription):
                        possible_trap = True
                    if any('AA' in t for t in transcription):
                        possible_bath = True
                if possible_trap and not possible_bath:
                    return "TRAP"
                elif possible_bath and not possible_trap:
                    return "BATH"
                else:
                    return "ambiguous TRAP or BATH"
                
            # split THOUGHT/CLOTH/NORTH/FORCE
            case "AO":
                if lexical_set == "ambiguous":
                    return "not in dict" # tries more spelling logic
                possible_thought = False
                possible_cloth = False
                for transcription in transcriptions:
                    if any('AO' in t for t in transcription):
                        possible_thought = True
                    if any('OX' in t for t in transcription):
                        possible_cloth = True
                if possible_thought and not possible_cloth:
                    if next and next.arpa == "R":
                        return north_or_force(word, phones, vowel, next)
                    return "THOUGHT"
                elif possible_cloth and not possible_thought:
                    return "CLOTH"
                elif next and next.arpa != "R":
                    return "ambiguous THOUGHT or CLOTH"
                else:
                    return "ambiguous THOUGHT or CLOTH or NORTH or FORCE"
                    
def north_or_force(word, phones, vowel, next):
    
    # check if vowel is word final
    if phones[-2] and phones[-2].arpa == vowel.arpa:
        if word.endswith(("ore", "oar", "oor", "our")):
            return "FORCE"
        if word.endswith(("or", "ar")):
            return "NORTH"
        
    
    # check for prevocalic spellings
    if re.search(r"(aur)[aeiouy]", word):
        return "NORTH"
    if re.search(r"(or|oar)[aeiouy]", word):
        return "FORCE"
    
    # check for impossible FORCE spellings
    if word in ("pork", "forge", "proportion"):
        return "FORCE"
    if next and next.arpa in (
        "P", "B", "K", "JH", "M", "DH", "F", "V", "Z", "L", "SH", "ZH"
    ):
        return "NORTH"
    
    else:
        return "ambiguous NORTH or FORCE"