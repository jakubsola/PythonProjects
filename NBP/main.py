import numpy as np
import pandas as pd

def generate_poisson(l):
    P = 1
    S = 1
    q = np.exp(-l)
    while S > q:
        U = np.random.uniform(0, 1)
        S *= U
        P += 1
    return P - 1
def main():
    N = 1500
    M = 50
    col_names = ['Max całkowity zysk klienta (gr)', 'Min całkowity zysk klienta (gr)', 'Max całkowity zysk sklepu (gr)', 'Min całkowity zysk sklepu (gr)']
    row_names = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #-----------------1----------------
    tab1 = np.zeros((10, 4))
    for L in range(1, 11):
        A = np.zeros((M + 1, N + 1))
        for i in range(N):
            for j in range(M):
                A[j, i] = ((9 * generate_poisson(L)) % 10) % 5
                if(A[j, i] == 3 or A[j, i] == 4): A[j, i] -= 5
                A[M, i] += A[j, i]
                A[j, N] -= A[j, i]
        k_max1 = max(A[M, :-1])
        k_min1 = min(A[M, :-1])
        s_max1 = max(A[:-1, N])
        s_min1 = min(A[:-1, N])
        tab1[L-1, :] = [k_max1, k_min1, s_max1, s_min1]
    df1 = pd.DataFrame(tab1, index=row_names, columns=col_names)
    df1.columns.name = 'Tylko towary promocyjne'
    df1.index.name = 'Wartość oczekiwana L'
    print(df1)

    #-----------------2-------------------------

    tab2 = np.zeros((10, 4))
    for L in range(1, 11):
        B = np.zeros((M + 1, N + 1))
        for i in range(N):
            for j in range(M):
                B[j, i] = ((9 * generate_poisson(L) + np.random.choice(10)) % 10) % 5
                if(B[j, i] == 3 or B[j, i] == 4): B[j, i] -= 5
                B[M, i] += B[j, i]
                B[j, N] -= B[j, i]
        k_max2 = max(B[M, :-1])
        k_min2 = min(B[M, :-1])
        s_max2 = max(B[:-1, N])
        s_min2 = min(B[:-1, N])
        tab2[L-1, :] = [k_max2, k_min2, s_max2, s_min2]
    df2 = pd.DataFrame(tab2, index=row_names, columns=col_names)
    df2.columns.name = 'Ostatnia cyfra sumy cen z rozkładu jednostajnego'
    df2.index.name = 'Wartość oczekiwana L'
    print(df2)

    # -----------------3-------------------------

    tab3 = np.zeros((10, 4))
    alpha = 1 / np.log(11)
    pr = np.zeros(10)
    pr[0] = alpha * np.log(1 + 1 / 10)
    for k in range(1, 10):
        pr[k] = alpha * np.log(1 + 1 / k)
    for L in range(1, 11):
        C = np.zeros((M + 1, N + 1))
        for i in range(N):
            for j in range(M):
                C[j, i] = ((9 * generate_poisson(L) + np.random.choice(10, p = [pr[0], pr[1], pr[2], pr[3], pr[4], pr[5], pr[6], pr[7], pr[8], pr[9]])) % 10) % 5
                if (C[j, i] == 3 or C[j, i] == 4): C[j, i] -= 5
                C[M, i] += C[j, i]
                C[j, N] -= C[j, i]
        k_max3 = max(C[M, :-1])
        k_min3 = min(C[M, :-1])
        s_max3 = max(C[:-1, N])
        s_min3 = min(C[:-1, N])
        tab3[L - 1, :] = [k_max3, k_min3, s_max3, s_min3]
    df3 = pd.DataFrame(tab3, index=row_names, columns=col_names)
    df3.columns.name = 'Ostatnia cyfra sumy cen z rozkładu Benforda'
    df3.index.name = 'Wartość oczekiwana L'
    print(df3)

if __name__ == "__main__":
    main()
