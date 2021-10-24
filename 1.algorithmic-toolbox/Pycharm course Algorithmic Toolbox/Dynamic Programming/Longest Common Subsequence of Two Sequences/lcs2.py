# python3


# Function to find the length of the longest common subsequence of
# sequences `X[0…m-1]` and `Y[0…n-1]`
def lcs_length(X, Y, m, n):
    # return if the end of either sequence is reached
    if m == 0 or n == 0:
        return 0

    # if the last character of `X` and `Y` matches
    if X[m - 1] == Y[n - 1]:
        return lcs_length(X, Y, m - 1, n - 1) + 1

    # otherwise, if the last character of `X` and `Y` don't match
    return max(lcs_length(X, Y, m, n - 1), lcs_length(X, Y, m - 1, n))


def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    return lcs_length(first_sequence, second_sequence, len(first_sequence), len(second_sequence))


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
