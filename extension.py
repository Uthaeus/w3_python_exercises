# Write a Python program to accept a filename from the user and print the extension of that.

# print("Welcome")
# file_name = input("Enter your filename: ")

# first, _, ext = file_name.partition('.')

# print(ext)

name = input("Enter the filename: ")
file = name.split(".")

print("The extension of the file is: ", file[-1])