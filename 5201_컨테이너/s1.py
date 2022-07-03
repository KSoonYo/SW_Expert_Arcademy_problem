
for tc in range(1, int(input())+1):
    # N: 컨테이너 수 | M : 트럭 수
    N, M = map(int, input().split())

    w = list(map(int, input().split()))
    t = list(map(int, input().split()))

    # 내림차순으로 정렬
    w.sort(reverse=True)
    t.sort(reverse=True)

    # print('w', w)
    # print('t', t)
    total = 0
    standard = min(N,M)
    wi = ti = 0
    while True:
        if wi > (N-1) or ti > (M-1):
            break

        if  w[wi] <= t[ti]:
            total += w[wi]

        else:
            wi += 1
            continue
        wi += 1
        ti += 1
    print('#{} {}'.format(tc, total))
    

'''
solution

import sys
sys.stdin = open('input.txt')
"""
ti : 트럭이 허용가능한 무게 배열
wi : 무게의 배열

가장 낮은 무게가 허용 가능한 트럭부터
가능한 가장 무거운 화물을 가져갈 수 있게끔 반복문 작성
이동된 화물은 remove 함수로 제외
"""

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))
    wi.sort(reverse=True)
    ti.sort()
    weight = 0

    for t in ti:
        for w in wi:
            if t >= w:
                weight += w
                wi.remove(w)
                break
    print("#{} {}".format(tc, weight))

'''

        