# A 요리, B 요리 모두 N / 2 개 만큼의 식재료를 선택하여 시너지 합을 구함

# 시너지 합 |Sa-Sb|가 최소가 될 경우의 차를 출력 


## 하나의 요리에 들어가는 조합 구하기
## 식재료 N개 중에서  N / 2 개의 원소를 가진 집합 set 산출 (중복조합이 없어야 함 => set 자료형 사용)
## A요리를 하기위한 식재료가 선정되면, 나머지 반절은 자동으로 B 요리의 식재료로 선정

### 구한 집합 set으로 시너지 합들을 모두 구함(B요리도 같이)
### |Sa - Sb| 와 minV을 비교해서 최소값 갱신


'''
완탐으로 조합 생성하여 푸는 문제인 줄 알았으나...생각해보니 순열로 푸는게 훨씬 나을 듯
어차피 1 2 3 이나 2 1 3 이나 같은 식재료 선택이다.
6개 식재료가 있다면 6개 식재료중 3개로 뭘 고를 지 고르는 것이므로 순열 문제.
1개를 고르고 나면 나머지 5개 중 하나를 골라야 한다. 
==> 멍청아, 그게 조합이잖아.

이전 풀이에서 런타임이 뜨는 이유는 N이 6일 때
1 - 3 을 고르고 1 3 2 를 다시 선택하는 경우가 연산 과정에 포함이 되었기 때문
1 - 2 를 골랐을 때 나머지 3, 4, 5, 6 중에서 하나가 세번째 식재료로 선택되는데,
1 - 3 - 2 는 1 - 2 - 3 과 같은 조합이나 다름없다. 
따라서 1 - 3 을 고른 경우에는 4, 5, 6 중에 하나를 세번째 식재료로 선택하는 경우여야 한다.


1 2 3 4 5 6 => 6개 중 3개의 요소를 가지는 조합 만들기
A: 1 - 2 - 3 / B: 4 - 5 - 6  => A 조합을 뺀 나머지가 곧 B 조합
...
1 - 2 - 6
2 - 3 - 4 
...
2 - 3 - 6


==> runtime 에러가 뜬다.
왜지???
=> 해결

'''
import sys

sys.stdin = open('input.txt')

def dfs(start, cnt):
    global minV
    
    if cnt == 0:
        # A 조합 완성
        # combinations에 없는 요소가 곧 B의 요소
        
        # 대칭쌍으로 더하기(N//2 가 3 이상 경우_리스트 하나 요소 갯수가 3개 이상인 경우도 고려)
        Sa = Sb = 0
        for i in range(N):
            for j in range(i+1, N):
                if i in combinations and j in combinations:
                    # A 리스트
                    Sa += (S[i][j] + S[j][i])
                elif i not in combinations and j not in combinations:
                    # B 리스트
                    Sb += (S[i][j]+ S[j][i])
        
        if minV > abs(Sa-Sb):
            minV = abs(Sa-Sb)
        return

    for idx in range(start, N):
        if idx not in combinations:
            combinations.append(idx)
            # dfs(start+1, cnt-1)
            dfs(idx+1, cnt-1)
            combinations.pop()



for tc in range(1, int(input())+1):
    # 식재료 수
    N = int(input())

    # 시너지 리스트
    S = [list(map(int, input().split())) for _ in range(N)]

    # N // 2 개 원소를 지닌 조합 만들기
    combinations = []

    minV = 987654321

    dfs(0, N // 2)
    print('#{} {}'.format(tc, minV))


'''

set의 차집합 연산으로 나머지 조합 걸러내기
all_list = [1,2,3,4,5,6]
A = [1,2,3] 
B = list(set(all_list) - set(A)) # [4,5,6] // 단 순서는 보장할 수 없음


'''










