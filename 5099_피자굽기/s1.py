import sys

sys.stdin = open('sample_input.txt')

tests = int(input())


for tc in range(1, tests+1):
    # 화덕 크기 : N, 피자 개수 : M
    # 치즈 양: C
    N, M = map(int, input().split())
    c = list(map(int, input().split())) # 피자 리스트


    # 치즈가 다 녹은 피자의 번호를 순서대로 저장할 stack
    finished_pizza = []

    #### 피자를 화덕에 넣는 과정
    # 피자들의 리스트는 선형 큐
    # 화덕의 크기 N 만큼의 큐 공간 생성(원형 큐)
    # 우선 피자들 목록을 앞에서부터 dequeue
    # 꺼낸 피자를 화덕에 enqueue  [0]은 피자의 번호, [1]은 치즈 양

    # 만약 화덕의 rear의 +1 값이 N 이라면 화덕은 꽉 찬 상태

    pizza_front = -1

    oven_queue = [0] * N
    oven_front = oven_rear = -1

    while oven_rear+1 < N:
        # 피자 dequeue
        # 피자는 항상 화덕의 크기보다 많거나 같음
        pizza_front += 1
        pizza = c[pizza_front]

        # 꺼낸 피자를 오븐에 enqueue
        # +) 번호와 치즈양을 함께 oven_queue 에 저장
        oven_rear += 1
        oven_rear %= N
        oven_queue[oven_rear] = [pizza_front, pizza]

    #### 화덕 회전
    # 피자를 화덕에 넣은 순간부터 rotation 시작
    # 아까 피자를 넣은 과정을 지났기 때문에 rear가 oven_queue 끝에 있는 피자를 가리키고 있는 상태
    # => 넣으면서부터 회전이 이미 이루어짐.
    # 이후 dequeue 할 때마다 피자의 치즈양을 // 2 씩 해주면 치즈가 녹은 피자를 곧바로 확인 가능

    # 화덕에서 피자를 꺼냄: dequeue
    # 치즈의 양이 반 줄어든 것 확인
    # 꺼낸 피자를 다시 화덕에 enqueue

    # finished_pizza 의 길이가 c와 똑같을 때까지 반복
    while len(finished_pizza) < len(c):
        # print('oven_status: ', oven_queue)

        # dequeue from oven
        oven_front += 1
        oven_front %= N
        one_pizza = oven_queue[oven_front]
        # print('before one_pizza', one_pizza)
        baked_pizza = one_pizza[1] // 2
        one_pizza[1] = baked_pizza
        # print('after one_pizza', one_pizza)

        # 오븐에서 dequeue를 하고 확인해보니 치즈의 양이 0이라면
        if baked_pizza == 0:

            # => 아까 피자 목록에서 남은 피자 dequeue
            # pizza_front 에서 +1 한 값이 M 이라면, 남은 피자는 이제 없으므로
            # 피자 리스트에서 dequeue 및 화덕에 enqueue 를 수행하지 않음
            if pizza_front + 1 != M:
                pizza_front += 1
                pizza = c[pizza_front]
                # 피자를 화덕에 enqueue
                # +) 번호도 함께
                oven_rear += 1
                oven_rear %= N
                oven_queue[oven_rear] = [pizza_front, pizza]


            else:   # 더 들어올 피자가 없다면
                # enqueue 하는 대신 해당 피자가 있던 위치의 치즈양이 0으로 변함
                oven_rear += 1
                oven_rear %= N
                oven_queue[oven_rear] = one_pizza

            # 해당 피자의 번호를 피자 스택에 저장
            # 이 때, 해당 피자의 번호는 one_pizza[0]
            # 이미 피자 번호가 스택에 들어있는 경우를 고려
            if one_pizza[0] not in finished_pizza:
                finished_pizza.append(one_pizza[0])
        else:
            # enaueue into oven
            oven_rear += 1
            oven_rear %= N
            oven_queue[oven_rear] = one_pizza

        ### 마지막 까지 남은 피자 번호 확인

    print('#{} {}'.format(tc, finished_pizza[-1] + 1))

### 팁: 피자의 번호와 치즈를 []로 묶어서 queue에 저장!

'''
solution)
화덕의 인덱스를 큐로 관리하여 푸는 방법

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    q = [i for i in range(N)]
    idx = N # 화덕에 들어갈 다음 인덱스값(치즈)
    while len(q) > 1: # 큐에 하나밖에 안남을때까지 반복
        now = q.pop(0) # 현재 화덕 번호
        cheese[now] //= 2
        if cheese[now] > 0:
            q.append(now)
        elif idx < M:
            q.append(idx) # 아직 치즈가 0이 아니면 다시 큐에 삽입(인덱스)
            idx += 1
    print('#{} {}'.format(t, q[0] + 1)) # 마지막 피자 번호 출력

'''