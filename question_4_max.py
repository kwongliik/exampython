def max_value(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

max = max_value(30.34, 22.23, 18.89)
print(f"maximum is {max}")