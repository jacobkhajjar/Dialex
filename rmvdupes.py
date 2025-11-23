input_file = "result.csv"
output_file = "result_deduped.csv"

seen = set()
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        if line not in seen:
            outfile.write(line)
            seen.add(line)