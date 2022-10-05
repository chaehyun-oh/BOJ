import sys

sys.stdin = open("input01.txt")

# 1769 3의 배수


def cvt(n, cnt):
    if len(n) > 1:
        cnt += 1
        s = 0
        for i in n:
            s += int(i)
        cvt(str(s), cnt)
    else:
        if int(n) % 3 == 0:
            print(cnt)
            print("YES")
        else:
            print(cnt)
            print("NO")


n = sys.stdin.readline()
cnt = 0
cvt(n, cnt)
