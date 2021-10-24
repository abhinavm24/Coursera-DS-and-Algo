# python3
import math


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(m):
    denominations = [1, 3, 4]
    minCoins = [0] + [math.inf] * m

    for i in range(1, m + 1):
        for j in denominations:
            if i >= j:
                coins = minCoins[i - j] + 1
                if coins < minCoins[i]:
                    minCoins[i] = coins
    return minCoins[m]


if __name__ == '__main__':
    amount = 1#int(input())
    for amount in range(10):
        print(amount, change(amount), change_naive(amount))
