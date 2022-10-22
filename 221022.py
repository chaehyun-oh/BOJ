import sys

sys.stdin = open("input01.txt")

# 11047 동전 0
n, k = map(int, input().split())
m = []
num = 0

for i in range(n):
    m.append(int(input()))

for j in range(n - 1, -1, -1):
    if k == 0:
        break
    if m[j] > k:
        continue
    num += k // m[j]
    k %= m[j]

print(num)
