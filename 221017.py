import sys

sys.stdin = open("input01.txt")

# 11279 최대 힙
import heapq

n = int(sys.stdin.readline())
mh = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(mh):
            print(heapq.heappop(mh)[1])
        else:
            print(0)
    else:
        heapq.heappush(mh, (-x, x))
