def prim(start, V):
    key = [987654321] * (V+1)
    key[start] = 0 # 출발지점 가중치 초기화
    visited = [0] * (V+1)
    parents = [0] * (V+1) # 연결한 노드의 부모노드

    for _ in range(V+1): # 노드 개수만큼 반복
        u = 0
        minV = float('INF')

        for idx in range(V+1):
            if not visited[idx] and key[idx] < minV:
                u = idx
                minV = key[idx]
        
        visited[u] = 1
        if visited[V]:
            break
              
        # 가중치값 갱신
        # 거리를 누적하면서 갱신하자!
        for i in range(V+1):
            if graph[u][i] and (not visited[i]):
                if key[i] > key[u] + graph[u][i]:
                    # 현재 인접 정점들에 기록된 값이 u 지점에서 기록된 값에 가중치를 더하여 간 값보다 크면
                    # 최소 거리 갱신
                    key[i] = key[u] + graph[u][i] 
                    parents[i] = u       

    return key[V]



    # # 마지막 노드에서부터 부모노드를 찾아 거리를 누적하여 리턴
    # child_node = V
    # total_distance = key[child_node]
    # while child_node != start: # 시작 지점에 도착할 때 까지
    #     parent = parents[child_node]
    #     total_distance += key[parent]
    #     child_node = parent

    # return total_distance 
    # => test case 8/10

for tc in range(1, int(input())+1):
    V, E = map(int, input().split()) # V : 마지막 정점 번호, E 간선 개수

    graph = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        start, end, weight = map(int, input().split())
        # 가중치가 있는 유향 그래프
        graph[start][end] = weight 

    
    result = prim(0, V)
    print('#{} {}'.format(tc, result))