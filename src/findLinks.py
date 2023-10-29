from imdb import IMDb


def getImdbLinks(inputFile, choice):
    ia = IMDb()
    imdbLinks = {}

    with open(inputFile, "r") as inputData:
        data = inputData.read().splitlines()

    for field in data:
        if choice == "actors":
            searchResults = ia.search_person(field)
        elif choice == "movies" or choice == "shows":
            searchResults = ia.search_movie(field)

        if searchResults:
            data = searchResults[0]
            if choice == "actors":
                imdbId = data.personID
                imdbLink = f"https://www.imdb.com/name/nm{imdbId}/"
            elif choice == "movies" or choice == "shows":
                imdbId = data.movieID
                imdbLink = f"https://www.imdb.com/title/tt{imdbId}/"
            imdbLinks[field] = imdbLink

    return imdbLinks
