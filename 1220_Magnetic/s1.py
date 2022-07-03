
for tc in range(1, 11):
    N = int(input())

    magnetic_map = [list(map(int, input().split())) for _ in range(N)]

    # N극
    # 1: N극 성질  
    # 2: S극 성질
    # S극

    # 1은 row 위치가 +1
    # 2는 row 위치가 -1


    # 한 열씩 탐색
    # 한 열에 요소가 하나라면? => 교착상태 없음 skip
    # 한 열에 요소가 두 개 이상이라면
    # 교착상태란 아래의 모양
    ## N (1)
    ## S (2)
    # 그 열을 한 줄씩 탐색하면서 
    # 처음 만나는 자성체를 기억해두고
    # 이전에 만난 자성체가 N극이고 다음에 만난 자성체가 S극일 때
    # 이를 교착상태로 보고 +1 을 해준다.

    # 이때 0행에 2가 있거나 N-1행에 1이있으면 교착의 가능성이 없으므로 자성체를 기억하지 않는다.

    # 전치를 시켜서 쉽게 해보자.(위 풀이에서 행 -> 열, 열 -> 행으로 하면 된다.)
    magnetic_T = list(zip(*magnetic_map))

    stop = 0
    for row_idx in range(N):
        if magnetic_T[row_idx].count(1) + magnetic_T[row_idx].count(2) == 1:
            continue

        magnetic = 0
        for col_idx in range(N):
            if col_idx == 0 and magnetic_T[row_idx][col_idx] == 2:
                continue
            if col_idx == (N-1) and magnetic_T[row_idx][col_idx] == 1:
                continue
            
            if magnetic == 1 and magnetic_T[row_idx][col_idx] == 2:
                # 교착 상태 
                stop += 1
            
            if magnetic_T[row_idx][col_idx]:
                magnetic = magnetic_T[row_idx][col_idx]
                
    print('#{} {}'.format(tc, stop))






