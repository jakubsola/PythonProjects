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
        [8.57227460, 1.25078230]
    ]
    data = np.asmatrix(data)
    C = 2
    eps = 10 ** (-5)
    v = np.zeros([20, 2])
    it = list()
    for m in range(10):
        v_f, U_f, it_f = C_means(data, C, m+2, eps)
        v_f = np.array(v_f)
        v[2 * m, 0] = v_f[0, 0]
        v[2 * m, 1] = v_f[0, 1]
        v[2 * m + 1, 0] = v_f[1, 0]
        v[2 * m + 1, 1] = v_f[1, 1]
        it.append(it_f)
    print(v, '\nNumber of iterations:',it)
    fig, ax = plt.subplots()
    data_points = np.array(data)
    ax.scatter(data_points[:, 0], data_points[:, 1], color='gray', alpha=0.5)
    legend_labels = {}
    colors = plt.cm.gist_rainbow(np.linspace(0, 1, len(v) // 2))
    new_colors = np.repeat(colors, 2, axis=0)
    for i in range(0, len(v), 2):
        label = f"m = {i // 2 + 2}"
        if label not in legend_labels:
            ax.scatter(v[i:i + 2, 0], v[i:i + 2, 1], color=new_colors[i], label=label)
            legend_labels[label] = True
        else:
            ax.scatter(v[i:i + 2, 0], v[i:i + 2, 1], color=new_colors[i])
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
