
import sys

sys.stdin = open('input01.txt')

# 분수찾기 1193

# n = int(input())

# line = 0
# linemax = 0

# while n > linemax:
#     line += 1
#     linemax += line

# gap = linemax - n
# if line % 2 == 0:
#     top = line - gap
#     under = gap + 1
# else:
#     top = gap + 1
#     under = line - gap
# print(f'{top}/{under}')

# -----------------
# 고무오리 디버깅 20001

# n = input()
# stk = []
# while n != '고무오리 디버깅 끝':
#     if n == '문제':
#         stk.append(n)
#     elif n == '고무오리':
#         if stk:
#             stk.pop()
#         else:
#             stk.append('문제')
#             stk.append('문제')
#     n = input()

# if stk:
#     print('힝구')
# else:
#     print('고무오리야 사랑해')


# -----------------
# 배부른 마라토너 10546

n = int(input())
p = {}
for _ in range(n):
    m = input()
    if m in p:
        p[m] += 1
    else:
        p[m] = 1

for _ in range(n-1):
    m2 = input()
    p[m2] -= 1
for k in p:
    if p[k]:
        print(k)
        break
