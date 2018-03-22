def get_pins(observed):
    adjacent_n = []
    pins = [[]]
    for n in observed:
        adjacent_n += [get_adjacent_n(n)]
    print(adjacent_n)
    for a in adjacent_n:
        print(a)
        pin = []
        for b in a:
            for i in pins:
        
                pin += [[b]+i]
        
        pins += pin

    possible_pins = []
    i = 0;
    for pin in pins:
        str_pin = ''
        for p in pin:
            str_pin += p
        possible_pins.append(str_pin[::-1])
    possible_pins = [i for i in possible_pins if len(i) == len(observed)]
    possible_pins.sort()
    print(possible_pins)
    return possible_pins
        
def get_adjacent_n(n):
    num_pad = [['1','2','3'],['4','5','6'],['7','8','9'],[None,'0',None]]
    indexes = [[i,k] for i,j in enumerate(num_pad) for k,m in enumerate(j) if n == m] # (row, col, n)
    r, c =  indexes[0][0], indexes[0][1]
    neighbors = [num_pad[r][c],None if r-1 <0 else num_pad[r-1][c],None if c-1 < 0 else num_pad[r][c-1], None if c+1>2 else num_pad[r][c+1], None if r+1 > 3 else num_pad[r+1][c]]
    return [x for x in neighbors if x != None]
