from lexiguess import lexiguess
from datetime import date

source_path = "lists/scowlmissing.txt"
dest_path = "result.csv"

word_source = "10000 list"

def lookups():
    with open(source_path, "r") as source:
        with open(dest_path, "w") as dest:
            dest.write("Word,Sets,Source,Checks,Score,Homonyms,Generated,Added\n")
            for line in source:
                if not line.strip():
                    continue
                word = line.strip()
                sets, score, homonyms = lexiguess(word)
                if homonyms:
                    for set in sets:
                        dest.write(f"{word},{set},{word_source},0,{score},{homonyms},True,{date.today()}\n")
                else:
                    dest.write(f"{word},{sets[0]},{word_source},0,{score},{homonyms},True,{date.today()}\n")

lookups()