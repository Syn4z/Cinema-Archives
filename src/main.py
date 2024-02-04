from findLinks import getImdbLinks
from formatData import createMdFile
import os
import re

if __name__ == "__main__":
    inputFile = '../input/' + input("Enter the name of the input file: ")+'.txt'
    choice, _ = os.path.splitext(os.path.basename(inputFile))
    linksFile = choice + "Links.txt"
    imdbLinks = getImdbLinks(inputFile, choice)

    with open(linksFile, "w") as file:
        for field, imdbLink in imdbLinks.items():
            file.write(f"{field}: {imdbLink}\n")

    outputData = '../output/' + re.match(r"([^A-Z]*)", linksFile).group(0) + '.md'
    createMdFile(linksFile, outputData)
