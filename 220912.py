from ast import MatchClass
import numbers
from pprint import pprint
import sys

sys.stdin = open('input01.txt')

# 2108 통계학

# n = int(input())
# nums = []
# for _ in range(n):
#     nums.append(int(input()))

# print(round(sum(nums)/n))

# nums.sort()
# print(nums[int((n-1)/2)])

# cnts = dict()
# for i in range(1, n+1):
#     cnts[i] = []

# maxCnt = 1
# cnt = 1
# for j in range(1, n):
#     if nums[j] == nums[j-1]:
#         cnt += 1
#     else:
#         cnts[cnt].append(nums[j-1])
#         if maxCnt < cnt:
#             maxCnt = cnt
#         cnt = 1
#     if j == n-1:
#         cnts[cnt].append(nums[j])
#         if maxCnt < cnt:
#             maxCnt = cnt

# if n == 1:
#     cnts[1].append(nums[0])

# cnts[maxCnt].sort()
# if len(cnts[maxCnt]) == 1:
#     print(cnts[maxCnt][0])
# else:
#     print(cnts[maxCnt][1])

# print(nums[-1]-nums[0])

# swea 1217 거듭 제곱

# for tc in range(1, 11):
#     test_case = int(input())
#     a, b = map(int, input().split())

#     print(f'#{tc} {a**b}')

# swea 1220 magnetic
for tc in range(1, 11):
    n = int(input())
    mag = [list(map(int, input().split())) for _ in range(n)]  # 1: N, 2: S

    total_res = 0
    for i in range(n):
        flag = 0
        for j in range(n):
            if mag[j][i] == 1:
                flag = 1
            elif mag[j][i] == 2:
                if flag:
                    total_res += 1
                    flag = 0

    print(f'#{tc} {total_res}')
