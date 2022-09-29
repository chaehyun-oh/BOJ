import sys

sys.stdin = open("input01.txt")

# 2851 슈퍼마리오

total = 0
result = [int(sys.stdin.readline()) for _ in range(10)]

for i in result:
    total += i
    if total >= 100:
        if total - 100 > 100 - (total - i):
            total -= i
            break
print(total)
