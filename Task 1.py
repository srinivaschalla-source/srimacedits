#Programme for taking input of an integer and finding and printing whether  it is even or odd number in the given format.
# step 1 Taking input of an integer in a variable x---Takes an integer input from the user.
x=int(input("Enter an integer: "))
# step 2 -Checks whether the number is even or odd using an if-else statement.Conditional verification using MOD operator if the entered value is divisible by 2 or not and if remainder is 0, printing it as even number else as odd number
if x%2==0:
# step 3---Displays the result accordingly.
    print(f"{x} is an Even number")
else:
    print(f"{x} is an Odd number")
