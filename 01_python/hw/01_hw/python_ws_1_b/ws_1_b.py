# 아래에 코드를 작성하시오.


# numbers 리스트에 1부터 10까지의 정수를 할당한다.
numbers = [1,2,3,4,5,6,7,8,9,10]

# numbers 리스트의 각 요소를 순회하며, 짝수일 경우 해당 숫자를 출력한다.
# for i in numbers:
#     if i % 2 == 0:
#         print(i)

# numbers 리스트의 각 요소를 순회하며, 홀수일 경우 해당 숫자를 '홀수'로 출력한다.
for i in numbers:
    if i == 5:
        break

    if i % 2 == 0:
        print(i)
    else:
        print(f'{i} is odd')

# numbers 리스트의 각 요소를 순회하며, 숫자가 5일 경우 반복을 종료한다.
