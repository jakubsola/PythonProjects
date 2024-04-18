import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def rsserr(a,b):
    b = np.matrix(b)
    return (a[0,0]-b[0,0])**2 + (a[0,1]-b[0,1])**2

def u_clusters(data, v, m):
    U = np.zeros(data.shape)
    for i in range(data.shape[0]):
            U[i,0] = 1 / ((rsserr(data[i], v.iloc[0])) / (rsserr(data[i], v.iloc[0])) + (rsserr(data[i], v.iloc[0])) / (rsserr(data[i], v.iloc[1])))**(2/(m-1))
            U[i,1] = 1 - U[i,0]
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
            sum_xc1 += U[i,0] * data[i,0]
            sum_yc1 += U[i,0] * data[i,1]
            sum_c1 += U[i,0]
            sum_xc2 += U[i,1] * data[i,0]
            sum_yc2 += U[i,1] * data[i,1]
            sum_c2 += U[i,1]
    v[0, 0] = sum_xc1 / sum_c1
    v[0, 1] = sum_yc1 / sum_c1
    v[1, 0] = sum_xc2 / sum_c2
    v[1, 1] = sum_yc2 / sum_c2
    v = pd.DataFrame(data=v, columns=['x', 'y'])
    return v

def quality(U_0, U_1):
    q = 0
    for k in range(U_0.shape[0]):
        q += np.abs(U_0[k,0] - U_1[k,0])
    return q

def C_means(data, C, m, eps):
    data_df = pd.DataFrame(data=data, columns=['x', 'y'])
    min_values = data_df.min()
    max_values = data_df.max()
    v_0 = np.random.uniform(low=min_values, high=max_values, size=(C, data_df.shape[1]))
    v_0 = pd.DataFrame(v_0, columns=['x', 'y'])
    U_0 = u_clusters(data, v_0, m)
    it = 0
    while True:
        it += 1
        v = prototype_v(U_0, data)
        U_1 = u_clusters(data, v, m)
        q = quality(U_0, U_1)
        if q <= eps:
            break
        else:
            U_0 = U_1
    return v, U_1, it
def main():
    data = [
        [4.62752830, 7.07828330],
        [5.09277850, 7.29750460],
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
        [7.67714750, 0.14355195]
    ]
    data = np.asmatrix(data)
    C = 2
    m = 5
    eps = 10 ** (-5)
    v, U, it = C_means(data, C, m, eps)

    data_ar = np.array(data)
    colors = ['red' if row.tolist()[0] >= row.tolist()[1] else 'green' for row in U]
    plt.scatter((data_ar[:, 0]), data_ar[:, 1], color=colors)
    plt.show()
    print(v, '\nNumber of iterations:',it)

if __name__ == "__main__":
    main()