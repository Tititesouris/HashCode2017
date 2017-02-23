import sys, parseInput, parseOutput, program, zeroScore, melOne, phreddOne, quentinV1
from os import listdir

processors = {
    'default': program,
    'zeroScore': zeroScore,
    'melOne': melOne,
    'phreddOne': phreddOne,
    'quentinV1': quentinV1
}

choice = 'default'

if len(sys.argv) > 1:
    choice = sys.argv[1]

if len(sys.argv) > 2:
    files = [sys.argv[2]]
else:
    inputPath = "input/"
    files = [inputPath + str(x) for x in listdir(inputPath)]

process = processors[choice]

inputs = parseInput.getParsedInputs(files)
outputs = {}

for name, input in inputs.items():
    print('Processing ' + name + ' with processor ' + choice + '...')
    outputs[name] = process.getOutput(input)

parseOutput.parseOutputs(outputs)
