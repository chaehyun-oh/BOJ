import sys

sys.stdin = open("input01.txt")

#  11399 ATM
n = int(input())
s = list(map(int, input().split()))
t = 0
s.sort()
for i in range(n):
    for j in range(i + 1):
        t += s[j]
print(t)
