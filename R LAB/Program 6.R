# Load the markovchain package
library("markovchain")

# Define the transition matrix for your Markov chain
transition_matrix <- matrix(c(0.8, 0.2, 0.4, 0.6), nrow = 2, byrow = TRUE)

# Define the states
states <- c("state A", "state B")

# Create a markovchain object
My_markov_chain <- new("markovchain", states = states, transitionMatrix = transition_matrix)

# Find the stationary distribution (use steadyStates)
stationary_dist <- steadyStates(My_markov_chain)

# Print the stationary distribution
cat("Stationary distribution:\n")
print(stationary_dist)
