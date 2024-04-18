Numerical Methods – laboratory

Below is a description of all the tasks associated with each laboratory exercise (5 weeks - 5
exercises). Each laboratory exercise is associated with a different data set.

1 Matrix operations
Task 1 and 2 require matrix A available from the data file MO-Task1&2-DataX.txt.
Task 3 requires matrices sa and sb available from the data file MO-Task3-DataX.txt (X is
index of assigned data set.
1. Calculate L and U matrices for the A matrix without pivot matrix P. Write the L and U
matrices down with 0.00005 precision.
2. Calculate matrices L and U, as well as P, L and U, by means of Matlab lu(A) command.
Show that the determinant of the A matrix can be obtained as a product of determinants of decomposed matrices. Write the results down with 0.00005 precision.
3. Rewrite two arrays from sparse form into classical matrices. Multiply them and write
down the resulting matrix.

2 Spline interpolation
Data file SI-Task1-DataX.txt includes three data pairs that are nodes and function values
for the nodes.
Data file SI-Task2-DataX.txt includes two sub-tasks (two different data sets) where interval,
number of nodes and interpolated function are indicated. Please use only the first function.
Data file SI-Task3-DataX.txt includes interval, three different number of nodes (hence three
sub-tasks are to do) and interpolated function. Please use only the "middle" value, i.e. six
nodes (i=0,1,2,3,4,5).
1. Calculate two spline polynomials for the three (i = 0, 1, 2) nodes. If possible, present
the result in the figure.
2. Do linear and cubic spline interpolation for the two sets of following data: the interval,
number of nodes (i = 0, 1, 2, 3) and the function. Make plots. Calculate max(|E|), where
E is the error for each case. Make plots. ATTENTION: There are two functions. Please
use only the first function!
3. Do interpolation by means of the Lagrange polynomial and the cubic spline for the given function and interval, and different numbers of nodes (n = [3, 5, 10]). Make plots.
Calculatemax(|E|) for each case. Make plots. ATTENTION: There are three different
numbers of nodes in data files. Please use only the "middle" value, i.e. six nodes (i=0,1,2,3,4,5).
The material was downloaded from the Remote Education Platform of the Silesian University of Technology – 2022
The material was downloaded from the Remote Education Platform of the Silesian University of Technology – 2022

3 Data clustering
Data file DC-DataX.txt contains all data required for the whole laboratory exercise. Two column data relate to two dimensional coordinates of the data points (they can be presented as
points of x and y coordinates)
1. For the given data set, please compute and write down the cluster prototypes using Kmeans clustering method. Set the tolerance limit ² = 10−5
. Moreover, please write the
number of executed iterations. The partition matrix should be initialized randomly.
Assume that the number of clusters K = 2.
2. For the given data set, please compute and write down the cluster prototypes using
fuzzy C-means clustering method. Set the exponent m = 2 and the tolerance limit ² =
10−5
. Moreover, please write the number of executed iterations. The partition matrix
should be initialized randomly. Assume that the number of clusters C = 2.
3. Figure out the influence of exponent value m ∈ [1, ··· , 10] on the result of clustering
(number of iterations and the values of prototypes).

4 Linear discriminant analysis
Data file LDA-DataX.txt contains all data required for the whole laboratory exercise. First
and second column are two dimensions of training data set. The third and fourth column are
two dimensions of testing data set. The last column relates to training/testing data class labels.
1. For the given training data set and their class labels, find linear discriminant function
weights utilizing the perceptron criterion algorithm. Assume learning rate ρ = 0.25.
When learning is finished (all training data are classified properly or the maximal number of iteration is achieved):
(a) write down the number of iterations,
(b) show the linear discriminant function and training data set,
(c) calculate and write down the training accuracy as the percentage number of correctly classified training data,
(d) perform classification of the testing data set, calculate and write down the testing
accuracy.
2. Repeat task 1) but instead of perceptron criterion, utilize the relaxation algorithm.
Assume ρ = 0.1 and B = 0.5.
3. Perform necessary calculations to obtain classic Figher’s linear discriminant analysis.
The material was downloaded from the Remote Education Platform of the Silesian University of Technology – 2022
The material was downloaded from the Remote Education Platform of the Silesian University of Technology – 2022

5 Eigenvalues and eigenvectors
Data file HTD-DataX.txt includes one 3×3 matrix for which their eigenvalues and eigenvectors needs to be calculated in the following tasks.
1. Calculate the first eigenvalue and the eigenvector of the matrix by means of the power
iteration method. Do not forget to consider the sign of the eigenvalue. Note number
of iterations that is necessary to calculate the values with 0.0005 precision. Write down
results to your report.
2. Calculate all eigenvalues and eigenvectors of the matrix by means of the symmetrical
matrix property. Write down matrices after deflation and all the eigenvalues and eigenvectors. Verify the eigenvalues and the eigenvectors basing on their definitions. Write
down the verification to your report.
3. Calculate all eigenvalues and eigenvectors of the matrix by means of Householder
transformation. Write down the values and the vectors, as well as H matrices to your
report. Verify the eigenvalues and the eigenvectors basing on their definitions. Write
down the verification to your report.

6 Data modeling
Data file DM-Task1&2-DataX.txt contain matrix of five columns and 100 rows. Each column
has following meaning: age, height, weight, speed in the city and speed outside the city.
Data file DM-Task3-DataX.txt includes collection of two dimensional points related to the
task of polynomial regression.
Data file DM-Task4-DataX.txt has data set expressed as 5×10 matrix. The matrix is necessary
for solving Task 4.
1) Determine mean and variance of data: age, height, weight, speed in the city, speed outside
the city, for data with and without an outlier. Comment on mean and variance.
2) Make a plot of speed in the city vs. speed outside the city and calculate the correlation
coefficient. Are these data correlated?
3) Determine coefficient of polynomials of the first (ax + b) and the second (ax2 + bx + c)
order by means of least square method.
4) Find covariance matrix, its eigenvectors and eigenvalues, decrease space observation dimension by two. Find out how big is the error after decreasing the space and transform data.
The material was downloaded from the Remote Education Platform of the Silesian University of Technology – 2022
