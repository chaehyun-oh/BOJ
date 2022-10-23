import sys

sys.stdin = open("input01.txt")

s = []
for i in range(28):
    s.append(int(input()))
s = sorted(s)
for i in range(1, 31):
    if i not in s:
        print(i)
