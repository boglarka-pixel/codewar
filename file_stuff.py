import os
import readline

test_file = open("test.txt", "wb")

print(test_file.mode) # wb

print(test_file.name) # test.txt

test_file.write(bytes("write me to the file", 'UTF-8'))

test_file.close()

test_file = open("test.txt", "r+")

text_in_file = test_file.read()
print(text_in_file)

# os.remove("test.txt") /törli a file-t


file = open("filename.txt", "wb")

file.write(bytes('this is a \n more lines \n file', 'UTF-8'))

# print(file.readlines()) # nem működik

file.close()


# best practice

try:
   f = open("filename.txt")

   print(f.read())

finally:
   f.close()


# An alternative way of doing this is using with statements. This creates a temporary variable (often called f), which is only accessible in the indented block of the with statement.
# with open("filename.txt") as f:

#    print(f.read())
# PY
# The file is automatically closed at the end of the with statement, even if exceptions occur within it.