import sys, parseInput, parseOutput, program, melOne

inputs = parseInput.getParsedInputs()
outputs = {}

for name, input in inputs.items():
    processors = {
        'default': program,
        'melOne': melOne,
    }

    choice = 'default'

    if len(sys.argv) > 1:
        choice = sys.argv[1]

    process = processors[choice]

    print('Processing ' + name + ' with processor ' + choice + '...')
    outputs[name] = process.getOutput(input)

parseOutput.parseOutputs(outputs)
