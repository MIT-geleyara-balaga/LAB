#install and load the required package
if(! require(Deriv)){
  install.packages("Deriv")
  library(Deriv)
}

# Simple vector of numbers
numbers <- c(1, 2, 3, 4, 5)

# Calculate cumulative sum
cumulative_sum <- cumsum(numbers)
cat("Cumulative sum:", cumulative_sum, "\n")

# Calculate cumulative product
cumulative_product <- cumprod(numbers)
cat("Cumulative product:", cumulative_product, "\n")

# Calculate minimum and maximum
min_value <- min(numbers)
max_value <- max(numbers)
cat("Minimum:", min_value, "\n")
cat("Maximum:", max_value, "\n")

# Define a function: f(x) = x^2
f <- function(x) x^2

# Calculate the derivative of f(x) = x^2
derivative <-Deriv(f)
cat("Derivative of f(x) = x^2 at x=2:", derivative(2), "\n")

# Integrate the function f(x) = x^2 from 1 to 5
integrate <- integrate(f, lower = 1, upper = 5)
cat("Integral of f(x) = x^2 from 1 to 5:", integrate $ value, "\n")