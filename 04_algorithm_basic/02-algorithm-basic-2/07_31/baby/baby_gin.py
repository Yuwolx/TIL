import sys
sys.stdin = open("input.txt")

def baby_gin(counts, group_count = 0):

    if group_count == 2: # if group consist with run and triple
        return True

    for i in range(10): #find triple
        if counts[i] >= 3:
            counts[i] -= 3
            # if current group count already 1, add and return true
            if baby_gin(counts, group_count + 1):
                return True
            counts[i] += 3 #back tracking
            # It's mean there is no another run or triple

    for i in range(8): #find 0~7
        if counts[i] > 0 and counts[i+1] > 0 and counts[i+2] > 0:
            # if still run after minus 1, that's mean 222 -> two triple
            counts[i] -= 1
            counts[i+1] -= 1
            counts[i+2] -= 1
            if baby_gin(counts, group_count + 1):
                return True
            counts[i] += 1
            counts[i + 1] += 1
            counts[i + 2] += 1

    return False





T = int(input())
for tc in range(1,T+1):
    cards = list(map(int, input().strip())) # info of cards
    counts = [0] * 10 # count cards each number

    for c in cards:
        counts[c] += 1

    result = baby_gin(counts)
    if result:
        rx = 'true'
    else:
        rx = 'false'
    print(f'#{tc} {rx}')