from datetime import date

with open("lists/scowlchecked.txt", "r") as source:
    with open("result.csv", "w") as dest:
        dest.write("Word,Sets,Source,Checks,Score,Homonyms,Generated,Added\n")
        for line in source:
            if not line.strip():
                continue
            line = line.strip().split(" ")
            word = line[0]
            dest.write(f"{word},{" ".join(line[1:])},SCOWL,1,0,False,False,{date.today()}\n")