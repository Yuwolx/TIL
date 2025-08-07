import sys
sys.stdin = open("sam.txt")

from collections import deque

def if_in(i):
    global area_num
    print(f"[입차시도] 차량 {i}번")  # 인덱스 그대로

    found_space = False
    for s in parking_lot:
        area_num += 1
        if s == {101:101}:
            if len(waited) == 0:
                parking_lot[area_num] = {i:area_num}
                print(f"  └▶ 주차공간 {area_num}번에 차량 {i}번 입차")
                i = 101
                found_space = True
                break
            else:
                print(f"  └▶ 대기열 존재: 차량 {i}번 대기행 추가")
                waited.append(i)
                found_space = True
                break
    if not found_space:
        print(f"  └▶ 빈 공간 없음: 차량 {i}번 대기열 추가")
        waited.append(i)

    print(f"    [주차장 상태] {parking_lot}")
    print(f"    [대기열 상태] {list(waited)}")

def if_wait():
    global area_num
    area_num = -1
    for s in parking_lot:
        area_num += 1
        if s == {101:101}:
            break
    priorty = waited.popleft()
    parking_lot[area_num] = {priorty:area_num}
    print(f"[대기입차] 대기 중 차량 {priorty}번 → 주차공간 {area_num}번 입차")
    print(f"    [주차장 상태] {parking_lot}")
    print(f"    [대기열 상태] {list(waited)}")

def if_out(i):
    global total_fare
    global area_idx
    print(f"[출차시도] 차량 {i}번")
    for dict in parking_lot:
        if i in dict:
            area_idx = dict[i]
            break
    parking_lot[area_idx] = {101:101}
    fee = per_fare[area_idx]
    wei = weight[i]
    f = fee * wei
    total_fare += f
    print(f"  └▶ 차량 {i}번 출차, 자리 {area_idx}번 비움")
    print(f"  └▶ 요금계산: {fee} * {wei} = {f}, 누적 {total_fare}")
    if len(waited) > 0:
        if_wait()

T = int(input())
for tc in range(1,T+1):
    # n is number of parking lots, m is number of car use parking area today
    n, m = map(int, input().split())

    # each parking area has separate rate per weight of car
    per_fare = []

    #make result
    total_fare = 0


    # make rate per weight to list, each index mean number of parking space
    for _ in range(n):
        rate = int(input())
        per_fare.append(rate)

    # each car has different weight
    weight = []
    for _ in range(m):
        kg = int(input())
        weight.append(kg)

    # owner know how many car will come parking lots
    # make log cars in and out record
    # car number is index in weight
    # -number mean out, + mean in
    inout_log = deque()
    for _ in range(2*m):
        log = int(input())
        inout_log.append(log)

    # make parking area list, 0 = empty, 1 = filled
    parking_lot = []
    for _ in range(n):
        parking_lot.append({101:101})
    # Waiting line
    waited = deque()

    while inout_log:
        i = inout_log.popleft()
        if i > 0:
            i = i - 1
            area_num = -1
            print("\n===== 입차 이벤트 =====")
            if_in(i)
        else:
            i = -i - 1
            area_num = -1
            print("\n===== 출차 이벤트 =====")
            if_out(i)
