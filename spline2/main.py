import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x-np.sin(x)

def use_f(func, x):
    return func(x)

def c_spline(x, y, n):
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

def l_spline(x, y, n):
    l = []
    for i in range(n):
        A = np.poly1d([1, -x[i + 1]]) / (x[i] - x[i + 1])
        B = np.poly1d([1, -x[i]]) / (x[i + 1] - x[i])
        l.append(A * y[i] + B * y[i+1])
    return l
def err(x, p, n):
    e = 0
    for i in range(n):
        x_int = np.linspace(x[i], x[i+1], num=1000)
        error = np.abs(p[i](x_int) - use_f(f, x_int))
        temp = np.max(error)
        if e < temp:
            e = temp
    return e
def main():
    n = 3
    x = np.linspace(2, 10, num=n+1)
    y = use_f(f, x)
    c = c_spline(x, y, n)
    l = l_spline(x, y, n)
    plt.subplots_adjust(hspace=0.5, wspace=0.4)
    plt.subplot(2, 2, 1)
    for i in range(n):
        x_plot = np.arange(x[i], x[i+1], 0.05)
        plt.plot(x_plot, c[i](x_plot), label='c{}'.format(i+1))

    x_plot = np.arange(2, 10, 0.05)
    plt.plot(x_plot, use_f(f, x_plot), label='x-sinx')
    plt.scatter(x, y, s=25, c='r')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Cubic Spline')
    plt.legend(loc='upper left', fontsize='x-small')

    plt.subplot(2, 2, 2)
    for i in range(n):
        x_plot = np.arange(x[i], x[i+1], 0.05)
        plt.plot(x_plot, l[i](x_plot), label='l{}'.format(i+1))
    x_plot = np.arange(2, 10, 0.05)
    plt.plot(x_plot, use_f(f, x_plot), label='x-sinx')
    plt.scatter(x, y, s=25, c='r')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Linear Spline')
    plt.legend(loc='upper left', fontsize='x-small')

    plt.subplot(2, 2, 3)
    for i in range(n):
        x_plot = np.arange(x[i], x[i+1], 0.001)
        plt.plot(x_plot, np.abs(c[i](x_plot)-use_f(f,x_plot)))
    plt.xlabel('x')
    plt.ylabel('error')
    plt.title('Cubic Spline Error')

    plt.subplot(2, 2, 4)
    for i in range(n):
        x_plot = np.arange(x[i], x[i + 1], 0.001)
        plt.plot(x_plot, np.abs(l[i](x_plot) - use_f(f, x_plot)))
    plt.xlabel('x')
    plt.ylabel('error')
    plt.title('Linear Spline Error')

    plt.show()
    error_c = err(x, c, n)
    error_l = err(x, l, n)
    print('Max error for cubic spline: ' + '{:.5f}'.format(error_c) + "\nMax error for linear spline: " + '{:.5f}'.format(error_l))


if __name__ == "__main__":
    main()