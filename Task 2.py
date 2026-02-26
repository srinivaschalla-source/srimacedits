#Programme for taking a number as input and importing math module and to calculate square root, natural logarithm and sine of the number in radians and printng the results of the same. 
#import math module
import math
# Take a number as input
number=(input("Enter a number : "))
#convert the number to float for calculation purpose and save it in a new variable
number_float=float(number)
# Use the functions in math module for calculating the square root, logarithm to base  e and sine of the number in radians. 
square_root=math.sqrt(number_float)
log=math.log(number_float)
sine=math.sin(number_float)
#Print the result in the given format.
print(f"The square of {number} is {square_root}\nThe logarithm of {number} is {log}\nThe sine of {number} is {sine}.")
