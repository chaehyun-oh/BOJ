from pprint import pprint
import sys

sys.stdin = open('input01.txt')

# 큰 수 a+b 10757

# a, b = map(int, input().split())
# print(a+b)

# 오목 2615
# dx = [0, 1, 1, 1, 0, -1, -1, -1]
# dy = [1, 1, 0,  -1, -1, -1, 0, 1]

# n = 19
# dx = [0, 1, -1, 1]
# dy = [1, 0, 1, 1]
# matrix = [list(map(int, input().split()))for _ in range(n)]

# # matrix = []
# # for _ in range(n):
# #     lst = list(map(int, input().split()))
# #     matrix.append(lst)

# ans = 0
# for x in range(n):
#     for y in range(n):
#         if matrix[y][x] == 1 or matrix[y][x] == 2:
#             for d in range(4):
#                 cnt = 1
#                 nx = x + dx[d]
#                 ny = y + dy[d]

#                 while True:
#                     if not (-1 < ny < n and -1 < nx < n):
#                         break

#                     if (matrix[y][x] != matrix[ny][nx]):
#                         break

#                     cnt += 1
#                     nx = nx + dx[d]
#                     ny = ny + dy[d]

#                 if cnt == 5:
#                     prevX = x - dx[d]
#                     prevY = y - dy[d]

#                     if not (-1 < prevY < n and -1 < prevX < n) or matrix[y][x] != matrix[prevY][prevX]:
#                         print(matrix[y][x])
#                         print(y + 1, x + 1)
#                         ans = matrix[y][x]
#                         exit(0)
#                     # nx += dx[d]
#                     # ny += dy[d]
# if ans == 0:
#     print(ans)

# ---------------------
# board = []
# for i in range(19):
#     board.append(list(map(int, input().split())))


# dx = [0, 1, 1, -1]
# dy = [1, 0, 1, 1]

# for x in range(19):
#     for y in range(19):
#         if board[x][y] != 0:
#             focus = board[x][y]

#             for i in range(4):
#                 cnt = 1
#                 nx = x + dx[i]
#                 ny = y + dy[i]

#                 while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == focus:
#                     cnt += 1

#                     if cnt == 5:

#                         if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and board[x - dx[i]][y - dy[i]] == focus:
#                             break
#                         if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and board[nx + dx[i]][ny + dy[i]] == focus:
#                             break

#                         print(focus)
#                         print(x + 1, y + 1)
#                         sys.exit(0)

#                     nx += dx[i]
#                     ny += dy[i]

# print(0)

# -----------
# 미로탐색 2178
# BFS
# n, m = map(int, input().split())

# matrix = []
# for _ in range(n):
#     matrix.append(list(input()))

# visited = [[0]*m for _ in range(n)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# q = [(0, 0)]
# visited[0][0] = 1

# while q:

#     x, y = q.pop(0)
#     # y = q.pop(0)

#     if x == n-1 and y == m-1:
#         print(visited[x][y])
#         break

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if 0 <= nx < n and 0 <= ny < m:
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < m:
#                 if visited[nx][ny] == 0 and matrix[nx][ny] == '1':
#                     visited[nx][ny] = visited[x][y] + 1
#                     q.append((nx, ny))
