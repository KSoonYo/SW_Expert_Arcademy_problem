import sys


sys.stdin = open('sample_input.txt')

tests = int(input())

def post_order(n, N):
    if n <= N:
        num1 = post_order(2*n, N)
        num2 = post_order(2*n+1, N)
        nodes[n] += (num1+num2)
        return nodes[n]
    return 0


for tc in range(1, tests+1):
    N, M, L = map(int, input().split())
    nodes = [0] * (N+1)
    
    # leaf 노드 채우기
    for _ in range(M):
        node_idx, value = map(int, input().split())
        nodes[node_idx] = value

    # 후위 순회로 값을 채우면서 올라오기
    post_order(1, N)
    print('#{} {}'.format(tc, nodes[L]))