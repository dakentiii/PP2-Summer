def check(c, e):
    if c not in d:
        return 0
    elif d[c] == e:
        return 1
    else:
        return check(d[c], e)
 