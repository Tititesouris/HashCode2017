import sys, parseInput, parseOutput, program, zeroScore, melOne

inputs = parseInput.getParsedInputs()
outputs = {}

for name, input in inputs.items():
    processors = {
        'default': program,
        'zeroScore': zeroScore,
        'melOne': melOne,
    }

    choice = 'default'

    if len(sys.argv) > 1:
        choice = sys.argv[1]

    process = processors[choice]

    print('Processing ' + name + ' with processor ' + choice + '...')
    outputs[name] = process.getOutput(input)

parseOutput.parseOutputs(outputs)
