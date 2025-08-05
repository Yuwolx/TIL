import sys
# open input text file
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(10, T+1):
    ladder = []
    for _ in range(100):
        row = list(map(int, input().split()))
        ladder.append(row)
        print(ladder)
