from pprint import pprint
import sys

sys.stdin = open('input01.txt')

# 11729 하노이탑

# n = int(input())


# def hanoi(n, fromP, toP, sP):
#     if n == 1:
#         print(fromP, sP)
#     else:
#         hanoi(n-1, fromP, sP, toP)
#         print(fromP, sP)
#         hanoi(n-1, toP, fromP, sP)


# cnt = 1
# for i in range(n-1):
#     cnt = cnt*2 + 1

# print(cnt)
# print(hanoi(n, 1, 3, 2))

# ----------------------
# n = int(input())


# def hanoi(n, a, b, c):
#     if n == 1:
#         print(a, c)
#     else:
#         hanoi(n - 1, a, c, b)
#         print(a, c)
#         hanoi(n - 1, b, a, c)


# sum = 1
# for i in range(n - 1):
#     sum = sum * 2 + 1
# print(sum)
# hanoi(n, 1, 2, 3)


# swea 2001 파리퇴치
# T = int(input())

# for testcase in range(1, T + 1):
#     n, m = map(int, input().split())
#     matrix = [list(map(int, input().split())) for _ in range(n)]
#     maxT = 0

#     for i in range(n - m + 1):
#         for j in range(n - m + 1):
#             total = 0
#             for k in range(m):
#                 total += sum(matrix[i+k][j:j+m])
#                 if total > maxT:
#                     maxT = total
#     print(f'#{testcase} {maxT}')


# swea 2005 파스칼의 삼각형

T = int(input())
for tc in range(1, T+1):
    n = int(input())

    arr = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i+1):
            if j == 0 or j == i:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

    print('#{}'.format(tc))

    for lst in arr:
        result = [x for x in lst if x]
        print(*result)


# swea 2007
