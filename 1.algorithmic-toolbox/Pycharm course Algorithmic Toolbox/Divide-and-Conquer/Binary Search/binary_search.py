# python3


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def bin_search(keys, query, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if query == keys[mid]:
        return mid
    elif query < keys[mid]:
        return bin_search(keys, query, low, mid - 1)
    else:
        return bin_search(keys, query, mid + 1, high)


def binary_search(keys, query):
    assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 3 * 10 ** 4
    return bin_search(keys, query, 0, len(keys)-1)


if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')