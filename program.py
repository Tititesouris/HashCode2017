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
    # TODO calculate an output data from the input data
    return input


for name, input in inputs.items():
    outputs[name] = getOutput(input)

parseOutput.parseOutputs(outputs)
