c0 = int(input("Give a number"))
steps = 0

while c0 > 0 and c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 / 2

    else:
        c0 = 3 * c0 + 1
    steps += 1
    print(c0)
print("Number of steps:", steps)