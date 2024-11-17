# Binary Search Tree (BST) Node constructor
bst <- function(value) {
  list(value = value, left = NULL, right = NULL)
}

# Insert function for BST
insert <- function(root, value) {
  if (is.null(root)) {
    return(bst(value))
  }
  
  if (value < root$value) {
    root$left <- insert(root$left, value)
  } else {
    root$right <- insert(root$right, value)
  }
  
  return(root)
}

# Inorder traversal to get sorted values from BST
inorder <- function(root, result = c()) {
  if (!is.null(root)) {
    result <- inorder(root$left, result)
    result <- c(result, root$value)
    result <- inorder(root$right, result)
  }
  return(result)
}

# Sorting function using BST
bst_quick_sort <- function(arr) {
  root <- NULL
  for (value in arr) {
    root <- insert(root, value)
  }
  
  sorted_arr <- inorder(root)
  return(sorted_arr)
}

# Test BST-based sort
a <- c(3, 6, 8, 10, 101, 1, -1, 21)
sorted_arr <- bst_quick_sort(a)
print("Sorted array using BST:")
print(sorted_arr)
