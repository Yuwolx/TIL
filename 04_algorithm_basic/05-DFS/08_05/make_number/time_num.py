import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ops = list(map(int, input().split()))  # + - * //
    numbers = list(map(int, input().split()))

    max_result = []
    
    def dfs(depth, total, plus, minus, mul, div):
        if depth == N:
            max_result.append(total)
            return

        num = numbers[depth]

        if plus:
            dfs(depth + 1, total + num, plus - 1, minus, mul, div)
        if minus:
            dfs(depth + 1, total - num, plus, minus - 1, mul, div)
        if mul:
            dfs(depth + 1, total * num, plus, minus, mul - 1, div)
        if div:
            if total < 0:
                dfs(depth + 1, -(-total // num), plus, minus, mul, div - 1)
            else:
                dfs(depth + 1, total // num, plus, minus, mul, div - 1)

    dfs(1, numbers[0], ops[0], ops[1], ops[2], ops[3])
    print(f"#{tc} {max(max_result) - min(max_result)}")
