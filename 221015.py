import sys

sys.stdin = open("input01.txt")

# 1021 회전하는 큐

from collections import deque

n, m = map(int, sys.stdin.readline().split())
p = list(map(int, sys.stdin.readline().split()))
q = deque([i for i in range(1, n + 1)])

cnt = 0
for i in p:
    while True:
        if q[0] == i:
            q.popleft()
            break
        else:
            if q.index(i) < len(q) / 2:
                while q[0] != i:
                    q.append(q.popleft())
                    cnt += 1
            else:
                while q[0] != i:
                    q.appendleft(q.pop())
                    cnt += 1
print(cnt)
