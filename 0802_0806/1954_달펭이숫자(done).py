
def snail_print(size, last_num):
    if size <= 0:
        return None

    if size == 1:
        return [[last_num + 1]]

    # size x size 행렬 
    snail_list = [[0 for _ in range(size)] for _ in range(size)]
    
    # 시작 출력 숫자
    start_print_num = last_num
    last_col = 0

    # 전략 
    # 1. 테두리부터 숫자들을 리스트에 입력하고 내부는 재귀로
    # for문으로 돌면서 위 행렬d의 각 숫자 위치에 따른 값을 지정
    for top_column in range(size):
        snail_list[0][top_column] = start_print_num + 1
        last_col = top_column
        start_print_num += 1


    for row in range(1, size):
        snail_list[row][last_col] = start_print_num + 1
        start_print_num += 1


    for bottom_column in range(last_col-1, -1, -1):
        snail_list[size-1][bottom_column] = start_print_num + 1
        last_col = bottom_column
        start_print_num += 1


    for reverse_row in range(size-2, 0, -1):
        snail_list[reverse_row][last_col] = start_print_num + 1
        start_print_num += 1


    # 2. 만약 snail_list[1][0]의 값이 0이 아니라면, 내부 재귀로 size를 -2해서 들어감
    next_size = size - 2
    if snail_list[1][0]:
        inner_list = snail_print(next_size, snail_list[1][0])

    # 3. 아직 비어있는 곳(값이 0인 곳)을 내부 재귀함수로부터 리턴받은 리스트를 통해 값 지정  
    # 반환값이 None이라면 더하지 않음.

    inner_row = 0
    inner_col = 0

    if inner_list:
        for elem_row in range(size):
            for elem_col in range(size):
                if not snail_list[elem_row][elem_col]:
                    if inner_col < next_size:
                        snail_list[elem_row][elem_col] = inner_list[inner_row][inner_col]
                        inner_col += 1
                    elif inner_row < next_size:
                        inner_row += 1
                        inner_col = 0
                        snail_list[elem_row][elem_col] = inner_list[inner_row][inner_col]
                        inner_col += 1           


    return snail_list

test_case = int(input())

size_list = []
for case in range(test_case):
    size = int(input())
    size_list.append(size)



for print_snail in range(1, test_case + 1):
    print(f'#{print_snail}')
    now_size = size_list[print_snail-1]
    snail_list = snail_print(now_size, 0)
    for row in range(now_size):
        for col in range(now_size):
            print(snail_list[row][col], end=' ')
        print("")

