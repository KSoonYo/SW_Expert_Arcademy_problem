def prim(start):
    key = [float('inf')] * N
    key[0] = 0 # 출발 지점의 비용
    connected = [0] * (N+1)
    
    for _ in range(N):
        to_island = 0
        min_cost = float('INF')
        
        # 방문지점 선택
        for i in range(N):
            if (not connected[i]) and key[i] < min_cost:
                to_island = i
                min_cost = key[i]

        connected[to_island] = 1
        
        # 방문한 노드의 인접 노드 가중치 갱신
        for j in range(N):
            if island_info[to_island][j] and (not connected[j]):
                if key[j] > island_info[to_island][j]:
                    key[j] = island_info[to_island][j]
        
    return sum(key)

for tc  in range(1, int(input())+1):
    # 0번 섬부터 N-1번 섬까지
    N = int(input()) # N: 섬의 개수


    island_info = [[0] * (N) for _ in range(N)]
    x = []
    y = []

    for matrix in range(2):
        if not matrix:
            x = list(map(int ,input().split()))
        
        else:
            y = list(map(int ,input().split()))

    E = float(input()) # 세율 입력

    # A 섬과 B 섬을 잇기 위한 비용을 가중치로 하여 island_info에 기록
    for start_idx in range(N):
        for end_idx in range(N):
            if start_idx == end_idx:
                continue
            L = ((x[start_idx] - x[end_idx]) ** 2 + (y[start_idx] - y[end_idx]) ** 2) ** (1/2)
            cost = E * (L ** 2)
            island_info[start_idx][end_idx] = cost


    # 0번 섬부터 출발한다고 가정
    # MST를 구성
    result = prim(0)
    print('#{} {}'.format(tc, round(result)))

