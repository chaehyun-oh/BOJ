import sys

sys.stdin = open("input01.txt")
# swea 1234 비밀번호

t = 10

for tc in range(1, t + 1):
    n, pw = map(str, sys.stdin.readline().split())
    n = int(n)
    pw = list(pw)

    i = 0
    while True:
        if pw[i] == pw[i + 1]:
            del pw[i : i + 2]
            n -= 2
            i -= 2
        i += 1
        if i == (n - 1):
            break

    npw = ""
    for i in range(n):
        npw += pw[i]

    print(f"#{tc} {npw}")
