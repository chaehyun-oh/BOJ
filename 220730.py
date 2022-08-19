# 4344 평균
# testcase = [5, 50, 50, 70, 80, 100]

# total = sum(testcase) - testcase[0]
# avrg = int (total / testcase[0])

C = int(input())
for _ in range(C):
    scores = list(map(int, input().split()))
    total = sum(scores) - scores[0]
    avrg = total / scores[0]
    print(avrg)

    cnt = 0

    for i in range(1, len(scores)):
        if scores[i] > avrg:
            cnt += 1
            print(cnt)
    rate = cnt / scores[0] * 100
    print(f'{rate: .3f}%')