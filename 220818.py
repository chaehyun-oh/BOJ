import sys

sys.stdin = open('input01.txt')
# ---------
# 체스말 3003

# chess = list(map(int, input().split()))
# ans = [1, 1, 2, 2, 2, 8]
# res = [0, 0, 0, 0, 0, 0]

# for i in range(len(chess)):
#     if chess[i] == ans[i]:
#         res[i] = 0
#     elif chess[i] > ans[i]:
#         res[i] = -(chess[i] - ans[i])
#     elif chess[i] < ans[i]:
#         res[i] = ans[i] - chess[i]
# print(*res)

# KMP 2902
# word = input().split('-')
# ans = ''
# for i in range(len(word)):
#     ans += word[i][0]
# print(ans)

# -------------------
# 우유축제 14720
# n = int(input())
# shop = list(map(int, input().split()))
# cnt = 0
# num = 0
# for i in range(n):
#     if shop[i] == num:
#         cnt += 1
#         num += 1
#     if num > 2:
#         num = 0
# print(cnt)

# for i in range(n):
#     if shop[i] == cnt % 3:
#         cnt += 1
# print(cnt)

# ------------
# 저항 1076
# res = ['black', 'brown', 'red', 'orange', 'yellow',
#        'green', 'blue', 'violet', 'grey', 'white']
# w = []
# for _ in range(3):
#     w.append(input())

# ans = ''

# for i in w:
#     ans += str(res.index(i))
# r = int(ans[0:2])
# c = int(ans[2])

# result = 0
# result = r * (10**c)
# print(result)
