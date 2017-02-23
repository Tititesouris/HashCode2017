# Calculates the output from the input
def getOutput(input):
    return scoreOf0(input)

def scoreOf0(input):
    output = {}
    nbCaches = input["cache_count"]
    for cacheId in range(nbCaches):
        output[cacheId] = []
    return output