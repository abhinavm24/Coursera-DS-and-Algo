#Uses python3

import sys

# Function to find the length of the longest common subsequence of
# sequences `X[0…m-1]` and `Y[0…n-1]`
def lcs_length_naive(X, Y, m, n):
    # return if the end of either sequence is reached
    if m == 0 or n == 0:
        return 0

    # if the last character of `X` and `Y` matches
    if X[m - 1] == Y[n - 1]:
        return lcs_length_naive(X, Y, m - 1, n - 1) + 1

    # otherwise, if the last character of `X` and `Y` don't match
    return max(lcs_length_naive(X, Y, m, n - 1), lcs_length_naive(X, Y, m - 1, n))

# Function to find the length of the longest common subsequence of substring
# `X[0…m-1]` and `Y[0…n-1]`
def LCSLength(X, Y, m, n, lookup):
 
    # return if the end of either string is reached
    if m == 0 or n == 0:
        return 0
 
    # construct a unique key from dynamic elements of the input
    key = (m, n)
 
    # if the subproblem is seen for the first time, solve it and
    # store its result in a dictionary
    if key not in lookup:
 
        # if the last character of `X` and `Y` matches
        if X[m - 1] == Y[n - 1]:
            lookup[key] = LCSLength(X, Y, m - 1, n - 1, lookup) + 1
 
        else:
            # otherwise, if the last character of `X` and `Y` don't match
            lookup[key] = max(LCSLength(X, Y, m, n - 1, lookup),
                            LCSLength(X, Y, m - 1, n, lookup))
 
    # return the subproblem solution from the dictionary
    return lookup[key]


# Function to find the length of the longest common subsequence of substring
# `X[0…m-1]` and `Y[0…n-1]`
def LCSLengthMatrix(X, Y):
 
    m = len(X)
    n = len(Y)
 
    # lookup table stores solution to already computed subproblems;
    # i.e., `T[i][j]` stores the length of LCS of substring
    # `X[0…i-1]` and `Y[0…j-1]`
    T = [[0 for x in range(n + 1)] for y in range(m + 1)]
 
    # fill the lookup table in a bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # if the current character of `X` and `Y` matches
            if X[i - 1] == Y[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1
            # otherwise, if the current character of `X` and `Y` don't match
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])
 
    # LCS will be the last entry in the lookup table
    return T[m][n]

def lcs2(a, b):
    # create a dictionary to store solutions to subproblems
    lookup = {}
    # return lcs_length(a, b, len(a), len(b))
    # return LCSLength(a, b, len(a), len(b), lookup)
    return LCSLengthMatrix(a, b)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
