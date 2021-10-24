NOT_FOUND = -1
def bin_search(keys, query, low, high):
    if low > high:
        return NOT_FOUND
    mid = (low + high) // 2
    if query == keys[mid]:
        return mid
    if query < keys[mid]:
        return bin_search(keys, query, low, mid - 1)
    else:
        return bin_search(keys, query, mid + 1, high)

def binary_search(keys, query):
    """
    Return the index of the query in keys, or -1 if not found.
    """
    return bin_search(keys, query, 0, len(keys) - 1)    


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
