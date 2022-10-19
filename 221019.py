import sys

sys.stdin = open("input01.txt")

# 2805 나무 자르기


def bnr(s, start, end):
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        total = 0

        for i in s:
            if i > mid:
                total += i - mid
        if total < m:
            end = mid - 1
        else:
            ans = mid
            start = mid + 1
    return ans


n, m = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))

res = bnr(s, 0, max(s))
print(res)
