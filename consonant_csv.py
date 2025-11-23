from consonants_only import lexiguess

source_path = "consonant_test.txt"
dest_path = "result.csv"

def lookups():
    with open(source_path, "r") as source:
        with open(dest_path, "w") as dest:
            dest.write("Word, Consonants\n")
            for line in source:
                if not line.strip():
                    continue
                word = line.strip()
                consonants = lexiguess(word)
                dest.write(f"{word},{consonants}\n")
lookups()