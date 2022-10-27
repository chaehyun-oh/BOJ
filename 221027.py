import sys

sys.stdin = open("input01.txt")
#  13350 주유소

n = int(input())
r = list(map(int, input().split()))
c = list(map(int, input().split()))

res = r[0] * c[0]
m = c[0]
d = 0
for i in range(1, n - 1):
    if c[i] < m:
        res += m * d
        d = r[i]
        m = c[i]
    else:
        d += r[i]

    if i == n - 2:
        res += m * d
print(res)
