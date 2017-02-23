# Calculates the output from the input
def getOutput(input):
    return myAlg(input)


def myAlg(input):
    output = {}
    nbCaches = input["cache_count"]
    for cacheId in range(nbCaches):
        output[cacheId] = []
    return output