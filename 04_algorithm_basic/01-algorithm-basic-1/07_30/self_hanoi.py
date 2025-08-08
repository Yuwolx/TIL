
def hanoi(n, main, sub, target):

    if n > 0:
        hanoi(n-1, main, target, sub) # f(1)은 작동 안함
        print(f'원반 {n}을 {main}에서 {target}으로 이동하였음.')
        hanoi(n-1,sub, main, target)




    return




number_of_disks = 4
hanoi(number_of_disks, 'A', 'B', 'C')