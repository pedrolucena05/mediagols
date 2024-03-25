
def organizing_keys(tuple):
    primarykeys = []
    secondarykeys = []
    urls = []

    for item in tuple:
        primarykeys.append(item[0])
        secondarykeys.append(item[1])

    for k_item in secondarykeys:
        aux= list(k_item.values())
        for j_item in aux:
            urls.append(j_item)
    
    return urls