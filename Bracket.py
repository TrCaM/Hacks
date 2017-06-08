# https://www.hackerrank.com/challenges/ctci-balanced-brackets
from collections import deque

def is_matched(expression):
    d = deque()
    for char in expression:
        if char == "[" or char == "{" or char == "(":
            d.append(char)
        else:
            try:
                match = d.pop()
            except IndexError:
                return False
            if (ord(char) - ord(match)) != 2 and (ord(char) - ord(match)) != 1:
                return False
    if len(d)!= 0:
        return False
    return True


t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
