from pprint import pprint
import sys

sys.stdin = open('input01.txt')

# 소수 2581
# n = int(input())
# m = int(input())
# ans = []
# for i in range(n, m+1):
#     error = 0
#     if i > 1:
#         for j in range(2, i):
#             if i % j == 0:
#                 error += 1
#                 break
#         if error == 0:
#             ans.append(i)

# if len(ans) > 0:
#     print(sum(ans))
#     print(min(ans))
# else:
#     print(-1)

# swea1545 거꾸로 출력
# a = int(input())
# for i in range(a+1):
#     print(a-i, end=' ')

# swea 1936 가위바위보

# a, b = map(int, input().split())
# if a == 1:
#     if b == 2:
#         print('B')
#     elif b == 3:
#         print('A')
# elif a == 2:
#     if b == 1:
#         print('A')
#     elif b == 3:
#         print('B')
# elif a == 3:
#     if b == 1:
#         print('B')
#     elif b == 2:
#         print('A')

# swea 1938 아주 간단한 계산기

# a, b = map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)

# swea 2025 n줄 덧셈

# a = int(input())
# print(int(a*(a+1)/2))

# swea 2027 대각선 출력

# for i in range(5):
#     for j in range(5):
#         if i == j:
#             print('#', end='')
#         else:
#             print('+', end='')
#     print()


# swea 2043

# p, k = map(int, input().split())
# print((p - k)+1)

# swea 2046

# n = int(input())
# print('#'*n)

# swea 2047 헤드라인

# n = input()
# print(n.upper())

# swea 2050 알파벳 변환

# n = input()
# # for i in range(len(n)):
# #     print(i+1, end=' ')
# for i in n:
#     print(ord(i)-64, end=' ')

# swea 2056 연월일 달력

# T = int(input())

# m = ['01', '03', '05', '07', '08', '10', '12']
# for tc in range(1, T+1):
#     n = input()
#     if n[4:6] == '02':
#         if int(n[6::]) > 28:
#             print(f'#{tc} -1')
#         else:
#             print(f'#{tc} {n[0:4]}/{n[4:6]}/{n[6::]}')
#     elif n[4:6] in m:
#         if int(n[6::]) > 31:
#             print(f'#{tc} -1')
#         elif int(n[6::]) <= 0:
#             print(f'#{tc} -1')
#         else:
#             print(f'#{tc} {n[0:4]}/{n[4:6]}/{n[6::]}')
#     elif int(n[4:6]) <= 0:
#         print(f'#{tc} -1')
#     else:
#         if int(n[6::]) > 30:
#             print(f'#{tc} -1')
#         else:
#             print(f'#{tc} {n[0:4]}/{n[4:6]}/{n[6::]}')

# swea 2058 자릿수 더하기

# n = input()
# ans = 0
# for i in n:
#     ans += int(i)
# print(ans)

# swea 2063 중간값

# n = int(input())
# nums = list(map(int, input().split()))
# nums.sort()
# ans = int(n//2)
# print(nums[ans])

# swea 2068 최대수 구하기

# T = int(input())
# for tc in range(1, T+1):
#     nums = list(map(int, input().split()))
#     print(f'#{tc} {max(nums)}')


# swea 2072 홀수만 더하기
T = int(input())

for tc in range(1, T+1):
    nums = list(map(int, input().split()))
    ans = 0
    for n in nums:
        if n % 2 != 0:
            ans += n
    print(f'#{tc} {ans}')
