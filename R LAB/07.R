matrix_A <- matrix(1:4,nrow = 2)
matrix_B <- matrix(5:8,nrow = 2)

determinant_A <- det(matrix_A)
cat("Determinant of Matrix A : ",determinant_A,"\n")

inverse_A <- solve(matrix_A)
cat("Inverse of matrix A : \n")
print(inverse_A)