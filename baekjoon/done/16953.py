a, b = map(int, input().split())

ev = 1
while b > a:
    if (b-1) % 10 == 0:
        ev += 1
        if round(b * 0.1) >= a:
            b = round(b * 0.1)
            continue

    if b % 2 == 0:
        ev += 1
        if b/2 >= a:
            b = b/2
            continue
    break
                


if a == b:
    print(ev)

else:
    print(-1)
