import sys
sys.stdin = open('sample_input.txt')

def test(film, D, W, K):
    #insfection each column
    for x in range(W):
        cnt, max_cnt = 1, 1
        for y in range(1,D):
            if film[y][x] == film[y-1][x]:
                cnt += 1
                # store max value
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 1
        # fail
        if max_cnt < K:
            return False
    # every column pass the test
    return True

def dfs(depth, cnt, film, D,W,K):
    global answer
    # if abuse drug
    if cnt >= answer:
        return
    
    # fill every
    if depth == D:
        if test(film, D, W, K):
            answer = min(answer, cnt)
        return
    
    # keep current row
    dfs(depth+1, cnt, film, D,W,K)

    backup = film[depth][:]
    # insert 0 drug
    film[depth] = [0]*W
    dfs(depth+1, cnt+1, film, D,W,K)
    film[depth] = backup[:]

    # insert 1 drug
    film[depth] = [1]*W
    dfs(depth+1, cnt+1, film, D,W,K)
    film[depth] = backup[:]



T = int(input())
for tc in range(1,T+1):
    # D is layer, W is bars in one layer, K is standard for pass 
    D, W, K = map(int, input().split())

    # the film size is D x W
    film = [list(map(int, input().split())) for _ in range(D)]

    # # print film
    # for x in film:
    #     print(x)

    # If change K times, then certainly pass
    answer = K
    dfs(0,0,film, D, W, K)
    print(f"#{tc} {answer}")