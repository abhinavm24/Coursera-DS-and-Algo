# python3

from sys import stdin


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    # We can compose weight 0 by taking nothing
    d = [[True] + [False] * capacity]
    for i in range(len(weights)):
        # We copy previous row which corresponds to
        # solution of not taking current gold
        d.append(d[-1][:])
        for w in range(weights[i], capacity + 1):
            # Weight w can be composed either by not taking current
            # gold (d[-2][w]) or by taking it (d[-2][w - golds[i]])
            d[-1][w] = d[-2][w] or d[-2][w - weights[i]]
        # It is enough to keep only last row
        d = d[-1:]
    for w in range(capacity, -1, -1):
        # Return maximal weight w that has True in d
        if d[-1][w]:
            return w


if __name__ == '__main__':
    input_capacity, n, *input_weights = [10, 3, 1, 4, 8]  # list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
