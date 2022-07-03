# A 요리, B 요리 모두 N / 2 개 만큼의 식재료를 선택하여 시너지 합을 구함

# 시너지 합 |Sa-Sb|가 최소가 될 경우의 차를 출력 


## 하나의 요리에 들어가는 조합 구하기
## 식재료 N개 중에서  N / 2 개의 원소를 가진 집합 set 산출 (중복조합이 없어야 함 => set 자료형 사용)
## A요리를 하기위한 식재료가 선정되면, 나머지 반절은 자동으로 B 요리의 식재료로 선정

### 구한 집합 set으로 시너지 합들을 모두 구함(B요리도 같이)
### |Sa - Sb| 와 minV을 비교해서 최소값 갱신


'''
runtime error
dfs 완전탐색으로 조합을 구해서 그런가....? 

=> 
No, 고려할 필요가 없는 것까지 같이 고려해가면서 조합을 구했기 때문에 런타임이 뜬 것.
예를 들어 N이 6일 때
1 - 3 을 고르고 1 3 2 를 다시 선택하는 경우가 연산 과정에 포함이 되었기 때문
1 - 2 를 골랐을 때 나머지 3, 4, 5, 6 중에서 하나가 세번째 식재료로 선택되는데,
1 - 3 - 2 는 1 - 2 - 3 과 같은 조합이나 다름없다. 
따라서 1 - 3 을 고른 경우에는 4, 5, 6 중에 하나를 세번째 식재료로 선택하는 경우여야 한다.

'''
import sys

sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    # 식재료 수
    N = int(input())

    # 식재료 항목들
    ingredients = list(range(1, N+1))
  
    # 시너지 리스트
    S = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
    
    # 식재료 조합을 담을 집합
    for_cook = []


    # 재귀로 원소 개수가 N / 2 개인 부분집합 set을 구함(중복조합 방지)
    k = N // 2
    def rec(to_set, ingredients, k, temp=[]):

        if len(temp) == k and set(temp) not in to_set:
            to_set.append(set(temp))
            return

        # 현재 뽑을 수 있는 다음 식재료 후보
        candidates = []
        for next_ingredient in ingredients:
            if next_ingredient not in temp:
                candidates.append(next_ingredient)
    
        for next in candidates:
            rec(to_set, ingredients, k, temp + [next])
     
    
    rec(for_cook, ingredients, k)


    minV = 987654321 # 최소차 초기화
   

    # 시너지 합 구하기
    for cook_idx in range(len(for_cook)//2):
        Acook = list(for_cook[cook_idx])
        Bcook = list(for_cook[-(cook_idx+1)])

        Sa = Sb = 0
        for i in range(N//2):
            for j in range(i+1, N//2):
                Sa += S[Acook[i]][Acook[j]] + S[Acook[j]][Acook[i]]
                Sb += S[Bcook[i]][Bcook[j]] + S[Bcook[j]][Bcook[i]]
            
        minV = min(minV, abs(Sa-Sb))
           

    print('#{} {}'.format(tc, minV))




