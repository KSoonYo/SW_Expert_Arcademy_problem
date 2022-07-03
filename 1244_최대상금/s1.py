import sys

sys.stdin = open('input.txt')

for tc in range(1,int(input())+1):
    data, swap_max = input().split() # 숫자판의 정보, 교환횟수
    swap_max = int(swap_max)
    N = len(data) # 숫자판 길이

    print('data', data)
    now = set([data]) # data는 문자열이기 때문에 []로 감싸서 set() 해줘야 함.
    nxt = set() # set 생성
    for _ in range(swap_max):
        # 교환 횟수만큼 반복
        print(f'{_ + 1}번째')
        print('now', now) 
        print('nex', nxt)
        while now:
            s = now.pop()
            s = list(s)
            print('s: ',s)
            for i in range(N):
                for j in range(i+1,N):
                    print(f's[{i}], s[{j}] 교환')
                    s[i],s[j] = s[j],s[i] # 교환
                    nxt.add(''.join(s))
                    print('nxt: ', nxt)
                    s[i], s[j] = s[j], s[i] # 원위치
        print(f'{now} <-> {nxt}')
        now,nxt = nxt,now 

    print('#{} {}'.format(tc,max(map(int,now))))
    print('######################')


'''
solution
dfs 와 딕셔너리로 방문처리를 해주는 방법

```python
# sol 1)
"""
초기 visited를 딕셔너리로 선언
dfs 안에 같은 visited로 봤던 수인지 확인 후 아니면 진행

"""
import sys
sys.stdin = open('input.txt')

T = int(input())

def dfs(c_count):
    """
    :param c_count: 남은 교환 횟수
    temp_val : 현재 상금
    temp_key : visited 여부 확인을 위한 교환 후의 상금

    visited 변수를 남은 교환횟수를 포함한 딕셔너리 형태로 선언하여
    재귀의 가지치기 진행
    """
    global max_val

    # 교환횟수 0일 시 max 값과 비교하여 저장 혹은 종료
    if not c_count:
        temp_val = int(''.join(number_list))
        if temp_val > max_val:
            max_val = temp_val
        return

    for i in range(length):
        for j in range(i+1, length):
            number_list[i], number_list[j] = number_list[j], number_list[i]
            temp_key = ''.join(number_list)
            # visited 변수 내에 같은 tuple(현재 상금, 남은 교환횟수) 형태가 없을 시 재귀 진행
            if not visited.get((temp_key, c_count-1)):
                visited[(temp_key, c_count-1)] = True
                dfs(c_count-1)
            number_list[i], number_list[j] = number_list[j], number_list[i]

for tc in range(1, T+1):
    # 초기 입력 값 선언 및 최대 상금 -1로 초기화
    N, C = input().split()
    number_list = list(N)
    C = int(C)
    max_val = -1
    length = len(number_list)
    # visited 변수를 dictionary로 선언 및 dfs 함수 호출
    visited = {}
    dfs(C)
    print('#{0} {1}'.format(tc, max_val))
```

'''


'''
다른 풀이 2
dfs와 set으로 방문처리

def dfs(arr, cnt):
    global max_reward
    reward = int(''.join(arr))  # int로 변환
    if (reward, cnt) in records:
        return
 
    records.add((reward, cnt))
 
    if cnt == M:    # 주어진 횟수만큼 자리 변경을 완료했다면
        # 최대값 비교 & 갱신
        if reward > max_reward:
            max_reward = reward
        return
 
    # 변경횟수가 남은 경우 - 자리 선택
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            # 자리 바꿈
            arr[i], arr[j] = arr[j], arr[i]
            # 자리를 바꾼 후 한층 더 탐색
            dfs(arr, cnt+1)
            # 원상복구
            arr[i], arr[j] = arr[j], arr[i]
 
T = int(input())
for tc in range(1, T+1):
    numbers, M = map(int, input().split())  # 숫자판, 교환횟수
    numbers = list(str(numbers))   # 배열로 변환
    max_reward = 0
    records = set()     # 이미 탐색한 reward 를 저장해둔다.
 
    dfs(numbers, 0)
    print('#{} {}'.format(tc, max_reward))




'''
