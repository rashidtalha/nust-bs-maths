import numpy as np

def new_bounds(x_lower, x_r, x_upper, func):
    if x_r == x_lower:
        return x_lower, x_lower
    elif x_r == x_upper:
        return x_upper, x_upper
    else:
        f_lower = func(x_lower)
        f_r = func(x_r)
        f_upper = func(x_upper)

        if f_lower * f_r < 0:
            return x_lower, x_r
        else:
            return x_r, x_upper

def get_estimate(x_lower, x_upper, func):
    if x_lower == x_upper:
        return x_lower

    f_lower = func(x_lower)
    f_upper = func(x_upper)
    
    if f_lower == 0:
        return x_lower
    elif f_upper == 0:
        return x_upper
    else:
        return (x_lower * f_upper - x_upper * f_lower) / (f_upper - f_lower)


f = lambda x: x**4 - 11*x + 8
# f = lambda x: (x-1)*(x+8)

x_l, x_u = 1, 2

for _ in range(4):
    x_r = get_estimate(x_l, x_u, f)
    print(f"Current bracket: {x_l:.5f}, {x_u:.5f}")
    print(f"Estimated root: {x_r:.5f}")
    print()
    x_l, x_u = new_bounds(x_l, x_r, x_u, f)

print(f"Final bracket: {x_l:.5f}, {x_u:.5f}")
