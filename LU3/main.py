import numpy as np

def decompress(A):
    n = A.shape[0] #wymiar macierzy
    M = np.zeros((n, n))
    for i in range(n):
        M[i, i] = A[i, 1]
        if(i != 0): M[i, i-1] = A[i, 0]
        if (i != n-1): M[i, i + 1] = A[i, 2]
    return M

def main():
    sa = np.array([[0, 7, 9], [7, 10, 2], [8, 4, 8], [9, 1, 10], [10, 1, 3], [9, 3, 10], [6, 3, 5], [2, 2, 4], [5, 9, 3], [4, 7, 0]], dtype=np.double)
    sb = np.array([[0, 4, 4], [5, 5, 8], [10, 2, 2], [6, 8, 5], [10, 7, 2], [1, 6, 5], [10, 4, 8], [3, 1, 1], [10, 6, 8], [10, 9, 0]], dtype=np.double)
    A = decompress(sa)
    B = decompress(sb)
    print("A * B = \n", np.dot(A, B))

if __name__ == "__main__":
    main()