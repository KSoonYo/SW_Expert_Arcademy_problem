import sys

sys.stdin = open('sample_input.txt')

tests = int(input())


def Book(P, target_page):
    cnt = 0
    book = list(range(1, P+1))
    start = 0
    end = len(book) - 1
    while start <= end:
        cnt += 1
        middle = (start + end) // 2
        if target_page == book[middle]:
            return cnt
        else:
            if target_page < book[middle]:
                end = middle 
            
            else:
                start = middle    


result = [0]
for _ in range(tests):
    P, Pa, Pb = map(int,input().split())
    
    a_cnt = Book(P, Pa)
    b_cnt = Book(P, Pb)

    # 더 적은 횟수가 우승자!
    if a_cnt > b_cnt:
        result.append('B')
    elif a_cnt < b_cnt:
        result.append('A')
    else:
        result.append('0')
    

for print_case in range(1, tests+1):
    print('#{} {}'.format(print_case, result[print_case]))