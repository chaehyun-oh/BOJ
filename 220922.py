import sys
sys.stdin = open('input01.txt')

# 1436 영화감독 숌
n = int(input())

cnt = 0
num = 1

while True:
    if '666' in str(num):
        cnt += 1

    if cnt == n:
        print(num)
        break

    num += 1
