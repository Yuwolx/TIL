import sys
sys.stdin = open("sample_input.txt")

from collections import deque

# up, down, left, right
direction_y = [-1, 1, 0, 0]
direction_x = [0, 0, -1, 1]

# 각 파이프 종류별 연결 가능한 방향
pipe_dirs = {
    1: [0, 1, 2, 3],
    2: [0, 1],
    3: [2, 3],
    4: [0, 3],
    5: [1, 3],
    6: [1, 2],
    7: [0, 2]
}

# 방향 반대 정의
opposite_dir = {0: 1, 1: 0, 2: 3, 3: 2}

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    pipes_map = [list(map(int, input().split())) for _ in range(N)]
    pipe_point = [[0] * M for _ in range(N)]

    def available_aisle(y, x, pipe_code):
        candidates = []
        for i in pipe_dirs.get(pipe_code, []):
            next_y = y + direction_y[i]
            next_x = x + direction_x[i]
            # 범위 밖
            if next_x < 0 or next_x >= M or next_y < 0 or next_y >= N:
                continue
            # 이미 방문
            if pipe_point[next_y][next_x] == 1:
                continue
            # 파이프 없음
            if pipes_map[next_y][next_x] == 0:
                continue
            # 연결 불가능한 파이프
            if opposite_dir[i] not in pipe_dirs.get(pipes_map[next_y][next_x], []):
                continue
            candidates.append((next_y, next_x))
        return candidates

    def find_possible_aisle(R, C, L):
        expand_candidate = deque()
        time = 0
        possibility = 1
        expand_candidate.append((R, C))
        pipe_point[R][C] = 1  # 시작 위치 방문 처리

        while time < L - 1 and expand_candidate:
            for _ in range(len(expand_candidate)):
                row, column = expand_candidate.popleft()
                candidates = available_aisle(row, column, pipes_map[row][column])
                for y, x in candidates:
                    if pipe_point[y][x] == 0:
                        pipe_point[y][x] = 1
                        possibility += 1
                        expand_candidate.append((y, x))
            time += 1

        return possibility



    result = find_possible_aisle(R, C, L)
    print(f'#{tc} {result}')
