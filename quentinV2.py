output = {}
nbCaches = 0
cacheSize = 0
videos = []
endpoints = []
sizeLeft = []
insideCache = []


def goodScore(input):
    global output, nbCaches, cacheSize, videos, endpoints, sizeLeft, insideCache
    output = {}
    nbCaches = input["cache_count"]
    for cacheId in range(nbCaches):
        output[cacheId] = []
    cacheSize = input["cache_size"]
    for i in range(len(input["videos"])):
        videos.append({"id": i, "size": input["videos"][i]})

    videos.sort(key=lambda video: video["size"], reverse=True)
    endpoints = input["endpoints"]
    endpoints.sort(key=lambda endpoint: endpoint["latency_to_dc"], reverse=True)
    sizeLeft = [cacheSize for i in range(nbCaches)]
    insideCache = [[] for i in range(nbCaches)]

    for endpoint in endpoints:
        for videoId, amountReq in endpoint["requests"].items():
            for cacheId, latency in endpoint["latency_to_caches"].items():
                if not hasVideo(cacheId, videoId) and hasEnoughSpace(cacheId, videoId):
                    addVideoToCache(cacheId, videoId)
    return output


def getVideoById(videoId):
    for video in videos:
        if video["id"] == videoId:
            return video

def hasEnoughSpace(cacheId, videoId):
    return sizeLeft[cacheId] >= getVideoById(videoId)["size"]


def hasVideo(cacheId, videoId):
    return videoId in insideCache[cacheId]


def addVideoToCache(cacheId, videoId):
    output[cacheId].append(videoId)
    sizeLeft[cacheId] -= getVideoById(videoId)["size"]
    insideCache[cacheId].append(videoId)


# Calculates the output from the input
def getOutput(input):
    return goodScore(input)
