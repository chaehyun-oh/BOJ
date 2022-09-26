import sys

sys.stdin = open("input01.txt")

# 10828 스택
n = int(sys.stdin.readline())
stk = []
for i in range(n):
    comd = sys.stdin.readline().split()

    if comd[0] == "push":
        stk.append(comd[1])
    elif comd[0] == "pop":
        if len(stk) == 0:
            print(-1)
        else:
            print(stk.pop())
    elif comd[0] == "size":
        print(len(stk))
    elif comd[0] == "empty":
        if len(stk) == 0:
            print(1)
        else:
            print(0)
    elif comd[0] == "top":
        if len(stk) == 0:
            print(-1)
        else:
            print(stk[-1])
