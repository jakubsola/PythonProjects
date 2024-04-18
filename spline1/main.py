import numpy as np
import matplotlib.pyplot as plt

def spline_pol(x, y):
    p = []
    dy1 = (3 / (x[2] - x[0])) * (((y[2] - y[1]) / (x[2] - x[1])) - ((y[1] - y[0]) / (x[1] - x[0])))
    for i in range(2):
        if i == 0:
            A = np.poly1d([1, -x[i + 1]]) / (x[i] - x[i + 1])
            B = np.poly1d([1, -x[i]]) / (x[i + 1] - x[i])
            D = (1 / 6) * (B**3 - B) * (x[i+1] - x[i])**2
            p.append(A * y[0] + B * y[1] + D * dy1)
        else:
            A = np.poly1d([1, -x[i + 1]]) / (x[i] - x[i + 1])
            B = np.poly1d([1, -x[i]]) / (x[i + 1] - x[i])
            C = (1 / 6) * (A**3 - A) * (x[i + 1] - x[i])**2
            p.append(A * y[1] + B * y[2] + C * dy1)
    return p
def main():
    x = np.array([2, 4, 6], dtype=float)
    y = np.array([1, 4, 2], dtype=float)
    z = spline_pol(x, y)
    x1 = np.arange(2, 4, 0.05)
    x2 = np.arange(4, 6, 0.05)
    plt.plot(x1, z[0](x1), label='p1')
    plt.plot(x2, z[1](x2), label='p2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Spline')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()