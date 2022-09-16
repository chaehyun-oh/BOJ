from itertools import count

import sys
sys.stdin = open('input01.txt')


# 11651 좌표 정렬하기 2
# n = int(sys.stdin.readline())
# so = []
# for i in range(n):
#     so.append(list(map(int, sys.stdin.readline().split())))
# so.sort(key=lambda x: (x[1], x[0]))
# for i in so:
#     print(i[0], i[1])

# 11718 그대로 출력

# while True:
#     try:
#         print(input())
#     except EOFError:
#         break

# 11382 꼬마 정민

# a, b, c = map(int, input().split())
# print(a+b+c)

# 2743 단어 길이 재기
# n = input()
# print(len(n))

# 2754 학점 계산

# grd = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7, 'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
#        'C+': 2.3, 'C0': 2.0, 'C-': 1.7, 'D+': 1.3, 'D0': 1.0, 'D-': 0.7, 'F': 0.0}
# n = input()
# print(grd[n])

# 10807 개수 세기

# n = int(input())
# nums = list(map(int, input().split()))
# v = int(input())
# print(nums.count(v))


# 10816 숫자 카드2

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
nums2 = list(map(int, input().split()))

cnts = {}
for i in nums:
    if i in cnts:
        cnts[i] += 1
    else:
        cnts[i] = 1

for j in nums2:
    if j in cnts:
        print(cnts[j], end=' ')
    else:
        print(0, end=' ')
