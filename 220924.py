import sys
sys.stdin = open('input01.txt')

# 14425 문자열 집합

n, m = map(int, input().split())
s = set([input() for _ in range(n)])
cnt = 0
for i in range(m):
    word = input()
    if word in s:
        cnt += 1
print(cnt)
