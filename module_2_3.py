my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while len(my_list) > i:
    a = my_list[i]
    i = i + 1
    if a == 0:
        continue
    elif a > 0:
        print(a)
    else:
        break

