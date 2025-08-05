import sys
sys.stdin = open("sample_input.txt", "r")


from itertools import permutations
test_case = int(input())

for tc in range(1,test_case+1):

    N = int(input())

    operators = list(map(int, input().split()))
    # Change to operators                              # in evaluation every result use int, so change to '//'
    opers = ['+'] * operators[0] + ['-'] * operators[1] + ['*'] * operators[2] + ['//'] * operators[3]
    numbers = list(map(int, input().split()))
    numbers_re = numbers[::-1]

    #make every operators permutation cases
    unique_perms = set(permutations(opers))

    expression_list = []
    for s in unique_perms:
        s = list(s)
        tmp_expression = []
        numbers = numbers_re[:]
        for i in range(len(numbers)*2 -1):
            if i % 2 == 0:
                tmp_expression.append(numbers.pop())
            else:
                tmp_expression.append(s.pop())
        expression_list.append(tmp_expression)

    def calculate(x, op, y):
        if op == '+': return x + y
        if op == '-': return x - y
        if op == '*': return x * y
        if op == '//':
            if x < 0:
                return -(-x // y)  
            return x // y

    result = []
    for lst in expression_list:
        dex = -1
        value = lst[0]
        for q in lst:
            dex += 1
            if dex % 2 == 1: 
                x = value
                op = q
                y = lst[dex+1]
                value = calculate(x,op,y)

        result.append(value)
        nal = max(result) - min(result)
    print(f"#{tc} {nal}")

