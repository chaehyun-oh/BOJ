from pprint import pprint
import sys

sys.stdin = open('input01.txt')

# 2751 수 정렬하기2

# n = int(input())
# nums = []
# for i in range(n):
#     nums.append(int(input()))
# for j in sorted(nums):
#     print(j)

# swea 2007 패턴 마디 길이

# T = int(input())

# for tc in range(1, T+1):
#     word = input()
#     for i in range(1, 10):
#         if word[:i] == word[i:i * 2]:
#             print(f'#{tc} {i}')
#             break


# swea 1206 View

# for tc in range(1, 11):
#     n = int(input())
#     bd = list(map(int, input().split()))
#     ans = 0

#     for i in range(2, n - 2):
#         if bd[i] > bd[i - 1] and bd[i] > bd[i - 2] and bd[i] > bd[i + 1] and bd[i] > bd[i + 2]:
#             maxH = bd[i - 2]

#             for j in range(-2, 3):
#                 if j == 0:
#                     continue
#                 if bd[i - j] > maxH:
#                     maxH = bd[i - j]

#             ans += bd[i] - maxH

#     print(f'#{tc} {ans}')

# swea 1208 평탄화
T = 10

for test_case in range(1, T+1):
    dmp = int(input())
    boxs = list(map(int, input().split()))
    n = len(boxs)

    total = int(sum(boxs) / n)

    while dmp:
        mx = max(boxs)
        mn = min(boxs)
        x = boxs.index(mx)
        y = boxs.index(mn)
        boxs[x] -= 1
        boxs[y] += 1
        dmp -= 1

    print(f'#{test_case}', max(boxs) - min(boxs))
