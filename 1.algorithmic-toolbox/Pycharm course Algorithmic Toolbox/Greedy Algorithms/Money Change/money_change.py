# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    # coins10, remainingMoney = divmod(money, 10)
    # coins5, remainingMoney = divmod(remainingMoney, 5)
    # return coins10 + coins5 + remainingMoney
    coins = [10, 5, 1]
    ans = []
    for coin in coins:
        div, rem = divmod(money, coin)
        ans.append(div)
        money = rem
    return sum(ans)


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
