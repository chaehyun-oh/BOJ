from pprint import pprint
import sys

sys.stdin = open('input01.txt')

# 10872 팩토리얼
# n = int(input())

# def fact(m):
#     if m <= 1:
#         return 1
#     return m * fact(m-1)

# print(fact(n))


# 10870 피보나치 수 5
# n = int(input())

# def fib(m):
#     if m <= 1:
#         return m
#     return fib(m-1) + fib(m-2)

# print(fib(n))


# swea 1961 숫자 배열 회전

# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     matrix = [list(map(int, input().split())) for _ in range(n)]
#     rot90 = [[0]*n for _ in range(n)]
#     rot180 = [[0] * n for _ in range(n)]
#     rot270 = [[0] * n for _ in range(n)]

#     for i in range(n):
#         for j in range(n):
#             rot90[i][j] = matrix[n-j-1][i]

#     for i in range(n):
#         for j in range(n):
#             rot180[i][j] = rot90[n-j-1][i]

#     for i in range(n):
#         for j in range(n):
#             rot270[i][j] = rot180[n-j-1][i]

#     print(f'#{tc}')
#     for i in range(n):
#         for r in range(n):
#             print(rot90[i][r], end='')
#         print(end=' ')
#         for o in range(n):
#             print(rot180[i][o], end='')
#         print(end=' ')
#         for t in range(n):
#             print(rot270[i][t], end='')
#         print()

# swea 1966 숫자 정렬

# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     nums = list(map(int, input().split()))
#     nums.sort()
#     print(f'#{tc}', *nums)

# swea 1970 쉬운 거스름돈

# T = int(input())
# mon = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
# for tc in range(1, T+1):
#     n = int(input())
#     ans = [0] * 8

#     for i in range(8):
#         if n // mon[i] > 0:
#             ans[i] += n // mon[i]
#             n = n % mon[i]
#     print(f'#{tc}')
#     print(*ans)

# swea 1974 스도쿠 검증
n = 9


def chkSDK(m):
    for i in range(n):
        R = [0] * (n+1)
        C = [0] * (n+1)
        for j in range(n):
            r = m[i][j]
            c = m[j][i]

            if R[r]:
                return 0
            if C[c]:
                return 0

            R[r] = 1
            C[c] = 1

            if i % 3 == 0 and j % 3 == 0:
                s = [0] * (n+1)
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        num = m[k][l]
                        if s[num]:
                            return 0
                        s[num] = 1

    return 1


T = int(input())
for tc in range(1, T+1):
    matrix = [list(map(int, input().split())) for _ in range(n)]
    ans = chkSDK(matrix)
    print(f'#{tc} {ans}')
