a_file = open("file_name.txt")

number_of_lines = 3

for i in range(number_of_lines):

    line = a_file.readline()
    print(line)