# Calculates the output from the input
def getOutput(input):
    return myAlg(input)


'''
Slight upgrade: first sort endpoints by descending latency_to_dc
'''

def myAlg(input):
    #print(input)
    output = {}

    # Harvest variables from input data
    numCaches = input["cache_count"]
    cacheSize = input["cache_size"]

    cacheSpace = {} # initialise dictionary to keep track of space left in cache
    for cacheID in range(numCaches):
        # Create a dictionary containing the space left in each cache
        cacheSpace[cacheID] = cacheSize
        # Create an empty list for each cache, to be populated with videos
        output[cacheID] = []

    for endpoint in sorted(input["endpoints"],key=lambda latency: latency["latency_to_dc"],reverse=True):
        # List of Video IDs sorted by descending number of requests
        videoIDs = sorted(endpoint["requests"],key=endpoint["requests"].__getitem__,reverse=True)
        # List of Caches sorted by ascending latency
        cacheList = sorted(endpoint["latency_to_caches"],key=endpoint["latency_to_caches"].__getitem__)

        for video in videoIDs:
            for cache in cacheList:
                if video in output[cache]:
                    break
                else:
                    if cacheSpace[cache] > input["videos"][video]:
                        output[cache].append(video)
                        cacheSpace[cache] -= input["videos"][video]
                        break

    return output



'''
Basic Algorithm

Plan:
    loop over endpoints
        loop over requests by descending number of requests
            loop over caches by ascending latencies
                if          video not in cache (else break)
                        and cache not full
                    then add video to cache
                break

'''
''' Basic algorithm:
def myAlg(input):
    print(input)
    output = {}

    # Harvest variables from input data
    numCaches = input["cache_count"]
    cacheSize = input["cache_size"]

    cacheSpace = {} # initialise dictionary to keep track of space left in cache
    for cacheID in range(numCaches):
        # Create a dictionary containing the space left in each cache
        cacheSpace[cacheID] = cacheSize
        # Create an empty list for each cache, to be populated with videos
        output[cacheID] = []

    #print(cacheSpace)
    #print(output)

    for endpoint in input["endpoints"]:
        # List of Video IDs sorted by descending number of requests
        videoIDs = sorted(endpoint["requests"],key=endpoint["requests"].__getitem__,reverse=True)
        # List of Caches sorted by ascending latency
        cacheList = sorted(endpoint["latency_to_caches"],key=endpoint["latency_to_caches"].__getitem__)

        for video in videoIDs:
            for cache in cacheList:
                if video in output[cache]:
                    #print('in')
                    break
                else:
                    #print('not in')
                    if cacheSpace[cache] > input["videos"][video]:
                        output[cache].append(video)
                        cacheSpace[cache] -= input["videos"][video]
                        break

    #print(output)
    #print(cacheSpace)

    return output
'''