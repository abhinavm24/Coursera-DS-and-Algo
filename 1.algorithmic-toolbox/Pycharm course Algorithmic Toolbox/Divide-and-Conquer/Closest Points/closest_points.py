# python3
import math
from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared


def minimum_distance_squared(points):
    # write your code here
    # print(x, y)
    x = [i.x for i in points]
    y = [i.y for i in points]
    # write your code here
    if len(x) == 2:
        return math.sqrt((x[0] - x[1]) ** 2 + (y[0] - y[1]) ** 2)

    mid = len(x) // 2
    left_x = x[:mid]
    right_x = x[mid:]
    left_y = y[:mid]
    right_y = y[mid:]

    left_dist = minimum_distance_squared(left_x, left_y)
    right_dist = minimum_distance_squared(right_x, right_y)
    mid_dist = minimum_distance_squared(x[mid - 1: mid + 1], y[mid - 1: mid + 1])

    return min(left_dist, right_dist, mid_dist)


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared_naive(input_points))))
    # print("{0:.9f}".format(sqrt(minimum_distance_squared(input_points))))
