# Programme for using  loop function for iterating numbers from 1 to 50 and adding them and printing the sum of all the numbers in the given format.
# Taking a dummy varibale for storing the total sum-Total_sum
Total_sum=0
# iterating 50 times using range function by adding the value of x from 1 to 50 to the already taken variable Total_sum
for x in range(1,51):
    Total_sum=Total_sum+x
# Printing the total sum of the range.
print(f"The sum of numbers from 1 to 50 is : {Total_sum}")
