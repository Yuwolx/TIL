# 팩토리얼을 반복문으로 구현

N = 5
#최종 결과값
answer = 1 #초기값을 1로 초기화
#이제 1부터 N까지 answer에 곱할 수 있도록 순회

for num in range(1, N+1):
    answer *= num

print(answer)

'''
재귀함수는 기본적으로 2가지 영억으로 구분지을 수 있다
1.Bsis Rule 1이 되었을 때 1을 반환
2 Intuctive Rule: (n-1)로 자기 자신을 호출
'''

def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)        #표현식 -> 하나의 값으로 평가

    # n이 주어졌을 때 n~0 사이의 정수들을 모두 곱해야한다.
    # 곱 연산이므로 0이 되기 전에 종료해야한다
    # 1이 됐을 때는 1을 반환한다
    # f(5) = 5*4*3*2*1
    # f(1) = 1
    # f(n) = n * f(n-1)