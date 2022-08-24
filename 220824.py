import sys

sys.stdin = open('input01.txt')

# 부녀회장 2775

# T = int(input())
# for _ in range(T):
#     k = int(input())
#     n = int(input())
#     f0 = [x for x in range(1, n+1)]
#     for fl in range(k):
#         for i in range(1, n):
#             f0[i] += f0[i - 1]
#     print(f0[-1])

# ----------
# 5와 6의 차이 2864

# a, b = input().split()
# mn = int(a.replace('6', '5')) + int(b.replace('6', '5'))
# mx = int(a.replace('5', '6')) + int(b.replace('5', '6'))
# print(mn, mx)

# ------------
# 상금헌터 15953

# fst = [500, 300, 200, 50, 30, 10]
# snd = [512, 256, 128, 64, 32]

# fstP = [0] + [fst[i] for i in range(6) for _ in range(i+1)]
# sndP = [0] + [snd[i] for i in range(5) for _ in range(2**i)]

# T = int(input())

# for _ in range(T):
#     a, b = map(int, input().split())
#     if a >= len(fstP):
#         a = 0
#     if b >= len(sndP):
#         b = 0
#     print((fstP[a]+sndP[b])*10000)

# 붕어빵 11945
n, m = map(int, input().split())
b = ''
for _ in range(n):
    b = input()
    print(b[::-1])
