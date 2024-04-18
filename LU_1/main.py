import numpy as np

def lu(A):
    n = A.shape[0]
    L = np.eye(n)
    U = np.zeros_like(A, dtype=np.double)
    for i in range(n):
        for j in range(i,n):
            s = 0
            for k in range(i):
                s += L[i, k] * U[k, j]
            U[i,j] = A[i, j] - s
        for j in range(i+1, n):
            s = 0
            for k in range(i):
                s += L[j, k] * U[k, i]
            L[j,i] = (A[j, i] - s) / U[i, i]
    np.round(L, decimals=int(-np.log10(0.00005)))
    np.round(U, decimals=int(-np.log10(0.00005)))
    return L, U

def main():
    A = np.array([[1, 1, 2, 4], [5, 1, 2, 4], [-2, 2, 1, 8], [5, 2, 4, 1]], dtype=np.double)
    L, U = lu(A)
    print("L:\n", L)
    print("U:\n", U)
    print("L*U=\n", np.dot(L, U))

if __name__ == "__main__":
    main()