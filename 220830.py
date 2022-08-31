from pprint import pprint
import sys

sys.stdin = open('input01.txt')

# 소인수분해 11653

# n = int(input())
# i = 2
# while n != 1:
#     if n % i == 0:
#         print(i)
#         n = n/i
#     else:
#         i += 1

# swea 1204 최빈수

# T = int(input())
# for tc in range(T):
#     casenum = int(input())
#     scores = list(map(int, input().split()))
#     cnt = {}

#     for score in scores:
#         score = str(score)
#         cnt[score] = cnt.get(score, 0) + 1

#     idx = max(cnt.values())

#     for k, v in cnt.items():
#         if v == idx:
#             print(f'#{casenum} {k}')

# swea 1288 불면증 치료

# T = int(input())

# for test_case in range(1, T + 1):
#     n = int(input())
#     n1 = n
#     nums = set()

#     while True:
#         for i in str(n):
#             nums.add(i)
#         if len(nums) == 10:
#             break
#         n += n1
#     print(f'#{test_case} {n}')


# swea 1859 백만장자
# T = int(input())

# for tc in range(1, T+1):
#     n = int(input())
#     nums = list(map(int, input().split()))
#     maxV = nums[-1]
#     p = 0

#     for i in range(n-2, -1, -1):
#         if nums[i] >= maxV:
#             maxV = nums[i]
#         else:
#             p += maxV - nums[i]

#     print(f'#{tc} {p}')

# swea 1926 간단한 369
# T = int(input())

# for t in range(1, T + 1):
#     t = str(t)
#     c = t.count('3') + t.count('6') + t.count('9')

#     if c == 0:
#         print(t, end=' ')
#     else:
#         print('-' * c, end=' ')

# swea 1928
dc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
      'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']

T = int(input())
for tc in range(1, T+1):
    word = input()
    v = ''
    for i in range(len(word)):
        num = dc.index(word[i])
        b = str(bin(num)[2:])

        while len(b) < 6:
            b = '0' + b
        v += b
    ans = ''
    for j in range(len(word)*6 // 8):
        d = int(v[j*8: j*8+8], 2)
        ans += chr(d)

    print(f'#{tc} {ans}')
