# Programme for using  loop function for iterating numbers from 1 to 50 and adding them and printing the sum of all the numbers in the given format.
# Taking a dummy varibale for storing the total sum-Total_sum
Total_sum=0
#  step 1--- Uses a for loop to iterate over numbers from 1 to 50.Iterating 50 times using range function by adding the value of x from 1 to 50 to the already taken variable Total_sum
for x in range(1,51):
#2.   Calculates the sum of all integers in this range.
    Total_sum=Total_sum+x
# Printing the total sum of the range. Displays the final sum.
print(f"The sum of numbers from 1 to 50 is : {Total_sum}")
