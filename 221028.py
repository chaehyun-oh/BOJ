import sys

sys.stdin = open("input01.txt")
#  24445 bfs
from collections import deque

n, m, r = map(int, input().split())
s = [[] for _ in range(n + 1)]
vst = [0] * (n + 1)
vst[r] = 1
cnt = 1
q = deque([r])

for _ in range(m):
    a, b = map(int, input().split())
    s[a].append(b)
    s[b].append(a)

for i in range(1, n+1):
    s[i].sort(reverse=True)

while q:
    v = q.popleft()
    for j in s[v]:
        if vst[j]:
            continue
        cnt += 1
        vst[j] = cnt
        q.append(j)
print(*vst[1:], sep='\n')