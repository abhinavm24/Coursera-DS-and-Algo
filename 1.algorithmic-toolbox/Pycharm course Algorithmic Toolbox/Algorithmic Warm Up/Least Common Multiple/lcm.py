# python3


def lcm_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    multiple = max(a, b)
    while multiple % a != 0 or multiple % b != 0:
        multiple += 1

    return multiple


def lcm(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    def gcd(a, b):
        remainder, number = min(a, b), max(a, b)
        # while remainder > 0:
        #     carry = remainder
        #     remainder = number % remainder
        #     number = carry
        # return number
        if remainder == 0:
            return number
        else:
            return gcd(number % remainder, remainder)

    return a*b//gcd(a, b)


if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(lcm(input_a, input_b))
