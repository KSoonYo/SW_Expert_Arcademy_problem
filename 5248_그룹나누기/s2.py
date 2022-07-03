
def find_set(x):
    if numbers[x] == x:
        return x
    else:
        return find_set(numbers[x]) # return 빼먹지 말기


def union(student1, student2):
    root1 = find_set(student1)
    root2 = find_set(student2)
    numbers[root2] = root1


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    # 신청서
    requests = list(map(int, input().split()))

    # 학생 출석 명단
    numbers = [0] + list(range(1,N+1)) 
    # numbers = [num for num in range(N+1)]

    # 조 생성하기
    for idx in range(M):
        student1 = requests[idx * 2]
        student2 = requests[idx * 2 + 1]
    
        union(student1, student2)

    # 조 count 하기
    cnt = [0] * (N+1)
    for student in range(1, N+1):
        group_rep = find_set(student) # 해당 student 가 속한 그룹의 조장
        cnt[group_rep] = 1            # 같은 그룹원들은 같은 조장을 공유
                                  
        
    result = sum(cnt)
    print('#{} {}'.format(tc, result)) 
