tests = int(input())

for tc in range(1, tests+1):
    # N : 오는 사람 수
    # M: 붕어빵을 만드는 데 걸리는 시간
    # K: M초 후 만들어지는 붕어빵 개수
    N,M,K = map(int, input().split())

    # 0초 이후 t초에 오는 사람들
    people = list(map(int, input().split()))

    # 일찍 오는 사람들 순 대로 정렬
    people.sort()

    status = 'Possible'
    
    # 현재의 붕어빵 개수
    bung_fish = 0

    # 서빙 횟수
    serving = 0

    t = 0
    while serving < N:
        if t > 0 and t % M == 0:
            bung_fish += K

        # 현재 t초에 온 사람들 count
        cnt = 0
        for i in range(N):
            if t == people[i]:
                cnt += 1
        
        # 현재의 붕어빵 개수가 현 순간에 온 사람들보다 적다면 Impossible
        if bung_fish < cnt:
            status = 'Impossible'
            break
        else:
            bung_fish -= cnt
            serving += cnt

        t += 1

    print('#{} {}'.format(tc, status))
