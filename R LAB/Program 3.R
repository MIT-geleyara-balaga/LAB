# Basic operations
a <- 11
b <- -4
sum_result <- a + b
print(sum_result)
diff_result <- a - b
print(diff_result)
product_result <- a * b
print(product_result)
division_result <- a / b
print(division_result)
modulus_result <- a %% b
print(modulus_result)

# Control structure (if_else)
if (a > b) {
  print("a is large")
} else if (a < b) {
  print("a is small")
} else {
  print("a is equal to b")
}

# Default values for arguments
my_function <- function(Country = "INDIA") {
  print(paste("I AM FROM", Country))
}

my_function() # Will use the default value, which is "INDIA"

# Function with a list as output
res <- function() {
  v <- c(1, 2, 5, 3, 8)
  m <- matrix(1:8, ncol = 4)
  v1 <- mean(v)
  m1 <- min(m)
  l <- list(vec = v1, mat = m1)
  return(l) # Return the list containing the results
}

print(res())
