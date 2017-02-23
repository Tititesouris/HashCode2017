output = {}
nbCaches = 0
cacheSize = 0
videos = []
sizeLeft = []
insideCache = []


def goodScore(input):
    global output, nbCaches, cacheSize, videos, sizeLeft, insideCache
    output = {}
    nbCaches = input["cache_count"]
    for cacheId in range(nbCaches):
        output[cacheId] = []
    cacheSize = input["cache_size"]
    videos = input["videos"]
    sizeLeft = [cacheSize for i in range(nbCaches)]
    insideCache = [[] for i in range(nbCaches)]

    for endpoint in input["endpoints"]:
        for videoId, amountReq in endpoint["requests"].items():
            for cacheId, latency in endpoint["latency_to_caches"].items():
                if not hasVideo(cacheId, videoId) and hasEnoughSpace(cacheId, videoId):
                    addVideoToCache(cacheId, videoId)
    return output


def hasEnoughSpace(cacheId, videoId):
    return sizeLeft[cacheId] >= videos[videoId]


def hasVideo(cacheId, videoId):
    return videoId in insideCache[cacheId]


def addVideoToCache(cacheId, videoId):
    output[cacheId].append(videoId)
    sizeLeft[cacheId] -= videos[videoId]
    insideCache[cacheId].append(videoId)


# Calculates the output from the input
def getOutput(input):
    return goodScore(input)
