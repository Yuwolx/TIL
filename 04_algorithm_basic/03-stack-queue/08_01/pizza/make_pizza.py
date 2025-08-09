import sys
sys.stdin = open("sample_input.txt")
from collections import deque

def insert_pizza(pizzas, piz_num, oven, record, made_pizza):
    # rotate oven
    while len(made_pizza) < N + M:
        #check oven status
        out_pizza = oven.popleft()
        out_pizza = out_pizza // 2
        # print(f'out pizza: {out_pizza}')
        out_index = record.popleft()
        if out_pizza == 0:
            # when there is more pizza list
            if len(pizzas) > 0:
                in_pizza = pizzas.popleft()
                in_num = piz_num.popleft()
                #insert pizza to oven
                oven.append(in_pizza)
                # print(f'in pizza {in_pizza}')
                #insert num to record
                record.append(in_num)

            # insert made pizza index
            made_pizza.append(out_index)
            # print(f'oven: {oven}')
            # print(f'record: {record}')
            # print(f'made_pizza: {made_pizza}')
        
        # baking pizza
        if out_pizza > 0:
            oven.append(out_pizza)
            record.append(out_index)
            # print(f'in pizza {out_pizza}')
            # print(f'oven: {oven}')
            # print(f'record: {record}')

    return made_pizza






T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    pizzas = deque(list(map(int, input().split())))
    piz_num = deque([i+1 for i in range(M)])

    #print(pizzas, piz_num)

    # make oven state
    oven = deque([0 for _ in range(N)])
    # record pizza number
    record = deque([0 for _ in range(N)])

    # list for store made pizza index
    made_pizza = []

    #Let's make pizza
    result = insert_pizza(pizzas, piz_num, oven, record, made_pizza)
    
    last_pizza = result.pop()

    print(f'#{tc} {last_pizza}')





