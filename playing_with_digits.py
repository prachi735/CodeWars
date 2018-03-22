def dig_pow(n, p):
    s2 = sum([int(d)**(p+i) for i,d in enumerate(str(n))])
    print(s2)
    if s2 % n == 0:
        return s2/n
    return -1
