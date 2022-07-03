import sys

sys.stdin = open('sample_input.txt')


'''
풀이 답
'''
def ratio(c_1, c_2, c_3):
    min_val = min(c_1, c_2, c_3)
    return str(c_1//min_val) + str(c_2//min_val) + str(c_3//min_val)


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    p_arr = [input() for _ in range(N)]
    answer = 0

    htob = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }
    p_dict = {
        '211': '0',
        '221': '1',
        '122': '2',
        '411': '3',
        '132': '4',
        '231': '5',
        '114': '6',
        '312': '7',
        '213': '8',
        '112': '9'
    }

    p_bin = ['']*N
    for i in range(N):
        for j in range(M):
            p_bin[i] += htob[p_arr[i][j]]

    sol = []
    p_list = ''
    for p in p_bin:
        count_1, count_2, count_3 = 0, 0, 0
        for i in range(M*4-1, -1, -1): # 행의 모든 요소를 2진수 4자리로 변환하기 때문에 전체 길이가 4배가 된다.
            if not count_1 and not count_2 and p[i] == '1':
                count_3 += 1
            elif not count_1 and count_3 and p[i] == '0':
                count_2 += 1
            elif count_2 and count_3 and p[i] == '1':
                count_1 += 1
            if count_1 and count_2 and count_3 and p[i] == '0':
                p_list += p_dict[ratio(count_1, count_2, count_3)]
                count_1, count_2, count_3 = 0, 0, 0
                if len(p_list) == 8:
                    p_list = p_list[::-1]
                    n_odd = int(p_list[0]) + int(p_list[2]) + int(p_list[4]) + int(p_list[6])
                    n_even = int(p_list[1]) + int(p_list[3]) + int(p_list[5]) + int(p_list[7])
                    if (3 * n_odd + n_even) % 10 == 0 and p_list not in sol:
                        answer += n_odd + n_even
                    sol.append(p_list)
                    p_list = ''
    print("#{} {}".format(tc, answer))
