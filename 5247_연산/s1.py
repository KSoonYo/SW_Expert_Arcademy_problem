from collections import deque


for tc in range(1, int(input())+1):
    N, M = map(int, input().split()) # N: start / M: end
  
    visited = [0] * 1000001 # 중간 연산 결과는 100만 이하 자연수이므로

    # 연산 항목들
    operators = [lambda x: x+1, lambda x: x-1, lambda x: x*2, lambda x: x-10]

    min_cnt = max(N,M) - min(N,M) # 최소 횟수 초기화

    def search(start, end):
        global min_cnt
        # BFS 로 다음 탐색 가능한 노드들 살펴보기
        queue = [(start, 0)]
        visited[start] = 1
        front = -1
        rear = 0
        while front != rear:
            front += 1
            now_value, cnt = queue[front]
            
            if now_value == end:
                min_cnt = cnt
                break

            for operator in operators:
                next_value = operator(now_value)
            
                if next_value <= 0 or next_value > 1000000:
                    continue
                if next_value > len(visited)-1:
                    continue

                if not visited[next_value]:
                    queue.append((next_value, cnt+1))
                    rear += 1
                    visited[next_value] = 1

   
    search(N,M)
    print('#{} {}'.format(tc, min_cnt))


# check 용도의 visit 은 True or False가 훨씬 메모리가 덜 든다.


