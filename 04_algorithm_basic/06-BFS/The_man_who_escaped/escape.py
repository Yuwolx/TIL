import sys
sys.stdin = open("sample_input.txt")

from collections import deque

#Catch the man who escaped

'''
idea
The man can move 1 pipe per hour.
Each pipe has a designed direction it can move.
If we use BFS, we can check whether each pipe has been reached.
Mark when increase visited pipe's number, point add 1.
When time reaches the target time (L), count pipes that have point 1.
Return the counted value.
'''


'''
Functions I need:
1. A function that indicates 4 directions(not function, just need setting)
2. A function that finds possible directions in the current location
3. A function that indicates the current location and point (whether it is used as a destination or not)
'''

'''
variables
- N : row and y
- M : column and x
- T : test case
- R : row value where door is
- C : column value where door is
- L : target time

'''

# Test case number
T = int(input())

for tc in range(1, T+1):

    # N, M, R, C, L
    N, M, R, C, L = map(int, input().split())
    # Make a map the man hide
    pipes_map = [list(map(int, input().split())) for _ in range(N)]

    # each location's point
    pipe_point = [[0] * M for _ in range(N)]

    # up, down, left, right
    direction_x = [0,0,-1,1]
    direction_y = [-1,1,0,0]




    # make func find to available aisle the man can use
    def available_aisle(y,x,pipe_code):
        # candidates list for searching next step
        candidates = []
        candidates = deque()
        # print(f"[조사 시작] {y},{x} 조사시작, 코드 {pipe_code}")
        # if encounter cross pipe
        if pipe_code == 1:
            #append every side to candidates
            for i in range(4):
                next_x = direction_x[i] + x
                next_y = direction_y[i] + y
                # if next aisle locate outside of map
                if next_x < 0 or next_x >= M or next_y < 0 or next_y >= N:
                    continue
                # if already have visited
                if pipe_point[next_y][next_x] == 1:
                    continue
                # if there is no pipe
                if pipes_map[next_y][next_x] == 0:
                    continue

                # if pipes not connected with hole
                if i == 0:
                    if pipes_map[next_y][next_x] in [3,4,7]:
                        continue
                elif i == 1:
                    if pipes_map[next_y][next_x] in [3, 5, 6]:
                        continue
                elif i == 2:
                    if pipes_map[next_y][next_x] in [2, 6, 7]:
                        continue
                elif i == 3:
                    if pipes_map[next_y][next_x] not in [1,3,6,7]: #in [2, 4, 5]:
                        continue

                candidates.append((next_y,next_x))
                # print(f"[이동가능] 현재: ({y},{x}), 파이프: {pipe_code} → 이동: {next_y},{next_x}")

            return candidates

        # if encounter vertical shape pipe
        if pipe_code == 2:
            #append up and down side to candidates
            for i in [0,1]:
                next_x = direction_x[i] + x
                next_y = direction_y[i] + y
                # print(f"[CHECK] i={i}, 현재=({y},{x}), 다음=({next_y},{next_x}), pipe={pipes_map[next_y][next_x] if 0 <= next_y < N and 0 <= next_x < M else 'Out of range'}")

                # if next aisle locate outside of map
                if next_x < 0 or next_x >= M or next_y < 0 or next_y >= N:
                    # print("  ↳ 범위 밖")
                    continue
                # if already have visited
                if pipe_point[next_y][next_x] == 1:
                    # print("  ↳ 이미 방문")
                    continue
                # if there is no pipe
                if pipes_map[next_y][next_x] == 0:
                    # print("  ↳ 파이프 없음")
                    continue
                # if pipes not connected with hole
                if i == 0:
                    if pipes_map[next_y][next_x] in [3,4,7]:
                        # print("  ↳ 연결 안 됨 (위)")
                        continue
                elif i == 1:
                    if pipes_map[next_y][next_x] not in [1,2,4,7]: #in [3, 5, 6]:
                        # print("  ↳ 연결 안 됨 (아래)")
                        continue

                candidates.append((next_y, next_x))
                # print(f"[이동가능] 현재: ({y},{x}), 파이프: {pipe_code} → 이동: {next_y},{next_x}")

            return candidates

        # if encounter horizon shape pipe
        if pipe_code == 3:
            #append left and right side to candidates
            for i in range(2,4):
                next_x = direction_x[i] + x
                next_y = direction_y[i] + y
                # if next aisle locate outside of map
                if next_x < 0 or next_x >= M or next_y < 0 or next_y >= N:
                    continue
                # if already have visited
                if pipe_point[next_y][next_x] == 1:
                    continue
                # if there is no pipe
                if pipes_map[next_y][next_x] == 0:
                    continue
                # if pipes not connected with hole
                if i == 2:
                    if pipes_map[next_y][next_x] in [2, 6, 7]:
                        continue
                elif i == 3:
                    if pipes_map[next_y][next_x] in [2, 4, 5]:
                        continue

                candidates.append((next_y, next_x))
                # print(f"[이동가능] 현재: ({y},{x}), 파이프: {pipe_code} → 이동: {next_y},{next_x}")

            return candidates

        # if encounter L shape pipe
        if pipe_code == 4:
            #append up and right side to candidates
            for i in [0,3]:
                next_x = direction_x[i] + x
                next_y = direction_y[i] + y
                # if next aisle locate outside of map
                if next_x < 0 or next_x >= M or next_y < 0 or next_y >= N:
                    continue
                # if already have visited
                if pipe_point[next_y][next_x] == 1:
                    continue
                # if there is no pipe
                if pipes_map[next_y][next_x] == 0:
                    continue
                # if pipes not connected with hole
                if i == 0:
                    if pipes_map[next_y][next_x] in [3,4,7]:
                        continue

                elif i == 3:
                    if pipes_map[next_y][next_x] in [2, 4, 5]:
                        continue

                candidates.append((next_y, next_x))
                # print(f"[이동가능] 현재: ({y},{x}), 파이프: {pipe_code} → 이동: {next_y},{next_x}")

            return candidates

        # if encounter r shape pipe
        if pipe_code == 5:
            #append down and right side to candidates
            for i in [1,3]:
                next_x = direction_x[i] + x
                next_y = direction_y[i] + y
                # if next aisle locate outside of map
                if next_x < 0 or next_x >= M or next_y < 0 or next_y >= N:
                    continue
                # if already have visited
                if pipe_point[next_y][next_x] == 1:
                    continue
                # if there is no pipe
                if pipes_map[next_y][next_x] == 0:
                    continue
                # if pipes not connected with hole
                if i == 1:
                    if pipes_map[next_y][next_x] in [3, 5, 6]:
                        continue
                elif i == 3:
                    if pipes_map[next_y][next_x] in [2, 4, 5]:
                        continue

                candidates.append((next_y,next_x))
                # print(f"[이동가능] 현재: ({y},{x}), 파이프: {pipe_code} → 이동: {next_y},{next_x}")

            return candidates

        # if encounter ㄱ shape pipe
        if pipe_code == 6:
            #append down and left side to candidates
            for i in [1,2]:
                next_x = direction_x[i] + x
                next_y = direction_y[i] + y
                # if next aisle locate outside of map
                if next_x < 0 or next_x >= M or next_y < 0 or next_y >= N:
                    continue
                # if already have visited
                if pipe_point[next_y][next_x] == 1:
                    continue
                # if there is no pipe
                if pipes_map[next_y][next_x] == 0:
                    continue
                # if pipes not connected with hole
                if i == 1:
                    if pipes_map[next_y][next_x] in [3, 5, 6]:
                        continue
                elif i == 2:
                    if pipes_map[next_y][next_x] in [2, 6, 7]:
                        continue


                candidates.append((next_y,next_x))
                # print(f"[이동가능] 현재: ({y},{x}), 파이프: {pipe_code} → 이동: {next_y},{next_x}")

            return candidates

        # if encounter J shape pipe
        if pipe_code == 7:
            #append up and left side to candidates
            for i in [0,2]:
                next_x = direction_x[i] + x
                next_y = direction_y[i] + y
                # if next aisle locate outside of map
                if next_x < 0 or next_x >= M or next_y < 0 or next_y >= N:
                    continue
                # if already have visited
                if pipe_point[next_y][next_x] == 1:
                    continue
                # if there is no pipe
                if pipes_map[next_y][next_x] == 0:
                    continue
                # if pipes not connected with hole
                if i == 0:
                    if pipes_map[next_y][next_x] in [3,4,7]:
                        continue
                elif i == 2:
                    if pipes_map[next_y][next_x] in [2, 6, 7]:
                        continue

                candidates.append((next_y,next_x))
                # print(f"[이동가능] 현재: ({y},{x}), 파이프: {pipe_code} → 이동: {next_y},{next_x}")

            return candidates


    # print(f"[시작] tc#{tc}, 시작 위치: ({R},{C}), 파이프 타입: {pipes_map[R][C]}")


    # definition function that check current location and time
    def find_possible_aisle(R,C,L):
        # for solving scope of variable problem
        expand_candidate = deque()
        time = 0
        possibility = 1
        # append next step
        expand_candidate.append((R, C))
        # check location visited
        pipe_point[R][C] = 1
        # print('first value', possibility)

        #Finish if time reaches to target time or use every candidates
        while time < L-1 and expand_candidate:
            # print(f"\n[시간단계] time={time}, queue={list(expand_candidate)}")
            for _ in range(len(expand_candidate)):
                row, column = expand_candidate.popleft()
               #  print(f"[방문] {row},{column} 방문")

                # Take function about current location
                candidates = available_aisle(row, column, pipes_map[row][column])
                # Take up to outside variable
                for y, x in candidates:
                    if pipe_point[y][x] == 0:
                        pipe_point[y][x] = 1
                        expand_candidate.append((y,x))
                        # add possibility
                        possibility += 1
                        #print(possibility)
                        # print(f"[큐추가] {y},{x} 추가 (파이프 타입: {pipes_map[y][x]})")

            # after searching around 1 step
            time += 1



        return possibility



    result = find_possible_aisle(R,C,L)

    print(f'#{tc} {result}')








