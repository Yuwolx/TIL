
T= int(input())

for _ in range(T):

    page = int(input())

    book = list(map(int, input().split()))
    print(book)

    maps = [['.'] * page for _ in range(page)]

    for x in range(page):
        maps[x][x] = 0

        if x < page -1:
            maps[x][x+1] = book[x] + book[x+1]

    for x in maps:
        print(x)

