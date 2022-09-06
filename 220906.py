from pprint import pprint
import sys

sys.stdin = open('input01.txt')

# 17478 재귀함수


# def Rec(i, m):
#     print('____' * i + '"재귀함수가 뭔가요?"')
#     if i == m:
#         print('____' * i + '"재귀합수는 자기 자신을 호출하는 함수라네"')
#     else:
#         print('____' * i + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
#         print('____' * i + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
#         print('____' * i + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
#         Rec(i+1, m)
#     print('____' * i + '라고 답변하였지.')


# n = int(input())

# print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
# Rec(0, n)

# swea 1976 시각 덧셈
# T = int(input())

# for tc in range(1, T + 1):
#     h1, m1, h2, m2 = map(int, input().split())
#     if m1 + m2 >= 60:
#         h = h1 + h2 + 1
#         m = (m1 + m2) - 60
#     else:
#         h = h1 + h2
#         m = m1 + m2
#     if h > 12:
#         h -= 12
#     print(f'#{tc}', h, m)

# swea 1979 어디에 단어가 들어갈 수 있을까

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if matrix[i][j] == 1:
                cnt += 1
            if matrix[i][j] == 0 or j == n-1:
                if cnt == k:
                    ans += 1
                if matrix[i][j] == 0:
                    cnt = 0

    for i in range(n):
        cnt = 0
        for j in range(n):
            if matrix[j][i] == 1:
                cnt += 1
            if matrix[j][i] == 0 or j == n-1:
                if cnt == k:
                    ans += 1
                if matrix[j][i] == 0:
                    cnt = 0

    print(f'#{tc} {ans}')
