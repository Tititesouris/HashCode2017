import parseInput, parseOutput

inputs = parseInput.getParsedInputs()

# Contains the output data as
# { fileName: {
#   cacheId1: [videoId1, videoId2],
#   cacheId2: [videoId2]
#   }
# }
outputs = {}


def scoreOf0(input):
    output = {}
    nbCaches = input["cache_count"]
    for cacheId in range(nbCaches):
        output[cacheId] = []
    return output


def goodScore(input):
    a = 1
    '''for endpoint in input["endpoints"]:
        for videoId, amountReq in endpoint["requests"]:
            for cacheId in range(nbCaches):
                output[cacheId].append(videoId)'''


# Calculates the output from the input
def getOutput(input):
    return scoreOf0(input)


for name, input in inputs.items():
    outputs[name] = getOutput(input)

parseOutput.parseOutputs(outputs)
