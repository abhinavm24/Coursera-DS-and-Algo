# python3
from collections import defaultdict


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            print("naive:", 1)
            return Outcome.has_majority
    print("naive:", 0)
    return Outcome.no_majority


class Outcome:
    has_majority = 1
    no_majority = 0

def get_majority_element(a, left, right):
    """Decides if there is a majority among the votes
        Args:
         a (list): collection to check
         left (int): left index
         right (int): right index
        Returns:
         int: 1 if there is a majority, 0 otherwise
        """
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    left_elem = get_majority_element(a, left, (left + right + 1) // 2)
    right_elem = get_majority_element(a, (left + right + 1) // 2, right)

    lcount = 0
    for i in range(left, right):
        if a[i] == left_elem:
            lcount += 1
    if lcount > (right - left) // 2:
        return left_elem

    rcount = 0
    for i in range(left, right):
        if a[i] == right_elem:
            rcount += 1
    if rcount > (right - left) // 2:
        return right_elem

    return -1


def majority_element(elements):
    assert len(elements) <= 10 ** 5
    """Decides if there is a majority among the votes
        Args:
         votes (list): collection to check
        Returns:
         int: 1 if there is a majority, 0 otherwise
        """
    if get_majority_element(elements, 0, len(elements)) != -1:
        return 1
    else:
        return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
