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
    output=input
    return output


for name, input in inputs.items():
    outputs[name] = getOutput(input)

#parseOutput.parseOutputs(outputs)

data = {
'videos': [50, 50, 80, 30, 110],
'endpoint': [
{
'latency_to_dc': 1000,
'latency_to_caches': {
0: 100,
1: 300,
2: 200
},
'requests':
 { 1: 1000, 3: 1500, 4: 500 }

},
{
'latency_to_dc': 500,
'latency_to_caches': {},
'requests':
 { 0: 1000 }
}
],
'cache_size': 3,
'cache_count': 100
}

print(getOutput(data))