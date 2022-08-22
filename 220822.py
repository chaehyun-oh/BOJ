# import math
import sys

sys.stdin = open('input01.txt')

# 달팽이

# a, b, v = map(int, input().split())

# cnt = math.ceil((v-a)/(a-b)) + 1
# print(cnt)

# ACM 호텔 10250
T = int(input())
ans = 0
for _ in range(T):
    h, w, n = map(int, input().split())
    floor = n % h
    rnum = n//h + 1
    if n % h == 0:
        rnum = n//h
        floor = h
    print(f'{floor*100+rnum}')
