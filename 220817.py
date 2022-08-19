import sys

# 그룹단어 체커 1316
sys.stdin = open('input01.txt')

# n = int(input())
# cnt = n

# for _ in range(n):
#     word = input()
#     for i in range(len(word)-1):
#         if word[i] == word[i+1]:
#             pass
#         elif word[i] in word[i+1:]:
#             cnt -= 1
#             break
# print(cnt)

# 베스트셀러 1302

# T = int(sys.stdin.readline())
# bs = {}

# for _ in range(T):
#     n = sys.stdin.readline()
#     if n not in bs:
#         bs[n] = 1
#     else:
#         bs[n] = bs[n] + 1

# bs = sorted(bs.items())
# print(sorted(bs, key=lambda x: x[1], reverse=True)[0][0])

# 듣보잡 1764

# n, m = map(int, input().split())
# h = set()
# s = set()

# for i in range(n):
#     h.add(input())
# for j in range(m):
#     s.add(input())

# ans = sorted(list(h & s))
# print(len(ans))
# for k in ans:
#     print(k)
# -------------------
# d = {}
# for i in range(n):
#     k = input()
#     d[k] = 1
# for j in range(m):
#     k2 = input()
#     if k2 not in d:
#         d[k2] = 1
#     else:
#         d[k2] += 1


# def findkey(D):
#     ans = []
#     for k, v in D.items():
#         if v == 2:
#             ans.append(k)
#     return ans

# 카드 11652

# n = int(input())
# d = {}
# for _ in range(n):
#     s = int(input())
#     if d.get(s):
#         d[s] += 1
#     else:
#         d[s] = 1

# ans = 0
# maxv = 0
# lst = sorted(d.items())
# for num, cnt in lst:
#     if maxv < cnt:
#         maxv = cnt
#         ans = num
# print(ans)

# ---------
# d = {}
# for i in range(n):
#     num = int(input())
#     if num not in d:
#         d[num] = 1
#     else:
#         d[num] += 1

# maxv = 0

# for v in d.values():
#     if v > maxv:
#         maxv = v


# def getkey(v):
#     ans = 0
#     for key, value in d.items():
#         if v == value:
#             ans = key
#     return key


# print(getkey(maxv))

