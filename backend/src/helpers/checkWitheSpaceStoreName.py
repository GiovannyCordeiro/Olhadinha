from re import match

def checkWitheSpaceStoreName(store: str) -> str:
    storeNameWithSpace = match("\w+\s\w+", store)
    if storeNameWithSpace != None:
        splitingStore = store.split(" ")
        return "-".join(splitingStore)
    return store