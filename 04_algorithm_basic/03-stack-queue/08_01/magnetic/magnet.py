import sys

sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(100)]

    # Make 100 list in list
    new_table = [[] for _ in range(100)]
    for col in range(100):
        for row in range(100):
            if table[row][col] == 0:
                continue
            else:
                new_table[col].append(table[row][col])

    # find 1,2
    cnt_complex = 0
    for row in range(100):
        for col in range(len(new_table[row])):
            if new_table[row][col] == 2 and col != 0:
                if new_table[row][col-1] == 1:
                    cnt_complex += 1

    print(f'#{tc} {cnt_complex}')

