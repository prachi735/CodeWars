def divisors(integer):
    l = [a for a in range(2,int(integer/2)+1) if integer % a == 0 ]
    return "{} is prime".format(integer) if len(l) is 0 else l
