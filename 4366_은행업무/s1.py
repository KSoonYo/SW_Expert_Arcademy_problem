def to_decimal(num):
    
    return_value = 0
    for n, value in enumerate(list(map(int, num))[::-1]):
        return_value += value * (3 ** n)

    return return_value




def in_triple(now_location, triple_num):

    if now_location == len(triple_num):
        return

    # 현재 위치가 틀렸다고 가정
    
    # 현재 위치에 올 수 있는 숫자들
    temp = []
    for num in triple_set:
        if num != triple_num[now_location]:
            temp.append(num)

    # triple_num 에서 현재 위치 숫자들만 바꾼 조합 생성
    for change in temp:
        temp_result = ''
        for idx in range(len(triple_num)):
            if idx == now_location:
                temp_result += change
                continue
            temp_result += triple_num[idx]
        second_candidates.append(temp_result)
    
    in_triple(now_location+1, triple_num)



  

for tc in range(1, int(input())+1):
    binary_num = input()
    triple_num = input()

    print_result = 0

    # 2진수의 현재 각 자리의 현재 수의 반대인 경우를 모두 탐색
    now_num = int('0b' + binary_num, 2)
    candidates = []
    for i in range(len(binary_num)):
        candidates.append(now_num ^ (1 << i))

    # 큰 수부터 확인해보자
    candidates.sort(reverse=True)

    triple_set = ('0','1','2')
    
    # 탐색한 수를 기반으로 3진수에서 각 자리의 현재 수의 반대인 경우 2가지를 모두 탐색
    # 탐색 수보다 커지면 곧바로 back
    
    second_candidates = []
    in_triple(0, triple_num)

    second_candidates = list(map(to_decimal, second_candidates))
    for target in candidates:
        if target in second_candidates:
            print('#{} {}'.format(tc, target))
            break



