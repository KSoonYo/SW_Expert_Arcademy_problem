import sys

sys.stdin = open('input.txt')

tests = int(input())

# max, min 함수 쓰면 쉽게 풀림
# 정렬 후 0번째 요소와 마지막 요소를 구하는 방식으로 풀이
# 입력 데이터의 최대 범위를 알지 못하므로 버블 정렬 방식 채택
result = []
for _ in range(tests):
    num_count = int(input())
    num_list = list(map(int, input().split()))

    # 정렬
    for idx in range(len(num_list)-1, 0, -1):
        for idx2 in range(idx):
            if num_list[idx2] > num_list[idx2+1]:
                num_list[idx2], num_list[idx2+1] = num_list[idx2+1], num_list[idx2]

    # 최대와 최소의 차를 결과 리스트에 추가
    result.append(num_list[-1] - num_list[0])

for print_case in range(1, tests+1):
    print('#{} {}'.format(print_case, result[print_case-1]))
