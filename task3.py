def password():
    number_list = [i for i in range(372 ** 2, 809 ** 2+1)]

    check = []
    n = 0
    rep_num1 = []
    final = []

    for j in number_list:
        check.append(list(map(int, str(j))))

    for i in range(len(check)):
        rep_num1 = []
        n = 0
        for j in range(len(check[i]) - 1):
            if check[i][j] <= check[i][j + 1]:
                if check[i][j] == check[i][j + 1]:
                    if check[i][j + 1] not in rep_num1:
                        rep_num1.append(check[i][j + 1])
                        n += 1
                        if n >= 2:
                            final.append(number_list[i])
            else:
                break

    print('%d numbers meet the criteria'% len(final))

password()