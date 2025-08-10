import sys
sys.stdin = open('input.txt')

def find_highest_comb(depth):
    current_state = ''.join(numbers)

    # cut visited
    if current_state in visited[depth]:
        return
    # make current state to visited state
    visited[depth].add(current_state)

    # if use every swap chance
    if depth == swap:
        if current_state > highest[0]:
            highest[0] = current_state
        return
    
    # there is more swap chance
    for i in range(num_len-1):
        for j in range(i+1, num_len):
            numbers[i], numbers[j] = numbers[j], numbers[i]

            find_highest_comb(depth + 1)

            #back tracking
            numbers[i], numbers[j] = numbers[j], numbers[i]

T= int(input())
for tc in range(1, T+1):
    numbers, swap = input().split()
    #numbers is number of prize list
    numbers = list(numbers)

    swap = int(swap)
    #length of prize
    num_len = len(numbers)

    # cut the branch visitied in this depth
    # swap + 1 mean initial value + every swaped comb
    visited = [set() for _ in range(swap+1)]

    # assigned highest value
    highest = ['0']

    find_highest_comb(0)

    print(f'#{tc} {highest[0]}')
