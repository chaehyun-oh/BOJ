import sys

sys.stdin = open("input01.txt")
# 1966 프린터 큐

T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))
    qo = [0 for i in range(n)]
    qo[m] = 1
    cnt = 0
    while True:
        if q[0] == max(q):
            cnt += 1
            if qo[0] == 1:
                print(cnt)
                break
            else:
                del q[0]
                del qo[0]
        else:
            q.append(q[0])
            del q[0]
            qo.append(qo[0])
            del qo[0]
