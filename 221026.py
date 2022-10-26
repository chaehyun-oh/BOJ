import sys

sys.stdin = open("input01.txt")
# 1931 회의실 배정
n = int(input())
s = []
for i in range(n):
    a, b = map(int, input().split())
    s.append([a, b])
s = sorted(s, key=lambda x: x[0])
s = sorted(s, key=lambda x: x[1])
end = 0
cnt = 0
for j, k in s:
    if j >= end:
        cnt += 1
        end = k
print(cnt)
