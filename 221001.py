import sys

sys.stdin = open("input01.txt")


def mg_sort(L):
    if len(L) == 1:
        return L

    mid = (len(L) + 1) // 2

    lft = mg_sort(L[:mid])
    rht = mg_sort(L[mid:])

    i, j = 0, 0
    L2 = []

    while i < len(lft) and j < len(rht):
        if lft[i] < rht[j]:
            L2.append(lft[i])
            ans.append(lft[i])
            i += 1
        else:
            L2.append(rht[j])
            ans.append(rht[j])
            j += 1

    while i < len(lft):
        L2.append(lft[i])
        ans.append(lft[i])
        i += 1
    while j < len(rht):
        L2.append(rht[j])
        ans.append(rht[j])
        j += 1

    return L2


n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
ans = []

mg_sort(a)

if len(ans) >= k:
    print(ans[k - 1])
else:
    print(-1)
