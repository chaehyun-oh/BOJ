from math import ceil, sqrt
from pprint import pprint
import sys


sys.stdin = open('input01.txt')

# 베르트랑 공준 4948
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     cnt = 0

#     for i in range(n+1, 2*n+1):
#         if i == 1:
#             continue
#         elif i == 2:
#             cnt += 1
#             continue
#         else:
#             for j in range(2, int(sqrt(i)+1)):
#                 if i % j == 0:
#                     break
#             else:
#                 cnt += 1
#     print(cnt)


# swea 1946 간단한 압축 풀기
# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     org = ''
#     for i in range(n):
#         a, m = map(str, input().split())
#         m = int(m)
#         org += a*m
#     l = ceil(len(org)/10)
#     print(f'#{tc}')
#     for j in range(l):
#         print(org[10*j:10*(j+1)])

# swea 1948 날짜 계산기
mon = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
       7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
T = int(input())
for tc in range(1, T+1):
    ans = 0
    m1, d1, m2, d2 = map(int, input().split())
    if m1 == m2:
        ans = d2 - d1
    else:
        for i in range(m1, m2+1):
            if i == m1:
                ans += (mon[i] - d1)
            elif i == m2:
                ans += d2
            else:
                ans += mon[i]
    print(f'#{tc} {ans+1}')


# swea 1954

# swea 1959
# swea 1961
# swea 1966
# swea 1970
