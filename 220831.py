from distutils.spawn import spawn
from pprint import pprint
import sys

sys.stdin = open('input01.txt')

# 소수구하기 1929

# m, n = map(int, input().split())

# for i in range(m, n+1):
#     if i == 1:
#         continue
#     for j in range(2, int(i**0.5)+1):
#         if i % j == 0:
#             break
#     else:
#         print(i)


# swea 1940 RC 카

# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     s = 0
#     d = 0
#     for i in range(n):
#         comd = list(map(int, input().split()))
#         if comd[0] == 1:
#             s += comd[1]
#         elif comd[0] == 2:
#             if s > comd[1]:
#                 s -= comd[1]
#             else:
#                 s = 0
#         d += s
#     print(f'#{tc} {d}')

# swea 1945
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    nums = [2, 3, 5, 7, 11]
    ans = [0] * 5
    while True:
        for i in range(5):
            while True:
                if n % nums[i] == 0:
                    n //= nums[i]
                    ans[i] += 1
                else:
                    break
        if n == 1:
            break
    print(f'#{tc}', end=' ')
    for j in range(5):
        print(ans[j], end=' ')
    print()


# swea

    # swea

    # swea

    # swea
    # swea
    # swea
    # swea
