from pprint import pprint
import sys

sys.stdin = open('input01.txt')

# 25305 커트라인

# n, k = map(int, input().split())
# scores = list(map(int, input().split()))
# scores.sort(reverse=True)
# print(scores[k-1])

# swea 1215 회문

# T = 10
# m = 8
# for tc in range(1, T+1):
#     n = int(input())
#     matrix = []
#     ans = 0

#     for _ in range(m):
#         line = input()
#         matrix.append(line)
#         for i in range(m - n + 1):
#             if line[i:i+n] == line[i:i+n][::-1]:
#                 ans += 1
#     matrix = list(zip(*matrix))

#     for i in range(m):
#         for j in range(m - n + 1):
#             if matrix[i][j:j+n] == matrix[i][j:j+n][::-1]:
#                 ans += 1

#     print(f'#{tc} {ans}')

# swea 1216 회문 2


def chk(arr):
    for i in range(len(arr)//2):
        if arr[i] != arr[-i-1]:
            return False
    return True


for tc in range(1, 11):
    t = int(input())
    arr = [list(input()) for _ in range(100)]
    arr2 = list(zip(*arr))
    maxV = 1

    for lng in range(100, 1, -1):
        if maxV >= lng:
            break
        for idx in range(100-lng+1):
            if maxV == lng:
                break
            for a1, a2 in zip(arr, arr2):
                if chk(a1[idx:idx+lng]) or chk(a2[idx:idx+lng]):
                    maxV = lng
                    break
    print('#{} {}'.format(tc, maxV))

# swea 1217
