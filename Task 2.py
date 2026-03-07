#This program is for creating a list with numbers 1 to 10 as elements. Extract first five elements and then reverse the extracted elements and print both the extracted list and reversed list.
#step 1: creating a list with 10 numbers and printing it
numbers=[1,2,3,4,5,6,7,8,9,10]
print(f"Original list: {numbers}")
#step2: extracting the first 5 elements of the list into a seperate list and printing the same.
extracted_list=numbers[0:5]
print(f"extracted first five elements: {extracted_list}")
#step 3: Reversing the extracted list using reverse function and printing the same list.
reversed_list=extracted_list.reverse()
print(f"Reversed extracted elements: {extracted_list}")