def getOutput(input):
    cache_content = {}

    cache_free = [input["cache_size"]] * input["cache_count"]

    for cacheId in range(input["cache_count"]):
        cache_content[cacheId] = []

    input['endpoints'] = sorted(input['endpoints'], key=endpoint_cost)

    while do_round(input, cache_content, cache_free):
        pass

    return cache_content


def request_cost(requests):
    return max(requests.values())


def endpoint_cost(endpoint):
    return -endpoint['latency_to_dc'] * request_cost(endpoint['requests'])


def do_round(input, cache_content, cache_free):
    for endpoint in input['endpoints']:
        cache_preference = sorted(endpoint['latency_to_caches'], key=endpoint['latency_to_caches'].__getitem__)

        if len(cache_preference) > 0 and len(endpoint['requests']) > 0:
            video = sorted(endpoint['requests'], key=endpoint['requests'].__getitem__)[-1]
            video_size = input['videos'][video]

            for cache_try in cache_preference:
                if video in cache_content[cache_try]:
                    del endpoint['requests'][video]
                    return True
                else:
                    if video_size <= cache_free[cache_try]:
                        del endpoint['requests'][video]
                        cache_free[cache_try] = cache_free[cache_try] - video_size
                        cache_content[cache_try].append(video)
                        return True

    return False
