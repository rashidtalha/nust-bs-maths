import numpy as np
import matplotlib.pyplot as plt

x_data, h = np.linspace(0, 10, 11, retstep=True)
print(h)

t = np.linspace(x_data[0],x_data[-1],100)
func = lambda x: np.exp(np.sin(x))
y_data = func(x_data)
# y_data = np.array([17,22,21,25])

def factorial(n):
    if n == 0: return 1
    if n == 1: return 1
    return n * factorial(n-1)

def backward_diff_array(x, y):
    npts = len(x)
    diffs = np.zeros((npts, npts))
    diffs[:,0] = y
    for order in range(1, npts):
        diffs[order:, order] = diffs[order:, order-1] - diffs[order-1:-1, order-1]
    return diffs

def p_forward(tbl, x, x0, h, n=None):
    if n is None: n = tbl.shape[-1]

    s = (x - x0) / h
    val = 0
    for j in range(n):
        w = np.prod([s-k for k in range(j)], initial=1.0) / factorial(j)
        val += tbl[j,j] * w

    return val

def p_backward(tbl, x, x0, h, n=None):
    if n is None: n = tbl.shape[-1]

    s = (x - x0) / h
    val = 0
    for j in range(n):
        w = np.prod([s+k for k in range(j)], initial=1.0) / factorial(j)
        val += tbl[-1,j] * w

    return val

res = backward_diff_array(x_data, y_data)

x  = 9.2

pb = p_backward(res, x, x_data[-1], h)
pf = p_forward(res, x, x_data[0], h)
print(pb, pf)


fig, ax = plt.subplots()
ax.plot(t, func(t))
ax.plot(x_data, y_data, "o")
ax.plot([x,],[pb,], "v")
ax.plot([x,],[pf,], "^")
plt.show()

