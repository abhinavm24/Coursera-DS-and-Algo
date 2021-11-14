# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i + 1))

        if next in ")]}":
            prev = opening_brackets_stack.pop() if len(
                opening_brackets_stack) > 0 else Bracket('', -1)

            if not are_matching(prev.char, next):
                return str(i + 1)

    if len(opening_brackets_stack) > 0:
        return str(opening_brackets_stack[-1].position)
    else:
        return 'Success'


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
