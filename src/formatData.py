import os


def createMdFile(inputFile, outputFile):
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

    print(f'Content has been appended to "{outputFile}".')
