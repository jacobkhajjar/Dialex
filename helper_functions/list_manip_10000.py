from datetime import date

with open("lists/10000.txt", "r") as source:
    with open("result.csv", "w") as dest:
        dest.write("Word,Sets,Source,Checks,Score,Synonyms,Generated,Added\n")
        for line in source:
            if not line.strip():
                continue
            line = line.strip().split(" ")
            word = line[-1]
            dest.write(f"{word},{" ".join(line[:-1])},10000 list,3,0,False,False,{date.today()}\n")