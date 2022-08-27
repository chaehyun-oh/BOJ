from pprint import pprint
import sys

sys.stdin = open('input01.txt')

# 몬스터 트럭 2897

# dr = [0, 1, 1]
# dc = [1, 1, 0]
# bd = '#'
# pc = 'X'
# pk = '.'

# r, c = map(int, input().split())
# matrix = []
# for _ in range(r):
#     matrix.append(list(input()))

# brkcnt = [0]*5

# for i in range(r):
#     for j in range(c):
#         cnt = 0
#         if matrix[i][j] == bd:
#             continue

#         if matrix[i][j] == pc:
#             cnt += 1

#         for k in range(3):
#             nextR = i + dr[k]
#             nextC = j + dc[k]

#             if not (-1 < nextR < r and -1 < nextC < c):
#                 break

#             if matrix[nextR][nextC] == bd:
#                 break

#             if matrix[nextR][nextC] == pc:
#                 cnt += 1
#         else:
#             brkcnt[cnt] += 1

# for c in brkcnt:
#     print(c)


# 촌수계산 2644

n = int(input())
a, b = list(map(int, input().split()))
m = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False] * (n + 1)

stk = []
stk.append((a, 0))
visited[a] = True

ans = -1

while len(stk) != 0:
    num, cnt = stk.pop()

    if num == b:
        ans = cnt
        break

    adj_graph = graph[num]

    for adj_num in adj_graph:
        if not visited[adj_num]:
            stk.append((adj_num, cnt + 1))
            visited[adj_num] = True

print(ans)
