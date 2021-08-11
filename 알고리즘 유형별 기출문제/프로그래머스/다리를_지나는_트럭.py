from collections import deque

# 2	10	[7,4,5,6]	8
# 100	100	[10]	101
# 100	100	[10,10,10,10,10,10,10,10,10,10]	110


# bridge_length = 2
# weight = 10
# truck_weights = [7, 4, 5, 6]


# bridge_length = 100
# weight = 100
# truck_weights = [10]

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]



timer = 0


def solution(bridge_length, weight, truck_weights):
    # 다리 길이만큼을 배열길이로 넣어줌
    answer = 0
    q = [0 for _ in range(bridge_length)]

    while q: # q가 빌때까지 시간을 더해주기
        # 시간(answer)이 1 증가할수록
        answer += 1
        # q배열이 왼쪽으로 이동
        q.pop(0)
        # 트럭이 더이상 없으면 끝
        if not truck_weights:
            continue
        if weight >= sum(q) + truck_weights[0]:
            q.append(truck_weights.pop(0))
        else:
            q.append(0)

    answer = 0
    return answer




print(solution(bridge_length, weight, truck_weights))

# print(on_bridge_truck)
# print(sum(on_bridge_truck))

# def solution(bridge_length, weight, truck_weights):
#     global timer
#     waiting_truck = deque(truck_weights)
#     on_bridge_truck = deque([0] * bridge_length)
#     finished_truck = []
#     while len(finished_truck) < len(truck_weights):
#         if on_bridge_truck[0] != 0:
#             temp = on_bridge_truck.popleft()
#             finished_truck.append(temp)
#             on_bridge_truck.appendleft(0)
#         if len(waiting_truck) != 0 and sum(on_bridge_truck) + waiting_truck[0] <= weight:
#             #다리 위에 트럭이 올라갈때 이미 다리 끝에 트럭이 있다면 한 칸씩 이동.
#             if sum(on_bridge_truck) != 0:
#                 on_bridge_truck.popleft()
#                 on_bridge_truck.append(0)
#             truck = waiting_truck.popleft()
#             on_bridge_truck[-1] = truck
#             print("다리에 싣음" + str(timer))
#         else:
#             #다리 중량이 꽉 차서 트럭을 옮길 수 없다면 다리위에 있는 트럭들을 한 칸씩 이동.
#             if sum(on_bridge_truck) != 0:
#                 on_bridge_truck.popleft()
#                 on_bridge_truck.append(0)
#             print("다리위에서 한 칸 이동" + str(timer))
#         timer += 1
#     return timer
