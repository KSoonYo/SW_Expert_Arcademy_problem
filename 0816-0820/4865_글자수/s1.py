
tests = int(input())

result = [0]
for _ in range(tests):
    str1 = input()
    str2 = input()

    # 사전 생성
    str_dict = {}
    for char in str1:
        if char not in str_dict:
            str_dict[char] = 0

    # 문자 count
    # count() 활용도 가능
    for char in str2:
        if char in str_dict:
            str_dict[char] += 1

    # 가장 많은 문자 check
    maxV = 0
    for key in str_dict:
        if maxV < str_dict[key]:
            maxV = str_dict[key]
    result.append(maxV)


for print_case in range(1, tests+1):
    print('#{} {}'.format(print_case, result[print_case]))
