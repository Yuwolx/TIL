import sys
# open input text file
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())

    total_list = []
    for x in range(10):
        blank_list = [ 0 for n in range(10)]
        total_list.append(blank_list)

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for x in range(r1,r2+1):
            for y in range(c1,c2+1):
                total_list[x][y] += color

    results = 0
    for x in range(10):
        for y in range(10):
            if total_list[x][y] == 3:
                results += 1

    print(f"#{tc} {results}")