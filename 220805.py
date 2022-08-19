# T = int(input())

# for _ in range(T):
# n, word = input().split()
n = '5'
word = '/HTP'
n = int(n)
for i in range(len(word)):
    nword = ''
    nword += word[i]*n
    print(word[i]*n, end='')
    # print(nword)


t = int(input())
for i in range(t):
    num, s = input().split()
    text = ''
    for i in s:
        text += int(num) * i
    print(text)
