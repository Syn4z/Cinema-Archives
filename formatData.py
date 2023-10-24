import re

inputFile = input("Enter the name of the input file: ")
outputFile = re.match(r"([^A-Z]*)", inputFile).group(0) + '.md'

with open(inputFile, "r") as infile, open(outputFile, "w") as outfile:
    for line in infile:
        lastColonIndex = line.rfind(': ')
        
        if lastColonIndex != -1:
            firstPart = line[:lastColonIndex]
            imdbUrl = line[lastColonIndex + 2:].strip()
            outfile.write(f"- [{firstPart}]({imdbUrl})\n")
        else:
            outfile.write(f"- {line.strip()}\n")

print(f'Content of "{inputFile}" has been modified and saved to "{outputFile}".')
