def max_value(a, b, c, d):
    if a > b and a > c and a > d:
        return a
    elif b > a and b > c and b > d:
        return b
    elif c > a and c > b and c > d:
        return c
    else:
        return d

max = max_value(30.34, 22.23, 48.89, 27.49)
print(f"Maximum is {max}")