import sys

sys.stdin = open("input01.txt")
# 24480 dfs 2
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, r = map(int, input().split())
s = [[] for _ in range(n + 1)]
ans = [0] * (n + 1)
cur = 1

for _ in range(m):
    a, b = map(int, input().split())
    s[a].append(b)
    s[b].append(a)

for i in s:
    i.sort(reverse=True)


def dfs(v):
    global cur
    ans[v] = cur
    for j in s[v]:
        if ans[j]:
            continue
        cur += 1
        dfs(j)


dfs(r)
for k in ans[1:]:
    print(k)
