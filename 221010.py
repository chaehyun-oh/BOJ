import sys
from collections import deque

sys.stdin = open("input01.txt")

# 2164 카드2

n = int(input())
q = deque()

for i in range(1, n + 1):
    q.append(i)

while True:
    if len(q) == 1:
        print(q[0])
        break
    q.popleft()
    q.append(q.popleft())
