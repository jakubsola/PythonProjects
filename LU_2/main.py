import numpy as np


def lu(A):
    n = A.shape[0]
    L = np.eye(n)
    U = A.copy()
    pivot = 0
    for j in range(0,n):
        for i in range(pivot+1,n):
            c = -U[i,j]/U[pivot,j]
            U[i,:] = c*U[pivot,:] + U[i,:]
            L[i,pivot] = -c
        pivot += 1
    np.round(L, decimals=int(-np.log10(0.00005)))
    np.round(U, decimals=int(-np.log10(0.00005)))
    return L,U

def main():
    A = np.array([[1, 1, 2, 4], [5, 1, 2, 4], [-2, 2, 1, 8], [5, 2, 4, 1]], dtype=np.double)
    L, U = lu(A)
    print("L:\n", L)
    print("U:\n", U)
    print("L*U=\n", np.dot(L, U))
    print("det(A) = ", np.round(np.linalg.det(A), decimals=int(-np.log10(0.00005))))
    print("det(L) * det(U) = ", np.round(np.linalg.det(L) * np.linalg.det(U), decimals=int(-np.log10(0.00005))))

if __name__ == "__main__":
    main()