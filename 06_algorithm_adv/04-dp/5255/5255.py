import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    
    n = int(input())

    a, b, c = 1,3,6

    for _ in range(n-3):
        if n == 0 and n == 1 and n == 2 and n == 3:
            continue
        a, b, c = b, c, a +b*2+ c
        #print(a,b,c)

    print(f'#{tc} {c}')