

def change(val, denoms):
    if val == 0:
        return []
    for (i,d) in enumerate(denoms):
        if (val - d) >= 0:
            res  = change(val - d, denoms[i:])
            res.append(d)
            return res


print change(177, [100, 50, 25, 10, 5, 1])

