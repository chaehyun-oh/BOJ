# 4673 셀프넘버
# 셀프넘버: 생성자가 없는 숫자

# def d(n):
#     nsum = n
#     n = str(n)
#     for i in range(len(n)):
#         nsum += int(n[i])
#     return nsum

#---- 

# def d(n):
#     n = n + sum(map(int, str(n)))
#     return n

# nonSN = set()

# for i in range(1, 10001):
#     nonSN.add(d(i))

# for j in range(1, 10001):
#     if j not in nonSN:
#         print(j)


# 2511 카드놀이

# A = [4, 5, 6, 7, 0, 1, 2, 3, 9, 8]
# B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# A= list(map(int, input().split()))
# B = list(map(int, input().split()))
# totalA = 0
# totalB = 0

# if A == B:
#     print(10, 10)
#     print('D')
# else:
#     for i in range(10):
#         if A[i] > B[i]:
#             totalA += 3
#             win = 'A'
#         elif A[i] < B[i]:
#             totalB += 3
#             win = 'B'
#         else:
#             totalA += 1
#             totalB += 1
#     print(totalA, totalB)
#     if totalA == totalB:
#         print(win)
#     else:
#         print('A' if totalA > totalB else 'B')


# 10798 세로 읽기

wlist = []
leng = []
for _ in range(5):
    word = input()
    # words = [input() for i in range(5)]
    wlist.append(word)
    leng.append(len(word)) # 각 문자들의 길이 저장

line = ''
for i in range(max(leng)):
    for j in range(5):
        if i < leng[j]:
            line += wlist[j][i]
            #wlist[0][0] > wlist[1][0] 순서로 더해 나감

print(line)