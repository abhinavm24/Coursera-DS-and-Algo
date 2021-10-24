# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    num_refill, curr_refill, fuelReach = 0, 0, m
    n = len(stops)
    while fuelReach < d:  # While the destination cannot be reached with current fuel
        if curr_refill >= n or stops[curr_refill] > fuelReach:
            # Cannot reach the destination nor the next gas station
            return -1
        # Find the furthest gas station we can reach
        while curr_refill < n - 1 and stops[curr_refill + 1] <= fuelReach:
            curr_refill += 1
        num_refill += 1  # Stop to tank
        fuelReach = stops[curr_refill] + m  # Fill up the tank
        curr_refill += 1
    return num_refill


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
