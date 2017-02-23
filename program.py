def goodScore(input):
    output = {}
    nbCaches = input["cache_count"]
    for cacheId in range(nbCaches):
        output[cacheId] = []
    cacheSize = input["cache_size"]
    videos = input["videos"]
    sizeLeft = [cacheSize for i in range(nbCaches)]

    for endpoint in input["endpoints"]:
        for videoId, amountReq in endpoint["requests"].items():
            for cacheId in range(nbCaches):
                output[cacheId].append(videoId)
    return output

# Calculates the output from the input
def getOutput(input):
    return goodScore(input)