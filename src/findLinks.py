from imdb import IMDb

def getImdbLinks(inputFile, choice):
    ia = IMDb()
    imdbLinks = {}

    with open(inputFile+'.txt', "r") as inputData:
        data = inputData.read().splitlines()

    for field in data:
        if choice == "actors":
            searchResults = ia.search_person(field)
        elif choice == "movies" or choice == "shows":
            searchResults = ia.search_movie(field)

        if searchResults:
            imdb_name = searchResults[0]['name'] if choice == "actors" else searchResults[0]['title']
            if imdb_name.lower() != field.lower():
                print(f"Warning: The name '{field}' does not match exactly with IMDb. Using IMDb name '{imdb_name}' instead.")
            if choice == "actors":
                imdbId = searchResults[0].personID
                imdbLink = f"https://www.imdb.com/name/nm{imdbId}/"
            elif choice == "movies" or choice == "shows":
                imdbId = searchResults[0].movieID
                imdbLink = f"https://www.imdb.com/title/tt{imdbId}/"
            imdbLinks[imdb_name] = imdbLink
        else:
            print(f"No results found for '{field}' in IMDb.")

    return imdbLinks
