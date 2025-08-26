import sys
sys.stdin = open('sample_input.txt')


def selection(liszt):
    for i in range(0,N-1):
        standard = i
        for j in range(i+1,N):
            # if liszt's index is even find max
            if i % 2 == 0:
                if liszt[j] > liszt[standard]:
                    standard = j

            else:
                if liszt[j] < liszt[standard]:
                    standard = j
        liszt[i], liszt[standard] = liszt[standard],liszt[i]
        #print(liszt)
    return liszt


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    result = selection(numbers)

    print(f'#{tc}', end = ' ')
    for i in range(10):
        print(result[i], end=' ')
    print()