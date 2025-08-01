import sys
sys.stdin = open("sample_input.txt", "r")

from collections import deque

T = int(input())  # 테스트 케이스 개수

for test_case in range(1, T + 1):
    # N: 접수 창구 개수, M: 정비 창구 개수, K: 사람 수, A: 목표 고객 접수창구 번호, B: 목표고객 정비창구 번호
    N, M, K, A, B = map(int, input().split())

    # 접수창구 시간
    a_times = list(map(int, input().split()))

    # 정비창구 시간
    b_times = list(map(int, input().split()))

    # 고객 도착 시간
    t_arrivals = list(map(int, input().split()))

customer_list = []
for i in range(1,K + 1):
    customer_list.append(str(i))

customer_list = deque(customer_list)

local_time = 0
arrival_customer = []
arrival_customer = deque(arrival_customer)
reception = []
reception = deque(reception)
repair = []
repair = deque(repair)

while True:
    customer_idx = -1
    for _ in t_arrivals:
        customer_idx += 1
        if local_time == t_arrivals:
            x = customer_list.popleft(customer_idx)
            arrival_customer.append(x)

    while len(reception) < N:
        reception.append(arrival_customer.popleft())
