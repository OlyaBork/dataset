import os
import os.path


answer = os.path.exists("C:\\")

print(answer)


answer = os.path.isfile("numbers.txt")
print(answer)

answer = os.path.isdir("numbers.txt")
print(answer)

file = open("data/names.txt")

data_in_file = file.read()
print(data_in_file)

lines = file.readlines()
print(lines)

file.close()