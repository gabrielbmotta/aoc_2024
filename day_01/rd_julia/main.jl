
# import stuff
using DelimitedFiles

# read in the file test.txt. it contains two columns of integers. read them into a matrix.
filepath = joinpath(@__DIR__, "input.txt")
data = readdlm(filepath, Int)

# sort list
sorted_column1 = sort(data[:, 1])
sorted_column2 = sort(data[:, 2])

# difference
difference = sorted_column1 - sorted_column2
abs_difference = abs.(difference)
distance = sum(abs_difference)

println("Task1: The distance is ", distance)

## Task 2:
# Initialize an empty dictionary
value_counts_2 = Dict{Int, Int}()

# Iterate through the vector and count values
for value in sorted_column2
    value_counts_2[value] = get(value_counts_2, value, 0) + 1
end

# iterare through vector 1 and get value counts from 2
similarity = 0

for value in sorted_column1
    global similarity
    n_counts_in_vec2 = get(value_counts_2, value, 0)
    similarity = similarity + value * n_counts_in_vec2
end

print("Task2: the similarity is ", similarity)