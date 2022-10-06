import sys

sys.stdin = open("input01.txt")

# 2747 피보나치 수

d = [0] * 46


def fibo(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    if d[n] != 0:
        return d[n]
    d[n] = fibo(n - 1) + fibo(n - 2)
    return d[n]


n = int(input())
print(fibo(n))
