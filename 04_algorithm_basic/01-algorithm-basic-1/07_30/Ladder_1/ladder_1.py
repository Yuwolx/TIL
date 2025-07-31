import sys
# open input text file
sys.stdin = open('input.txt')

T = int(input())
ladder = [list(map(int, input().split())) for _ in range(100)]


destination = -1
for x in range(100):
    if ladder[x][99] == 2:
        destination = x
        break

print(destination)
print(ladder[:][99])