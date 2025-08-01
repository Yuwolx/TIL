import sys
sys.stdin = open('sample_input.txt')

T = int(input())
answer = 0

for test_case in range(T):
    K, N, M = map(int, input().split())
    stop_list = list(map(int, input().split()))
    location = 0
    count = 0

while location < N:
    possible = 0
    max_location = 0
    if location + K >= N:
        answer = count
        break

    for i in range(location+1 , location + K+1):
        if i in stop_list:
            max_location = max(max_location,i) 
            possible += 1
    if possible == 0:
        answer = 0
        break


    
    location = max_location
    count += 1

print(answer)