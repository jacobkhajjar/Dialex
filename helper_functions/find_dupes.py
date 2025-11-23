words = set()
dupes = set()

with open("lists/10000.csv", "r") as f1:
    count = 0
    for line in f1:
        word = line.split(",")[0]
        if word in words:
            dupes.add(word)
            count += 1
        words.add(word)
    print(f"{count} dupes in 10000.csv")

with open("lists/Armstrong0.csv", "r") as f1:
    count = 0
    for line in f1:
        word = line.split(",")[0]
        if word in words:
            dupes.add(word)
            count += 1
        words.add(word)
    print(f"{count} dupes in Armstrong0.csv")

with open("lists/Armstrong1.csv", "r") as f1:
    count = 0
    for line in f1:
        word = line.split(",")[0]
        if word in words:
            dupes.add(word)
            count += 1
        words.add(word)
    print(f"{count} dupes in Armstrong.csv")

with open("lists/scowlchecked.csv", "r") as f1:
    count = 0
    for line in f1:
        word = line.split(",")[0]
        if word in words:
            dupes.add(word)
            count += 1
        words.add(word)
    print(f"{count} dupes in scowlchecked.csv")

with open("lists/missing10000.txt", "r") as f1:
    count = 0
    for line in f1:
        word = line.strip()
        if word in words:
            dupes.add(word)
            count += 1
        words.add(word)
    print(f"{count} dupes in missing10000.txt")

with open("lists/scowlmissing.txt", "r") as f1:
    count = 0
    for line in f1:
        word = line.strip()
        if word in words:
            dupes.add(word)
            count += 1
        words.add(word)
    print(f"{count} dupes in scowlmissing.txt")

with open("dupes.txt", "w") as f:
    for dupe in dupes:
        f.write(dupe + "\n")