def find_outlier(integers):
    odd = 0
    even = 0
    for i in integers[:3]:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    if even > odd:
        return [a for a in integers if a % 2 == 1][0]
    else:
        return [a for a in integers if a % 2 == 0][0]
