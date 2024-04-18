import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x-np.sin(x)

def use_f(func, x):
    return func(x)

def c_spline(x, y):
    n = len(x)-1
    c = []
    d = np.zeros(n+1)
    for i in range(n+1):
        if i == 0 or i == n:
            d[i] = 0
        else:
            d[i] = (3 / (x[i+1] - x[i-1])) * (((y[i+1] - y[i]) / (x[i+1] - x[i])) - ((y[i] - y[i-1]) / (x[i] - x[i-1])))
    for i in range(n):
        A = np.poly1d([1, -x[i + 1]]) / (x[i] - x[i + 1])
        B = np.poly1d([1, -x[i]]) / (x[i + 1] - x[i])
        C = (1 / 6) * (A ** 3 - A) * (x[i + 1] - x[i]) ** 2
        D = (1 / 6) * (B ** 3 - B) * (x[i + 1] - x[i]) ** 2
        c.append(A * y[i] + B * y[i+1] + C * d[i] + D * d[i+1])
    return c

def lag_spline(x, y):
    n = len(x)-1
    w = np.poly1d([0])
    for i in range(n+1):
        l = np.poly1d([1])
        for j in range(n+1):
            if j != i:
               l *= (np.poly1d([1, -x[j]]) / (x[i] - x[j]))
        w += l * y[i]
    return w
def err_c(x, p, n):
    e = 0
    for i in range(n):
        x_int = np.linspace(x[i], x[i+1], num=1000)
        error = np.abs(p[i](x_int) - use_f(f, x_int))
        temp = np.max(error)
        if e < temp:
            e = temp
    return e

def err_l(x, p):
    x_int = np.linspace(x[0], x[len(x)-1], num=1000)
    error = np.abs(p(x_int) - use_f(f, x_int))
    e = np.max(error)
    return e

def main():
    n = 5
    a = 2
    b = 10
    x = np.linspace(a, b, num=n+1)
    y = use_f(f, x)
    c = c_spline(x, y)
    l = lag_spline(x, y)
    plt.subplots_adjust(hspace=0.5, wspace=0.4)
    plt.subplot(2, 2, 1)
    for i in range(n):
        x_plot = np.arange(x[i], x[i+1], 0.05)
        plt.plot(x_plot, c[i](x_plot), label='c{}'.format(i+1))

    x_plot = np.arange(a, b, 0.05)
    plt.plot(x_plot, use_f(f, x_plot), label='x-sinx')
    plt.scatter(x, y, s=25, c='r')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Cubic Spline')
    plt.legend(loc='upper left', fontsize='xx-small')

    plt.subplot(2, 2, 2)
    plt.plot(x_plot, l(x_plot), label='lag')
    plt.plot(x_plot, use_f(f, x_plot), label='x-sinx')
    plt.scatter(x, y, s=25, c='r')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Lagrange Interpolation')
    plt.legend(loc='upper left', fontsize='x-small')

    plt.subplot(2, 2, 3)
    for i in range(n):
        x_plot = np.arange(x[i], x[i+1], 0.001)
        plt.plot(x_plot, np.abs(c[i](x_plot)-use_f(f,x_plot)))
    plt.xlabel('x')
    plt.ylabel('error')
    plt.title('Cubic Spline Error')

    plt.subplot(2, 2, 4)
    x_plot = np.arange(a, b, 0.05)
    plt.plot(x_plot, np.abs(l(x_plot) - use_f(f, x_plot)))
    plt.xlabel('x')
    plt.ylabel('error')
    plt.title('Lagrange Interpolation Error')

    plt.show()
    error_c = err_c(x, c, n)
    error_l = err_l(x, l)
    print('Max error for cubic spline: ' + '{:.5f}'.format(error_c) + "\nMax error for Lagrange interpolation: " + '{:.5f}'.format(error_l))


if __name__ == "__main__":
    main()