def fibonacci(n, depth=0):
    indent = "  " * depth  # 호출 깊이만큼 들여쓰기
    print(f"{indent}fibonacci({n}) 호출")
    if n == 0:
        print(f"{indent}  반환: 0")
        return 0
    elif n == 1:
        print(f"{indent}  반환: 1")
        return 1
    else:
        a = fibonacci(n-1, depth+1)
        b = fibonacci(n-2, depth+1)
        print(f"{indent}  반환: {a} + {b} = {a+b}")
        return a + b

print("최종 결과:", fibonacci(4))
