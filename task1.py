#Programme for taking input of an integer and finding and printing whether  it is even or odd number in the given format.
#Taking input of an integer in a variable x
x=int(input("Enter an integer: "))
# conditional verification using MOD operator if the entered value is divisible by 2 or not and if remainder is 0, printing it as even number else as odd number
if x%2==0:
    print(f"{x} is an Even number")
else:
    print(f"{x} is an Odd number")
