from imdb import IMDb

inputFile = input("Enter the name of the input file: ")
outputFile = inputFile.replace(".txt", "Links.txt")

ia = IMDb()
imdbLinks = {}

with open(inputFile, "r") as inputData:
    data = inputData.read().splitlines()

choice = inputFile.split('.')[0]
for field in data:
    if (choice == "actors"):
        searchResults = ia.search_person(field)
    elif (choice == "movies" or choice == "shows"):
        searchResults = ia.search_movie(field)  

    if searchResults:
        data = searchResults[0]
        if (choice == "actors"):
            imdbId = data.personID
            imdbLink = f"https://www.imdb.com/name/nm{imdbId}/"
        elif (choice == "movies" or choice == "shows"):
            imdbId = data.movieID    
            imdbLink = f"https://www.imdb.com/title/tt{imdbId}/"
        imdbLinks[field] = imdbLink

with open(outputFile, "w") as file:
    for field, imdbLink in imdbLinks.items():
        file.write(f"{field}: {imdbLink}\n")

print(f"IMDb links for have been saved to {outputFile}.")
