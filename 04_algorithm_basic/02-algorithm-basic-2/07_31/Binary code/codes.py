import sys
sys.stdin = open('input.txt')

pattern = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9
}

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    code = [list(map(int, input())) for _ in range(N)]

    for x in range(N):
        if len(set(code[x])) == 2: # if only 0 then 1
            y = 0 #idx to set finish
            tmp = []
            while y != M: # to end point of right
                # if 1 in first row or if 1 and above row's value is 0
                if (x == 0 and code[x][y] == 1) or (code[x][y] == 1 and code[x-1][y] == 0):
                    c = {0:0, 1:0, 2:0, 3:0}
                    for k in range(4):
                        while code[x][y] == (k % 2):
                            c[k] += 1
                            y += 1
                    tmp.append((pattern[(c[1],c[2],c[3])]))
                y += 1
            # translate
            result = 0
            for i in range(8): #len of code
                # even
                if i % 2:
                    result += tmp[i]
                else:
                    result += tmp[i] *3
            # result is not end 0
            if result % 10:
                print(f'#{tc} 0')
            else:
                print(f'#{tc} {sum(tmp)}')
            break


