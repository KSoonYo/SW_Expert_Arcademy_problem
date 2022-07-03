
hex_num = {
    'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13,
    'E' : 14, 'F' : 15
}


def to_decimal(nums):                          # 16진수 -> 10진수 
    length = len(nums)
    front = length - 1                         # 맨 앞 숫자의 차항
    result = 0
    for num in nums:
        if num.isdigit():
            result += int(num) * (16 ** front)
        else:
            result += hex_num[num] * (16 ** front)
        front -= 1

    return result



for tc in range(1, int(input())+1):
    N, K = map(int, input().split())            # N: 16진수 숫자의 개수, K: k번째로 큰 수
    
    numbers = list(input())                     # 16진수 숫자 list(문자열)
    # print(numbers)

    max_rotate = (N // 4)  - 1                  # 가능한 모든 경우의 수가 나올 수 있는 최대 회전 수(모든 변의 숫자 개수는 동일)
    number_length = N // 4                      # 16 진수 숫자 길이

    rotate = 0                                  # 현재 회전 수
    numbers_set = set()                         # 숫자 조합 set
    while rotate <= max_rotate:
        temp = ''
        if rotate > 0:                          # rotation
            numbers = [numbers.pop()] + numbers 
            # print('numbers', numbers)
        
        for num in numbers:                     # split
            temp += num
            if len(temp) == number_length:
                numbers_set.add(temp)
                temp = ''
        rotate += 1

    # print(list(numbers_set))

    decimal_numbers = list(map(to_decimal, list(numbers_set)))
    decimal_numbers.sort(reverse=True)
    # print(decimal_numbers[K-1])

    print('#{} {}'.format(tc, decimal_numbers[K-1]))

