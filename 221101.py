import sys

sys.stdin = open("input01.txt")

#  1260 dfs bfs
from collections import deque


def dfs(n):
    vst[n] = True
    print(n, end=" ")
    for i in s[n]:
        if not vst[i]:
            dfs(i)


def bfs(n):
    q = deque([n])
    vst[n] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in s[v]:
            if not vst[i]:
                q.append(i)
                vst[i] = True


n, m, v = map(int, sys.stdin.readline().split())
s = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    s[a].append(b)
    s[b].append(a)
for j in range(1, n + 1):
    s[j].sort()

vst = [False] * (n + 1)

dfs(v)
print()

vst = [False] * (n + 1)

bfs(v)
