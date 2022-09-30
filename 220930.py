import sys

sys.stdin = open("input01.txt")

# 1543 문서검색
d = input()
s = input()
cnt = 0
n = 0
while n <= len(d) - len(s):
    if d[n : n + len(s)] == s:
        cnt += 1
        n += len(s)
    else:
        n += 1
print(cnt)
