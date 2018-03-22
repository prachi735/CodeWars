Simultaneous Equations - Three Variables

import numpy as np
def solve_eq(eq):
    # your code here
    a = []
    b = []
    for e in eq:
        a.append(e[:len(e)-1])
        b.append(e[len(e)-1])
    solution = np.linalg.solve(a,b)
    print(list(solution))
    return [round(x) for x in list(solution)]
