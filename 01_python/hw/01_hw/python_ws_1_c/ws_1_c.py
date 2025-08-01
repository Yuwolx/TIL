# 아래에 코드를 작성하시오.

# 영화관 좌석 예매 시스템의 기본 기능을 구현하시오. 시스템은 3x3 크기의 좌석 배치를 가지며, 
# 사용자가 원하는 좌석을 선택하여 예매할 수 있어야 한다.

# 요구사항
# 3x3 크기의 2차원 리스트를 생성하여 초기 좌석 배치를 표현하시오. 좌석은 'O'로 표시합니다.
seats = [['O' for o in range(3)] for o in range(3)]
print(seats)

# (0,2), (1,0), (1,2), (2,0), (2,2) 좌석을 예매 처리하시오. 예매된 좌석은 'X'로 표시합니다.
reserved = [(0,2), (1,0), (1,2), (2,0), (2,2)]
for row, col in reserved:
    seats[row][col] = 'x'


# 예매된 좌석을 포함하여 현재 좌석 배치를 출력하시오.
print(seats)