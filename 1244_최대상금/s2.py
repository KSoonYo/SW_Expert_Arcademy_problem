

def swap(listA, target_a, target_b):
    listA[target_a], listA[target_b] = listA[target_b], listA[target_a]

for tc in range(1, int(input())+1):
    number_cards, swap_chances = input().split()
    
    # 카드 리스트
    cards_list = list(map(int, number_cards))
    # 최대 교환 횟수
    max_swap = int(swap_chances)

    # 상금
    price = 0

    # 교환 작업
    swap_cnt = 0
    front_idx = 0
    candidates = []
    each_length = 0
    pop_cnt = 0
    while True:

        # 현재 카드 리스트를 순회하면서 가장 큰 숫자의 인덱스를 queue에 넣기.
        # 0번 인덱스의 최대 숫자는 queue에 넣을 필요 없음
        queue = []
        front = rear = -1

        print('card_list', cards_list)
        max_num = max(cards_list[front_idx:])
        for idx in range(front_idx, len(cards_list)):
            if idx == front_idx and cards_list[idx] == max_num:
                continue

            if cards_list[idx] == max_num:
                queue.append(idx)
                rear += 1
    
        if swap_cnt == (max_swap-1):
            price = max(price, int(''.join(map(str, cards_list))))
    
        print('queue', queue)
        while front < rear:
            # queue의 앞에서부터 인덱스를 꺼내어 맨 앞 인덱스의 값과 교환
            # 교환한 결과값을 candidates 후보군에 등록
            # 후보군에 등록한 뒤 다시 원위치
            
            temp_idx = 0
            front += 1
            
            temp_idx = queue[front]
          
            if cards_list[front_idx] == cards_list[temp_idx]:
                front_idx += 1 # 바꾸려는 자리에 이미 최대값이 있는 경우는 그 다음 자리를 노린다.
                front -= 1
                continue
                
        
            swap(cards_list, temp_idx, front_idx)
            candidates.append(cards_list[:])
            swap(cards_list, temp_idx, front_idx) # 원위치
        
        front_idx -= (swap_cnt+1)

        if not each_length:
            each_length = len(candidates)

        if pop_cnt == each_length:
            swap_cnt += 1
            print('swap_cnt', swap_cnt)
            each_length = len(candidates)
            pop_cnt = 0
        
        if swap_cnt == max_swap:
            break 


        print('candidates:', candidates)
        candidate = candidates.pop(0)
        front_idx += (swap_cnt+1)
        pop_cnt += 1
        cards_list = candidate
    
