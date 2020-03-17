def password():
    # creating list of all number from 372 ** 2 to 809 ** 2
    number_list = [i for i in range(372 ** 2, 809 ** 2 + 1)]

    check = []  # list of divided numbers into list of digits
    final = []  # final list with number of results

    # making lists of all digit in each number
    for j in number_list:
        check.append(list(map(int, str(j))))

    # finding all numbers with given criteria
    for i in range(len(check)):
        rep_num1 = []  # support list to compare number of repeating values
        n = 0  # number of  repeats

        # checking all criteria for the password
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

    print('%d numbers meet the criteria' % len(final))


password()
