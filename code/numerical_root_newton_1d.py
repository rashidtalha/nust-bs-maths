import numpy as np

def get_estimate(xval, func, deriv):
    if deriv(xval) == 0:
        raise AssertionError("Division by zero!")
    return xval - (func(xval) / deriv(xval))


f = lambda x: x**2 - 29
dfdx = lambda x: 2*x

x = 3.3
print(f"Initial guess: {x:.5f}")

for j in range(8):
    x = get_estimate(x, f, dfdx)
    print(f"After {j+1} iterations: {x:.7f}")
