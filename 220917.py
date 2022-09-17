from os import sep
import sys
sys.stdin = open('input01.txt')

# 10814 나이순 정렬

# n = int(sys.stdin.readline())
# mem = []
# for i in range(n):
#     mem.append(list(sys.stdin.readline().split()))
# mem.sort(key=lambda x: int(x[0]))
# for i in range(n):
#     print(mem[i][0], mem[i][1])

# 20291 파일 정리

n = int(sys.stdin.readline())
files = {}
for i in range(n):
    ex = (input().split('.'))[1]
    if not ex in files:
        files[ex] = 1
    else:
        files[ex] += 1

fileSort = sorted(files.items())

for k, v in fileSort:
    print(k, v)
