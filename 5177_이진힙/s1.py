

tests = int(input())

for tc in range(1, tests+1):
    target_node = int(input())
    values = [0] + list(map(int, input().split()))
    v = len(values) - 1

    # 힙은 완전 이진트리
    # 새로 값을 추가하는 경우, 
    # 루트 노드 -> 왼쪽 노드 -> 오른쪽 노드 순으로 값 추가

    nodes = [0] * (v+1) # 부모 노드의 값
    # left = [0] * (v+1)
    # right = [0] * (v+1)
    
    for idx in range(1, v+1):
        nodes[idx] = values[idx] # 노드 값 추가
        parent_idx = idx // 2
        
        while parent_idx >= 1:
            if nodes[parent_idx] > nodes[idx]:
                nodes[parent_idx], nodes[idx] = nodes[idx], nodes[parent_idx]
                # print('node 변화')
                # print('nodes: ', nodes)
            idx //= 2
            parent_idx //= 2

    # print(nodes)
    total_sum = 0
    # 마지막 인덱스
    last_idx = v // 2
    while last_idx >= 1:
        total_sum += nodes[last_idx]
        last_idx //= 2

    print('#{} {}'.format(tc, total_sum))