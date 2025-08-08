from collections import deque

# 입력 데이터 직접 삽입
T = 1
N, M, R, C, L = 5, 6, 2, 1, 3
pipes_map = [
    [0, 0, 5, 3, 6, 0],
    [0, 0, 2, 0, 2, 0],
    [3, 3, 1, 3, 7, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

pipe_point = [[0] * M for _ in range(N)]

# 상하좌우
direction_y = [-1, 1, 0, 0]
direction_x = [0, 0, -1, 1]

# 각 파이프가 이동 가능한 방향
pipe_dirs = {
    1: [0, 1, 2, 3],    # 상하좌우
    2: [0, 1],          # 상하
    3: [2, 3],          # 좌우
    4: [0, 3],          # 상우
    5: [1, 3],          # 하우
    6: [1, 2],          # 하좌
    7: [0, 2],          # 상좌
}

# 방향 반대쪽 매핑
opposite = {0:1, 1:0, 2:3, 3:2}

def find_possible_aisle(R, C, L):
    queue = deque()
    queue.append((R, C, 1))  # y, x, 현재 시간
    pipe_point[R][C] = 1
    count = 1

    while queue:
        y, x, time = queue.popleft()

        if time >= L:
            continue

        pipe_type = pipes_map[y][x]
        for d in pipe_dirs.get(pipe_type, []):
            ny = y + direction_y[d]
            nx = x + direction_x[d]

            # 범위 확인
            if not (0 <= ny < N and 0 <= nx < M):
                continue
            # 다음 위치에 파이프 없거나 이미 방문했는지
            if pipes_map[ny][nx] == 0 or pipe_point[ny][nx]:
                continue
            # 연결 가능한지 확인
            next_pipe = pipes_map[ny][nx]
            if opposite[d] not in pipe_dirs.get(next_pipe, []):
                continue

            pipe_point[ny][nx] = 1
            count += 1
            queue.append((ny, nx, time + 1))

    return count

# 실행
result = find_possible_aisle(R, C, L)
print(f'#1 {result}')
