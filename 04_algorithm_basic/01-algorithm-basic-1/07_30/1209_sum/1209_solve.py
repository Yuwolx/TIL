import sys
# open input text file
sys.stdin = open('input.txt')

# This problem have 10 test case
'''
for _ in range(1,11):
    tc = input()    # insert test case
    # 100 x 100 receive 2차원 list
    data = []
    for i in range(100):
        # 공백 기준으로 쪼개진 문자열을 정수로 바꿔야 한다.
        tmp_list = input().split() # make list splited by space
        map_data = map(int, tmp_list)
        map_to_list = list(map_data)
        data.append(map_to_list)
    print(data)
'''
for _ in range(10):
    tc = input()
    data = [list(map(int,input().split())) for _ in range(100)] # make 100x100 list

    sum_row_list = []
    for line in data: # loof low
        rst = 0
        for y in range(100):
            rst += line[y]   # sum in row
        sum_row_list.append(rst)

    sum_col_list = []
    for x in range(100):
        rst = 0
        for y in range(100):
            rst += data[x][y]     # sum in col
        sum_col_list.append(rst)

    rst_crs1 = 0
    for x in range(100):
        rst_crs1 += data[x][x]     # sum in cross

    rst_crs2 = 0
    for x in range(100):
        z = 99 - x
        rst_crs2 += data[x][z]     # sum in cross2


print(rst_crs1)


# Sum each row and column and cross
# print max_value
# 2 4 3 1 문제 풀이 순서