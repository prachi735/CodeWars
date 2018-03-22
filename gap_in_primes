import math
def gap(g, m, n):
    prime = 2
    for i in range(m, n+1):
        is_prime = True
        for j in range(2,int(math.sqrt(n))+1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            if i - prime == g:
                return [prime, i]
            else:
                prime = i
