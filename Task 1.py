"""
# This block is for creating a file named sampl.txt and writing two lines into it in write mode"
#creating a file named sample.txt in w mode for creating a text file
with open('sample.txt', 'w') as file_handler:
#writing 2 lines into the text file
    file_handler.write("This is a sample text file \n") 
    file_handler.write("It contains multiple lines")
"""
# using infinite loop function to open file in read mode and print lines one by one if file exists
file_name="sample.txt"
line_count = 0
with open('sample.txt', 'r') as f:
    for line in f:
        line_count += 1
while True:
    try:
        with open('sample.txt','r') as file_handler:
            for i in range(line_count):
                content=file_handler.readline()
                print(content)
        break
 # exception block for handling error       
    except FileNotFoundError:
        print(f"The file {file_name} was not found")
        break
