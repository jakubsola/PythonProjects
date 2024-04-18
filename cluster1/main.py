import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def rsserr(a,b):
    b = np.matrix(b)
    return np.square((a[0,0]-b[0,0])**2 + (a[0,1]-b[0,1])**2)

def u_clusters(data, c):
    U = np.zeros(data.shape)
    for i in range(data.shape[0]):
        if rsserr(data[i], c.iloc[0]) <= rsserr(data[i], c.iloc[1]):
            U[i,0] = 1
        else:
            U[i,1] = 1
    return U

def prototype_v(U, data):
    v = np.zeros((2,2))
    sum_xc1 = 0
    sum_xc2 = 0
    sum_yc1 = 0
    sum_yc2 = 0
    sum_c1 = 0
    sum_c2 = 0
    for i in range(data.shape[0]):
        if U[i,0] == 1:
            sum_xc1 += data[i,0]
            sum_yc1 += data[i,1]
            sum_c1 += 1
        else:
            sum_xc2 += data[i,0]
            sum_yc2 += data[i,1]
            sum_c2 += 1
    v[0, 0] = sum_xc1 / sum_c1
    v[0, 1] = sum_yc1 / sum_c1
    v[1, 0] = sum_xc2 / sum_c2
    v[1, 1] = sum_yc2 / sum_c2
    v = pd.DataFrame(data=v, columns=['x', 'y'])
    return v

def K_means(data, K, eps):
    data_df = pd.DataFrame(data=data, columns=['x', 'y'])
    min_values = data_df.min()
    max_values = data_df.max()
    while True: #losujemy dwa centroidy tak, żeby nie bylo sytuacji w ktorej z jednego jest blizej do wszystkich punktow niz z drugiego
        centroids = np.random.uniform(low=min_values, high=max_values, size=(K, data_df.shape[1]))
        centroids = pd.DataFrame(data=centroids, columns=['x', 'y'])
        U_0 = u_clusters(data, centroids)
        if U_0.sum(axis=0)[0] != data.shape[0] or U_0.sum(axis=0)[1] != data.shape[0]:
            break
    it = 0
    while True:
        it += 1
        v_0 = prototype_v(U_0, data)
        U_1 = u_clusters(data, v_0)
        s = 0
        for i in range(data.shape[0]):
            if U_0[i,0] != U_1[i,0]:
                s +=2
        if s <= eps:
            break
        else:
            U_0 = U_1
    return v_0, U_1, it
def main():
    data = [
        [4.62752830, 7.07828330],
        [5.09277850, 7.29750460],
        [5.05294280, 6.79229910],
        [5.20807690, 6.67230680],
        [5.18024740, 6.45782830],
        [5.30769090, 7.30586920],
        [5.31933720, 6.83899610],
        [4.88400300, 7.33065310],
        [5.32755900, 7.03480380],
        [5.03280360, 6.60466300],
        [5.37213600, 7.29227490],
        [5.41033940, 7.15924750],
        [5.27488080, 7.02720140],
        [4.89700880, 6.70802690],
        [5.07677620, 6.53975690],
        [5.02021540, 7.35118530],
        [5.06525010, 7.26764890],
        [4.80454950, 7.73982090],
        [5.02380450, 7.38074770],
        [4.99601510, 6.95003150],
        [8.46523080, -0.00291594],
        [8.07654330, 0.72304788],
        [7.40009720, 2.27199440],
        [7.69016020, 1.27905350],
        [8.08957240, 1.27957830],
        [7.59479030, 2.07079130],
        [7.88768460, 0.44438654],
        [8.38275350, 0.69348660],
        [8.21199060, 0.26213366],
        [7.86550940, 1.76837710],
        [8.25625730, 2.15477280],
        [7.79479590, 1.71182380],
        [7.67714750, 0.14355195],
        [8.24630840, 1.47685650],
        [8.34369430, 0.70301601],
        [7.34241200, 1.12931880],
        [8.25530740, 0.63634076],
        [7.46684790, 1.54736620],
        [8.13190080, 0.37510221],
        [8.57227460, 1.25078230],
    ]
    data = np.asmatrix(data)
    K = 2
    eps = 10 ** (-5)
    v, U, it = K_means(data, K, eps)

    data_ar = np.array(data)
    colors = ['red' if row.tolist() == [1, 0] else 'green' for row in U]
    plt.scatter((data_ar[:, 0]), data_ar[:, 1], color=colors)
    plt.show()
    print(v, '\nNumber of iterations:',it)

if __name__ == "__main__":
    main()