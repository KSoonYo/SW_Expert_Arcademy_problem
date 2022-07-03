
'''
test case 9/10

'''

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    numbers = list(range(1,N+1))

    # 신청서
    requests = list(map(int, input().split()))
    request_set = []

    # 신청서 set 제작(2개씩 짝을 지어서)
    for num_idx in range(0, len(requests), 2):
        request_set.append(set([requests[num_idx], requests[num_idx+1]]))
    

    front = 0
    rear = len(request_set)-1
    
    pair_set = [request_set[front]]
    while front < rear:
        front += 1
        comming_pair = request_set[front]
        
        for pair_idx in range(len(pair_set)):
            if (pair_set[pair_idx] - comming_pair) != pair_set[pair_idx]:
                pair_set[pair_idx] = pair_set[pair_idx] | comming_pair
                break
        else:
            pair_set.append(comming_pair)

    print(pair_set)
    # 조를 구성한 인원 수
    people = 0
    for pair in pair_set:
        people += len(pair)
    

    # 전체 인원 수 - 조를 구성한 인원 수 = 혼자인 애
    result = len(pair_set) + (N - people)
    print('#{} {}'.format(tc, result))

