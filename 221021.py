import sys

sys.stdin = open("input01.txt")

# 1654 랜선 자르기


k, n = map(int, input().split())
L = [int(sys.stdin.readline()) for _ in range(k)]
start, end = 1, max(L)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in L:
        cnt += i // mid

    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)
