import sys

sys.stdin = open("input01.txt")

# 11053 증가 수열

n = int(input())
s = list(map(int, input().split()))
dp = [0 for _ in range(n)]

for i in range(n):
    for j in range(n):
        if s[i] > s[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))
