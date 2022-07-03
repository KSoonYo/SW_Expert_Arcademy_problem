# front 와 rear를 이용해서 풀어보자.

tests = int(input())

for tc in range(1, tests+1):
    N, M = map(int, input().split())
    # M번 만큼 앞에 있는 숫자를 뒤로 옮기는 작업을 해야 함.
    # 원형 큐 활용해보기
    num_list = list(map(int, input().split()))

    front = -1
    rear = N - 1

    count = 0
    while count < M:
        # dequeue
        # front = (front + 1) % N
        front += 1
        front %= N
        elem = num_list[front]

        # dequeue 한 요소를 뒤에 추가
        # rear = (rear + 1) % N
        rear += 1
        rear %= N
        num_list[rear] = elem

        count += 1

    # 회전이 모두 끝나고 맨 앞에 있는 값을 dequeue
    front += 1
    front %= N
    ans = num_list[front]
    print('#{} {}'.format(tc, ans))


