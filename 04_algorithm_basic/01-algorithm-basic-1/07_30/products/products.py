import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,2):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]


center = N // 2

for i in len(farm):
    for j in len(farm):
        if i <= center:
            