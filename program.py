import parseInput, parseOutput

inputs = parseInput.getParsedInputs()

# Contains the output data as
# { fileName: {
#   cacheId1: [videoId1, videoId2],
#   cacheId2: [videoId2]
#   }
# }
outputs = {}


# Calculates the output from the input
def getOutput(input):
    output = {}
    nbCaches = input["cache_count"]
    for cacheId in range(nbCaches):
        output[cacheId] = []
    '''for endpoint in input["endpoints"]:
        for videoId, amountReq in endpoint["requests"]:
            for cacheId in range(nbCaches):
                output[cacheId].append(videoId)'''
    return output

for name, input in inputs.items():
    outputs[name] = getOutput(input)

parseOutput.parseOutputs(outputs)
