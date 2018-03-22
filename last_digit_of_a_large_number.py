def last_digit(n1, n2):
    if n2 == 0:
        return 1
    exp = 4
    if n2 % 4 == 0:
        exp = 4
    else:
        exp = n2 % 4
    last_digit_in_base = n1 % 10
    ldigit = pow(last_digit_in_base,exp)
    return ldigit % 10
