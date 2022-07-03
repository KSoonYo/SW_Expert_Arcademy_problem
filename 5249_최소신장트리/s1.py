# PRIM 알고리즘으로 MST 구성하기
def prim(start, V):
    '''
    start : 시작 노드
    V : 마지막 노드
    '''
    
    key = [98765421] * (V+1)
    key[start] = 0 # 시작노드의 가중치는 0

    visited = [0] * (V+1)
    parents = [0] * (V+1) # 노드의 부모노드 저장하는 리스트


    for _ in range(V+1): # 노드의 개수만큼 반복
        u = start
        minV = float('INF')

        # 방문하지 않은 노드들 중 최소 가중치인 것을 선택
        for idx in range(V+1):
            if not visited[idx] and key[idx] < minV:
                u = idx
                minV = key[idx]

        visited[u] = 1 # 방문 처리

        # 방문처리한 노드와 인접한 노드들의 가중치 갱신
        for node_idx in range(V+1):
            if nodes[u][node_idx] and (not visited[node_idx]):
                if key[node_idx] > nodes[u][node_idx]:
                    key[node_idx] = nodes[u][node_idx]
                    parents[node_idx] = u # u 노드를 부모 노드로 

    return sum(key) # 가중치 최소합 return

for tc in range(1, int(input())+1):
    # 노드는 0번부터 V번까지 존재
    V, E = map(int, input().split()) # V: 마지막 노드 번호, E: 간선 개수
    

    # 그래프 가중치 입력받기
    nodes = [[0] * (V+1) for _ in range(V+1)] 
    for _ in range(E):
        start, end, weight = map(int, input().split())
        nodes[start][end] = nodes[end][start] = weight

    result = prim(0, V) # 0번 노드부터 시작
    print('#{} {}'.format(tc, result))
