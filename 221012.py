import sys

sys.stdin = open("input01.txt")

# 11866 요세푸스
from collections import deque

n, k = map(int, input().split())
q = deque([])

for i in range(1, n + 1):
    q.append(i)
print("<", end="")
while q:
    for j in range(k - 1):
        q.append(q[0])
        q.popleft()
    print(q.popleft(), end="")
    if q:
        print(", ", end="")
print(">")
