def fibonacci_for_loop(n):
    #Basis rule is same
    # n이 1이면 1, 0이면 0
    if n ==0:
        return 0
    elif n == 1:
        return 1
    #n이 2 이상인 경우
    else: #이전 두 항의 값을 알아야 한다
        #n이 3이라면 first, second = 0,1
        # 2부터 n까지 모두 순회
        # 근데 예전 값들은 딱히 필요 없다
        for _ in range(2, n+1):
            next_fib = first + second
            # 다음으로 넘어가면 기존의 second가 first가 된다
            first, second = second, next_fib
            #다음 연산이 없다면 next_fib == second

        return second


# 사용 예시
print(fibonacci_for_loop(10)) # 55

