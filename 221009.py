import sys
from collections import deque

sys.stdin = open("input01.txt")

# 18258  큐2

n = int(input())
q = deque([])

for i in range(n):
    s = sys.stdin.readline().split()
    if s[0] == "push":
        q.append(s[1])
    elif s[0] == "pop":
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif s[0] == "size":
        print(len(q))
    elif s[0] == "empty":
        if not q:
            print(1)
        else:
            print(0)
    elif s[0] == "front":
        if not q:
            print(-1)
        else:
            print(q[0])
    elif s[0] == "back":
        if not q:
            print(-1)
        else:
            print(q[-1])
