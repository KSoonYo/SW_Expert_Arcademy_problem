

for tc in range(1, 11):
    input_tc = int(input())
    queue = list(map(int, input().split()))

    # 1 사이클 : [-1, -2, -3, -4, -5]
    cycle = list(range(-1, -6, -1))

    # 끝 자리가 0보다 작거나 같을 때까지 사이클 반복
    # 사이클을 도는 동안, 요소를 dequeue 하고 값을 뺀 다음 다시 enqueue

    # 선형 큐 활용
    idx = 0
    while True:
        if idx >= len(cycle):
            idx = idx % len(cycle)

        # 요소 dequeue
        elem = queue.pop(0)
        elem += cycle[idx]

        # 요소 enqueue
        queue.append(elem)

        if elem <= 0:
            queue[-1] = 0
            break

        idx += 1
    print('#{}'.format(tc), *queue)

#
# tc = 0
# while tc < 11:
#     input_tc = int(input())
#
#     queue = list(map(int, input().split()))
#
#     # 1 사이클 : [-1, -2, -3, -4, -5]
#     cycle = list(range(-1, -6, -1))
#
#     # 끝 자리가 0보다 작거나 같을 때까지 사이클 반복
#     # 사이클을 도는 동안, 요소를 dequeue 하고 값을 뺀 다음 다시 enqueue
#
#     # 선형 큐 활용
#     idx = 0
#     while True:
#         if idx >= len(cycle):
#             idx = idx % len(cycle)
#
#         # 요소 dequeue
#         elem = queue.pop(0)
#         elem += cycle[idx]
#
#         # 요소 enqueue
#         queue.append(elem)
#
#         if elem <= 0:
#             queue[-1] = 0
#             break
#
#         idx += 1
#
#     print('#{}'.format(tc), *queue)
#     tc += 1
