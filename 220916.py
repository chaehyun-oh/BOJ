import sys
sys.stdin = open('input01.txt')

# 1181 단어 정렬

n = int(input())
word = []
for i in range(0, n):
    word.append(input())
word = list(set(word))
word.sort()
word.sort(key=len)

for i in word:
    print(i)
