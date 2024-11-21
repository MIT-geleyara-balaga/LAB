#create vector and matrix
v1<-c(1,2,3)
v2<-c(4,5,6)
m1<-matrix(c(1,2,3,4,5,6),nrow=3,ncol=2)
m2<-matrix(7:12,nrow=2,byrow=TRUE)

#basic operations
#vector addition
vadd<-v1+v2
print("vector addition")
print(vadd)

#scalar multiplication(matrix)
scalar<-2
scalMult<-scalar*(m1)
print("scalar multiplication")
print(scalMult)

#transpose.matrix
transp<-t(m2)
print("transpose")
print(transp)

# Calculate the determinant
determinant_A <- det(m1)
cat("Determinant of m1 : ",determinant_A,"\n")

# Print the result
print("result")

#inverse
result<-solve(m1)
print("inverse")
print(result)

#eigen values and eigen vectors
eigen_result<-eigen(m1)
print("eigen value")
print(eigen_result $ value)
print("eigen vectors")
print(eigen_result $ result)
