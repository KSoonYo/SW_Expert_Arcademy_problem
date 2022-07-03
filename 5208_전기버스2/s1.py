import sys

sys.stdin = open('input.txt')

def get_minV(start, end, minC, cnt):

    # 현재 정류장이 출발지가 아니라면 cnt += 1(현재 정류장에서 교체했다고 가정)
    if start > 1:
        cnt += 1

    if cnt >= minC:
        return minC
    
    if start == end:
        return min(minC, cnt)
    

    # print('start', start)
    # 현재 출발 정류장에서 갈 수 있는 모든 다음 정류장들을 다음 출발지점으로 탐색
    next_nodes = []
    for next in range(1, node_info[start]+1):
        # 다음 노드 중에 목적지가 있다면 곧바로 return
        next_node = start + next
        if next_node == end:
            return cnt
        next_nodes.append(next_node)

    next_nodes = sorted(next_nodes, key=lambda x: -node_info[x])
    # print('next nodes', next_nodes)
    for go in next_nodes:
        return_value = get_minV(go, end, minC, cnt)
        minC = min(minC, return_value)
    return minC


for tc in range(1, int(input())+1):
    input_data = list(map(int, input().split()))
    N = input_data[0]
    
    # 각 정류장에서 베터리를 충전할 때 최대 갈 수 있는 거리 정보
    # 마지막 인덱스는 도착 노드
    node_info = [0] + input_data[1:] + [0] # 1에서 출발, 1에서 갈 수 있는 모든 정류장들이 다음 노드

    # 출발지점 : 1
    # 종점 : len(M)-1 
    start = 1
    end = len(node_info) - 1
    # print('end', end)
    flag = False
    result = get_minV(start, end, len(node_info)**2, 0)
    print('#{} {}'.format(tc, result))



