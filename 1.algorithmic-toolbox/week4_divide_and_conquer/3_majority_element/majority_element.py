# Uses python3
import sys
from typing import DefaultDict

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
    
    left_elem = get_majority_element(a, left, (left+right+1)//2)
    right_elem = get_majority_element(a, (left+right+1)//2, right)
    
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
    
        
def iterative_majority(votes):
    """Decides if there is a majority among the votes
    Args:
     votes (list): collection to check
    Returns:
     int: 1 if there is a majority, 0 otherwise
    """
    half = len(votes)//2
    counts = DefaultDict(lambda: 0)
    for vote in votes:
        counts[vote] += 1

    sorted_counts = sorted((count for count in counts.values()), reverse=True)
    return (Outcome.has_majority if sorted_counts[0] > half
            else Outcome.no_majority)

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
    # print(iterative_majority(a))
