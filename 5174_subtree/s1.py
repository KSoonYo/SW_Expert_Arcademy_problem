# import sys

tests = int(input())


# 전위 순회 함수
def pre_order(t, cnt):
    if t:
        cnt += 1
        cnt = pre_order(left[t], cnt)
        cnt = pre_order(right[t], cnt)
    return cnt

for tc in range(1, tests+1):
    e, sub_root = map(int, input().split())
    v = e + 1
    edge = list(map(int, input().split()))

    # 자식 노드들
    left = [0] * (v+1)
    right = [0] * (v+1)


    # 간선 연결 짓기
    # 부모 인덱스로 자식 노드 번호 연결
    for i in range(e):
        p, c = edge[i * 2], edge[i * 2 + 1]
        if not left[p]: 
            left[p] = c  
        else:
            right[p] = c
    
    # sub_root 노드부터 시작하여 자식 노드들의 개수를 count
    # 전위 순회 방식 사용
    cnt = 0
    result = pre_order(sub_root, cnt)
    print(f'#{tc} {result}')
    
