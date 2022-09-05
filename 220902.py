from pprint import pprint
import sys

sys.stdin = open('input01.txt')

# 골드바흐의 추측 9020
# s = [0 for i in range(10001)]
# s[1] = 1
# for i in range(2, 98):
#     for j in range(i * 2, 10001, i):
#         s[j] = 1
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     a = n // 2
#     for k in range(a, 1, -1):
#         if s[n - k] == 0 and s[k] == 0:
#             print(k, n - k)
#             break

# swea 1954 달팽이 숫자
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# T = int(input())

# for tc in range(1, T+1):
#     n = int(input())
#     i, j = 0, 0
#     d = 0
#     matrix = [[0] * n for i in range(n)]
#     for k in range(1, n*n+1):
#         matrix[i][j] = k
#         i += dx[d]
#         j += dy[d]

#         if i < 0 or j < 0 or i >= n or j >= n or matrix[i][j] != 0:
#             i -= dx[d]
#             j -= dy[d]

#             d = (d+1) % 4
#             i += dx[d]
#             j += dy[d]
#     print(f'#{tc}')
#     for m in matrix:
#         print(*m)
#     print()


# ----------
# T = int(input())
# for tc in range(1, T+1):
#     n = int(input())
#     matrix = [[0] * n for i in range(n)]
#     ni, nj, di, dj = 0, 0, 0, 1

#     matrix[0][0] = 1
#     for i in range(2, n*n+1):
#         if dj == 1:
#             if nj == n-1 or matrix[ni][nj+1] != 0:
#                 di, dj = 1, 0
#         if dj == -1:
#             if nj == 0 or matrix[ni][nj-1] != 0:
#                 di, dj = -1, 0
#         if di == 1:
#             if ni == n-1 or matrix[ni+1][nj] != 0:
#                 di, dj = 0, -1
#         if di == -1:
#             if ni == 0 or matrix[ni-1][nj] != 0:
#                 di, dj = 0, 1
#         ni += di
#         nj += dj
#         matrix[ni][nj] = i
#     print(f'#{tc}')
#     for j in range(n):
#         print(*matrix[j])


# swea 1959 두 개의 숫자열
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if n == m:
        maxV = 0
        for i in range(n):
            maxV += A[i] * B[i]
    else:
        if n > m:
            total = [0] * (n-m+1)
            for i in range(len(total)):
                for j in range(-1, -m-1, -1):
                    total[i] += A[j-i] * B[j]
        else:
            total = [0] * (m-n+1)
            for i in range(len(total)):
                for j in range(-1, -n-1, -1):
                    total[i] += A[j] * B[j-i]

        total.sort()
        maxV = total[-1]
    print(f'#{tc} {maxV}')


