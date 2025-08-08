

















# for tc in range(1, 11):
#     n = int(input())  # 보통 100이 들어옴 (문제에서)
#     data = [list(map(int, input().split())) for _ in range(n)]
#
#     result = 0
#     for x in range(100):  # 열 기준 순회
#         stack = 0
#         for y in range(100):  # 행 순회 (위→아래)
#             if data[y][x] == 1:
#                 stack = 1  # N극 만남
#             elif data[y][x] == 2 and stack:
#                 stack = 0  # S극 만나고, 그 전에 N극이 있었으면
#                 result += 1
#     print(result)