quick_sort <- function(arr) {
  if (length(arr) <= 1) {
    return(arr)
  }
  
  pivot <- arr[1]
  left <- arr[arr < pivot]
  middle <- arr[arr == pivot]
  right <- arr[arr > pivot]
  
  return(c(quick_sort(left), middle, quick_sort(right)))
}

vect <- c(2, 9, 0, -1, 6, 9, 8, 89, -5)
cat("Unsorted vector is:", vect, "\n")
sorted_vector <- quick_sort(vect)
cat("Sorted vector is:", sorted_vector, "\n")
