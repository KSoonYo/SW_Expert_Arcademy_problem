def dfs(person, height):
    global min_gap
    
    if height >= B:
        min_gap = min(min_gap, height-B)
        return

    
    for next_person in range(person+1, N):
        dfs(next_person, height + height_list[next_person])




for tc in range(1, int(input())+1):
    N, B = map(int, input().split())

    height_list = list(map(int, input().split()))

    # 만들 수 있는 높이가 B 이상인 탑 중 탑의 높이와 B 차이가 가장 작은 것
    # 조합 dfs 로 풀어보자.
    min_gap = 987654321
    for start_person in range(N):
        dfs(start_person, height_list[start_person])

    print('#{} {}'.format(tc, min_gap))