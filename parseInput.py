from os import listdir

inputPath = "input/"
inputFiles = listdir(inputPath)

# Contains the input data as { fileName: data }
parsedInputs = {}

# Takes in a string and returns the data represented by that string
def parseInput(file):
    # Read header
    video_count, endpoint_count, requests, cache_count, cache_size = split_line(file.readline())

    # Dictionary to return
    data = {'videos': [], 'endpoints': [], 'cache_size': int(cache_size), 'cache_count': int(cache_count)}

    # Read the video sizes
    video_sizes = split_line(file.readline())

    # Sanity check size
    if len(video_sizes) != int(video_count):
        print("Header video count does not match read videos.")

    data['videos'] = list(map(int, video_sizes))

    for x in range(0, int(endpoint_count)):
        data['endpoints'].append(read_endpoint(file))

    for x in range(0, int(requests)):
        read_request(file, data)

    return data


def read_endpoint(file):
    latency_to_dc, cache_count = split_line(file.readline())

    data = {'latency_to_dc': int(latency_to_dc), 'latency_to_caches': {}, 'requests': {}}

    for x in range(0, int(cache_count)):
        cache_number, cache_latency = split_line(file.readline())
        data['latency_to_caches'][int(cache_number)] = int(cache_latency)

    return data


def read_request(file, data):
    video, endpoint, count = split_line(file.readline())

    endpoint_as_int = int(endpoint)
    data['endpoints'][endpoint_as_int]['requests'][int(video)] = int(count)


def split_line(line):
    return line.split(" ")

for fileName in inputFiles:
    print("Parsing " + fileName)
    file = open(inputPath + fileName, "r")
    parsedInputs[fileName.split(".")[0]] = parseInput(file)

def getParsedInputs():
    return parsedInputs
