from pprint import pprint
import sys

sys.stdin = open('input01.txt')

# 10989 수 정렬하기

# n = int(input())

# chk = [0] * 10001

# for i in range(n):
#     input_num = int(sys.stdin.readline())

#     chk[input_num] = chk[input_num] + 1

# for i in range(10001):
#     if chk[i] != 0:
#         for j in range(chk[i]):
#             print(i)


# swea 1209 sum
# for _ in range(10):
#     tc = int(input())
#     matrix = [list(map(int, input().split())) for i in range(100)]

#     maxR = 0
#     for i in range(100):
#         s = 0
#         for j in range(100):
#             s += matrix[i][j]
#         if s > maxR:
#             maxR = s

#     maxC = 0
#     for i in range(100):
#         s = 0
#         for j in range(100):
#             s += matrix[j][i]
#         if s > maxC:
#             maxC = s

#     maxA = 0
#     for i in range(100):
#         s1, s2 = 0, 0
#         s1 += matrix[i][i]
#         s2 += matrix[i][99-i]
#     if max(s1, s2) > maxA:
#         maxA = max(s1, s2)

#     print(f'#{tc} {max(maxR, maxC, maxA)}')


# swea 1213 string

while True:
    try:
        tc = int(input())
        tg = input()
        data = input()

        ans = data.count(tg)

        print(f'#{tc} {ans}')
    except:
        break

# swea 1215
