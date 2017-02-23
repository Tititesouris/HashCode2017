from os import listdir

inputPath = "input/"
inputFiles = listdir(inputPath)

# Contains the input data as { fileName: data }
parsedInputs = {}


# Takes in a string and returns the data represented by that string
def parseInput(input):
    # TODO transform input string into data
    return [1, len(input), 3, "cucumber"]


for fileName in inputFiles:
    print("Parsing " + fileName)
    file = open(inputPath + fileName, "r")
    parsedInputs[fileName.split(".")[0]] = parseInput(file.read())


def getParsedInputs():
    return parsedInputs
