import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input()) 
    farm = [list(map(int, input())) for _ in range(N)]
    result = 0

    x = N//2
    for i in range(N):
        if i <= N // 2:
            result += sum(farm[i][x - i: x + i+1])
        else:
            result += sum(farm[i][i-x:3*x-i+1])

    print(f"#{tc} {result}")