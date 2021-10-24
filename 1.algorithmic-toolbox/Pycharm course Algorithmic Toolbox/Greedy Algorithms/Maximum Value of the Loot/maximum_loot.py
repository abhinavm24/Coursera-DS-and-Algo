# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    priceByWeight = ((prices[index] / weights[index], index)
                     for index in range(len(weights)))

    # we have to reverse-sort it (otherwise sorting puts the smallest
    # number first)
    sortedPricedWeight = sorted(priceByWeight, reverse=True)

    # loot is the value of what we've taken so far
    loot = 0

    # precondition: per_poundage is the value-per-pound in descending
    # order for each item along with the index of the original weight/value
    for value, index in sortedPricedWeight:
        # invariant: value is the largest price-per-pound available
        if capacity < weights[index]:
            # we don't have enough strength to take all of this item
            # so just take as much as we can and quit
            loot += value * capacity
            break
        # otherwise take all of this item
        loot += prices[index]
        # reducing our capacity by its total weight
        capacity -= weights[index]
        if capacity == 0:
            # we're out of capacity, quit
            break
    return loot


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
