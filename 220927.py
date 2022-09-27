import sys

sys.stdin = open("input01.txt")

# 1874 스택 수열

n = int(sys.stdin.readline())
stk = []
p = []
cnt = 1
tmp = True
for i in range(n):
    a = int(sys.stdin.readline())
    while cnt <= a:
        stk.append(cnt)
        p.append("+")
        cnt += 1
    if stk[-1] == a:
        stk.pop()
        p.append("-")
    else:
        tmp = False
if tmp == False:
    print("NO")
else:
    for j in p:
        print(j)
