
#Taking user input and writing it to a file named Output.txt
Data=input("Enter text to write to the file : ")
#writing a file with input text in w mode.
with open('output.txt','w') as fh:
    fh.write(Data)
print("Data successfully written to the output.txt file.")
#taking additional data as input and appending the same to text file.
Data1=input("Enter additional text to append: ")
with open('output.txt','a') as fh:
    fh.write("\n" + Data1)
print("Data successfully appended. ")
#opening the file in read mode and using readlines function printing the output of the file line by line.
with open('output.txt','r') as fh:
    Data3=fh.readlines()
print("Final content of the output.txt")
for line in Data3:
    print(line.strip())