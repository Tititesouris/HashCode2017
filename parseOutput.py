outputPath = "output/"


# Takes in data and returns a string representing that data
def parseOutput(output):
    # TODO transform output data into string
    return "BOB"


def parseOutputs(outputs):
    for name, output in outputs.items():
        file = open(outputPath + name + ".out", "w")
        file.write(parseOutput(output))
        file.close()
