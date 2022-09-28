import sys

sys.stdin = open("input01.txt")

# 1822 차집합

n, m = map(int, sys.stdin.readline().split())

a = set(map(int, sys.stdin.readline().split()))
b = set(map(int, sys.stdin.readline().split()))
ans = a - b

res = sorted(ans)
print(len(res))
if len(res) != 0:
    print(*(res))
