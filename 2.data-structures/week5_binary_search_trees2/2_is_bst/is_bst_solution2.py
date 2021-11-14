#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(10**8)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


# this class represents a node in a binary tree
class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    # this function returns a string representation of a node for printing purposes
    def __str__(self):
        return 'key = {} left = {} right = {}'.format(self.key, self.left, self.right)


# this function reads the input and returns a binary tree built from the input
def read():
    n = int(sys.stdin.readline())
    key = [0 for i in range(n)]
    left = [0 for i in range(n)]
    right = [0 for i in range(n)]
    for i in range(n):
        [a, b, c] = map(int, sys.stdin.readline().split())
        key[i] = a
        left[i] = b
        right[i] = c

    if n == 0:  # emtpy tree is considered a BST
        return 0

    tree = [Node(key[i], left[i], right[i]) for i in range(n)]

  # start building a binary tree by updating each node's left and right attribute
    for i in range(n):
        if tree[i].left != -1:
            temp = tree[i].left
            tree[i].left = tree[temp]
        if tree[i].right != -1:
            temp = tree[i].right
            tree[i].right = tree[temp]

    return tree[0]  # return the root of the binary tree

# this function check whether the passed in binary tree is a BST
# if yes, return True
# if no, return False


def IsBinarySearchTree(tree):
  # create a list result to store the in-order traversal path of the passed in binary tree
    result = []
    inOrder(tree, result)

    # create a new list that has the same elements from the result list but in sorted order
    sorted_result = sorted(result)

    # if the sorted list is the same as the result list, the tree is a BST and return True
    # otherwise, return False
    if result == sorted_result:
        return True
    else:
        return False


# this function traverses through a binary tree in an in-order fashion
# and returns the traversal path taken
def inOrder(tree, result):
    # if the current tree (represented as a node) is a leaf, append the tree's key (node's key) to result to document the traversal path and then return to the tree's parent
    if tree.left == -1 and tree.right == -1:
        result.append(tree.key)
        return

    # if the subtree has a left child, traverse down the left child subtree
    if tree.left != -1:
        inOrder(tree.left, result)

    # append the tree's key after done traversing its left child
    result.append(tree.key)

    # traverse down the tree's right child(
    if tree.right != -1:
        inOrder(tree.right, result)


# this function reads the input, build a binary tree from it,
# and check if the tree is a BST by checking if its in-order traversal path assembles a sorted list
# the tree does not need to be balanced
# if yes, return 'CORRECT'
# if no, return 'INCORRECT'
# special case: an empty tree is a BST
# The definition of the binary search tree is the following:
# for any node of the tree, if its
# key is 𝑥, then for any node in its left subtree its key must be strictly less than 𝑥, and for any node in
# its right subtree its key must be strictly greater than 𝑥.
# input format:
# The first line contains the number of vertices 𝑛. The vertices of the tree are numbered from 0 to 𝑛 − 1. Vertex 0 is the root.
# The next 𝑛 lines contain information about vertices 0, 1, ..., 𝑛−1 in order. Each of these lines contains
# three integers 𝑘𝑒𝑦𝑖, 𝑙𝑒𝑓𝑡𝑖 and 𝑟𝑖𝑔ℎ𝑡𝑖 — 𝑘𝑒𝑦𝑖 is the key of the 𝑖-th vertex, 𝑙𝑒𝑓𝑡𝑖 is the index of the left
# child of the 𝑖-th vertex, and 𝑟𝑖𝑔ℎ𝑡𝑖 is the index of the right child of the 𝑖-th vertex. If 𝑖 doesn’t have
# left or right child (or both), the corresponding 𝑙𝑒𝑓𝑡𝑖 or 𝑟𝑖𝑔ℎ𝑡𝑖 (or both) will be equal to −1.
# output format:
# Output Format. If the given binary tree is a correct binary search tree,
# output one word “CORRECT” (without quotes). Otherwise, output one word “INCORRECT” (without quotes).
# example:
# input:
# 8
# 5 1 2
# 3 3 4
# 8 -1 5
# 1 -1 -1
# 4 -1 -1
# 9 -1 6
# 10 -1 7
# 11 -1 -1
# tree built from the input using read() and visualized as below
#               5
#             /  \
#           3     8
#         /  \     \
#       1     4     9
#                    \
#                    10
#                      \
#                      11
# output: CORRECT
# because the tree's in-order traversal path is a sorted list = [1, 3, 4, 5, 8, 9, 10, 11],
# it is a binary search tree
def main():
    tree = read()
    if tree == 0:  # emtpy tree is considered a BST
        print('CORRECT')
    else:  # if a tree is not empty, traverse through the tree to check if it's a BST
        if IsBinarySearchTree(tree):
            print("CORRECT")
        else:
            print("INCORRECT")


threading.Thread(target=main).start()
