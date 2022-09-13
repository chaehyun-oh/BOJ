from pprint import pprint
import sys

sys.stdin = open('input01.txt')

# 1427 소트인사이드

# n = input()
# nums = []
# for i in n:
#     nums.append(int(i))
# nums.sort(reverse=True)
# for j in nums:
#     print(j, end='')

# swea 1221 GNS

# T = int(input())
# nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

# for tc in range(1, T+1):
#     num, n = input().split()
#     arr = list(input().split())

#     for i in range(int(n)):
#         arr[i] = nums.index(arr[i])

#     arr.sort()
#     for j in range(int(n)):
#         arr[j] = nums[arr[j]]

#     print(f'#{tc}')
#     print(*arr)

# swea 1225 암호생성기


def psw(lst):
    while True:
        for i in range(1, 6):
            num = lst.pop(0)
            lst.append(num - i)

            if lst[-1] <= 0:
                lst[-1] = 0
                return lst


for _ in range(1, 11):
    tc = int(input())
    nums = list(map(int, input().split()))

    ans = psw(nums)
    print(f'#{tc}', *ans)
