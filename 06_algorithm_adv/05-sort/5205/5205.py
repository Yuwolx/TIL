import sys
sys.stdin = open('sample_input.txt')

T = int(input())

# quick sort
def quick(lists):
    # when there is only one in lists attach first or last
    if len(lists) <= 1:
        return lists
    
    pivot = lists[0]
    # Separate each number left or right by pivot's value
    left = [x for x in lists[1:] if x <= pivot]
    right = [x for x in lists[1:] if x > pivot]
    return quick(left) + [pivot] + quick(right)
    


for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    result = quick(numbers)
    k = result[N//2]

    print(f'#{tc} {k}')

    