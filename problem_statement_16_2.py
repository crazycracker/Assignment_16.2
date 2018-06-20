import math

print("Enter the number of inputs")
n = int(input())

print("Enter the input values")
li = list()

for x in range(n):
    li.append(int(input()))

# step 1: calculate mean of the given data

mean = float(sum(li)/n)

# step 2: for each point, find the sum of the squares of its distance to the mean

sum_of_squared_distances = 0.0

for point in li:
    dist = (point - mean)
    dist = dist*dist
    sum_of_squared_distances += dist

# step 3: divide the sum of squared distances by the count of points

variance = float(sum_of_squared_distances/n)

# step 4: output the calculated variance

print("variance is " + str(variance))