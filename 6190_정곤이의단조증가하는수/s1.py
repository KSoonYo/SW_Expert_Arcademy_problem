tests = int(input())


# 단조 증가 수인지 판별하는 함수
def is_danzo(num):
    
    # 몫: quotient / 나머지: r
    # 나머지 연산으로 단조 판별
    divisor = 10
    pre_r = num % 10 # 최초 나머지
    quotient = num // divisor # 최초 몫
    while quotient != 0:
        quotient, r = divmod(quotient, divisor)
        # 10으로 나머지 연산을 할 때, 이전 나머지가 항상 현재의 나머지보다 크거나 같아야 단조
        # 이전 나머지가 현재 나머지보다 작으면 False 
        if pre_r < r:
            return False
        pre_r = r # 나머지 갱신
    
    # 반복을 모두 무사히 돌았다면
    return True


for tc in range(1, tests+1):
    N = int(input())
    
    # 숫자 입력
    num_list = list(map(int, input().split()))

    # 숫자 내림차순 정렬
    num_list.sort(reverse=True)

    # danzo 초기화
    danzo_num = -1

    flag = 0
    # 두개씩 곱하면서 단조 증가 수 인지 판별
    for i in range(N-1):
        for j in range(i+1, N):
            result = num_list[i] * num_list[j]
            if result <= 10:
                continue

            elif is_danzo(result) and (result > danzo_num): # 단조이고 현재 단조값보다 크다면
                # 최대 단조값 업데이트
                danzo_num = result
                

    print('#{} {}'.format(tc, danzo_num))

            