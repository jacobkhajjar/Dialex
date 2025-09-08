from datetime import date

with open("lists/Armstrong1check.txt", "r") as source:
    with open("result.csv", "w") as dest:
        dest.write("Word,Sets,Source,Checks,Score,Synonyms,Generated,Added\n")
        for line in source:
            if not line.strip():
                continue
            line = line.strip().split(" ")
            word = line[0]
            dest.write(f"{word},{" ".join(line[1:])},Armstrong,2,0,False,False,{date.today()}\n")