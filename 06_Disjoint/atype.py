T = int(input())
for tc in range(1,T+1):
    #number of tree
    N = int(input())
    trees = list(map(int, input().split()))

    max_tree = max(trees)

    # make gap list between highest tree with another trees
    gap = []
    for i in trees:
        gap.append(max_tree - i)

    # min days for growth
    min_days = []
    for i in gap:
        min_days.append(i//3)

    # 3cm is 1 set, and 1set composed 2 days
    minest = sum(min_days) * 2

    # rest cm for target
    rest = []
    for i in gap:
        rest.append(i%3)


    # for count rest days
    one = 0
    two = 0
    for i in rest:
        if i == 1:
            one += 1
        elif i == 2:
            two += 1

    # if who need two centimeter plant is more than need one. they can poured split by 1 day twice
    while two - one >= 2:
        two -= 1
        one += 2

    while one - two >= 2:
        two += 1
        one -= 2




    #count full day
    if one > two:
        full_day = minest + (one*2-1)
    else:
        full_day = minest + two*2

    print(f'#{tc} {full_day}')