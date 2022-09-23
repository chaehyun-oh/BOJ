import sys
sys.stdin = open('input01.txt')

# 10815 숫자 카드

n = int(input())
cards = sorted(map(int, input().split()))
m = int(input())
mcards = list(map(int, input().split()))
ans = []

# 이분탐색


def bnr(n, cards, start, end):
    mid = (start + end) // 2
    if start > end:
        ans.append(str(0))
    elif n == cards[mid]:
        ans.append(str(1))
    elif n > cards[mid]:
        bnr(n, cards, mid + 1, end)
    else:
        bnr(n, cards, start, mid - 1)


for c in mcards:
    start = 0
    end = len(cards) - 1
    bnr(c, cards, start, end)

print(' '.join(ans))
