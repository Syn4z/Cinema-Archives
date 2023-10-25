import re
import os

inputFile = input("Enter the name of the input file: ")
outputFile = '../data/' + re.match(r"([^A-Z]*)", inputFile).group(0) + '.md'

appendMode = False
uniqueLines = set()

if os.path.exists(outputFile):
    appendMode = True

    with open(outputFile, "r") as existing_file:
        for line in existing_file:
            uniqueLines.add(line)

with open(inputFile, "r") as infile, open(outputFile, "a" if appendMode else "w") as outfile:
    for line in infile:
        lastColonIndex = line.rfind(': ')
        firstPart = line[:lastColonIndex]
        imdbUrl = line[lastColonIndex + 2:].strip()
        line = f"- [{firstPart}]({imdbUrl})\n"
        if line not in uniqueLines:
            
            if lastColonIndex != -1:
                outfile.write(f"- [{firstPart}]({imdbUrl})\n")
            else:
                outfile.write(f"{line.strip()}\n")

print(f'Content of "{inputFile}" has been appended (without duplicates) to "{outputFile}".')