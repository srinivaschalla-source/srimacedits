# This is a programme for calculating and printing Factorial of a number which is taken as an input by using the Recursion method.
#Define a function using recursion for finding the factorial of any number
def factorial_recursive(num):
    res=1
    if num>1:
        return num*factorial_recursive(num-1)
    else:
        return 1
#Take the input as any number, convert it to integer and if it is not zero or negative calculate factorial and print it else convey message.
n=int(input("Enter a numer : "))
if n>1:
    x=factorial_recursive(n)
    print(f"The factorial of {n} is: {x}")
else:
    print("There cannot be factorial for negative numbers or ZERO")
