import sys

sys.stdin = open("input01.txt")

# 1914 하노이탑


def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, c)
        hanoi(n - 1, b, a, c)


n = int(input())

sum = 1
for i in range(n - 1):
    sum = sum * 2 + 1

if n <= 20:
    print(sum)
    hanoi(n, 1, 2, 3)
else:
    print(sum)
