# pseudo code example:

# initialise variables:
# sum_of_squares = 0
# sum = 0
# i = 1

# while i <= 100:
#    sum_of_squares = sum_of_squares + i*i
#    sum = sum + i
#    i += 1

#    square_of_sum = sum * sum
#    diff = square_of_sum - sum_of_squares
#    display diff
    
sum_of_squares = 0
sum = 0
i = 1

while i <= 100:
    sum_of_squares = sum_of_squares + i*i
    sum = sum + i
    i += 1
    
square_of_sum = sum * sum
diff = square_of_sum - sum_of_squares
print(diff)

# alternatively with range: 
sum_of_squares = 0
sum = 0

for i in range(1,101):
    sum_of_squares = sum_of_squares + i*i
    sum = sum + i
    
square_of_sum = sum * sum
diff = square_of_sum - sum_of_squares
print(diff)