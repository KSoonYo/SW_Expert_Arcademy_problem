
tests = int(input())

result = [0]
for _ in range(tests):
    str1 = input()
    str2 = input()

    # 고지식한 알고리즘으로 풀이
    i = 0
    j = 0
    while j < len(str1) and i < len(str2):
        if str1[j] != str2[i]:
            i = i - j
            j = -1
        i += 1
        j += 1

    if j == len(str1):
        result.append(1)
    else:
        result.append(0)

"""
다른 방식의 고지식한 알고리즘

sol1)

def check(str1, str2):
    # 고지식한 패턴 검색 방법 사용
    n = len(str2)
    m = len(str1)
    for i in range(n-m+1):
        if str2[i:i+m] == str1:
            return 1
    else:
        return 0

T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    print("#{} {}".format(test_case, check(str1, str2)))
    
#####

in 연산자를 이용한 풀이

T = int(input())

for test_case in range(1, T + 1):
    target_str = input()
    obj_str = input()

    exist = target_str in obj_str
    result = 1 if exist else 0

    print('#{} {}'.format(test_case, result))
"""


for print_case in range(1, tests+1):
    print("#{} {}".format(print_case, result[print_case]))
