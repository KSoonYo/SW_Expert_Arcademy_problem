import sys



# tests = int(input())


# def middle_search(n, max_height, max_value, now_node=1, now_height=1):
#     if n > max_value:
#         return n
#     if now_height <= max_height:
#         now_height += 1
#         next_left = now_node * 2
#         next_right = now_node * 2 + 1   
#         print('왼쪽 자식 노드 탐색')
#         n = middle_search(n, max_height, max_value, next_left , now_height)
        
#         print('now_value: ', n)
#         print('now height: ', now_height-1)
#         print('now_node: ', now_node)
#         nodes[now_node] = n        
#         n += 1

#         print('오른쪽 자식노드 탐색')
#         n = middle_search(n, max_height, max_value, next_right, now_height) 

#     return n
    
# for tc in range(1, tests+1):
#     N = int(input()) # 정점 개수 
#     # 트리 초기화
#     nodes = [0] * (1000)

#     # root 노드의 value는 1, 2, 4, 8, 16 .... 2 ^ height
#     # N // 2 을 1이 될 때까지 하여 높이를 구한다. 
#     last_leaf = N
#     cnt = 0
#     while last_leaf >= 1:
#         cnt += 1
#         last_leaf //= 2

#     max_height = cnt
#     # 중위 순회로 값 채워넣기 (1 부터 N 까지)
#     # 높이로 단계를 구분
#     print('max height: ', max_height)
#     middle_search(1, max_height, N)


#     # 현재 트리의 최상단 root 노드 값 =  2 ^ (현재 트리 최대 높이-1)
#     root_value = 2 ** (max_height-1)
#     # N//2 번 노드 값(M번째 노드의 부모 노드 값)
#     result = nodes[N//2]
#     print(f'#{tc} {root_value} {result}')



def in_order(n, value, max_value):
    
    if n <= max_value:
        value = in_order(2*n, value, max_value)
        nodes[n] = value
        value += 1
        value = in_order((2*n)+ 1, value, max_value)

    return value


tests = int(input())

for tc in range(1, tests+1):
    N = int(input()) # 정점 개수 
    # 트리 초기화
    nodes = [0] * (N+1)
    in_order(1, 1, N)
    print(f'#{tc} {nodes[1]} {nodes[N//2]}')

