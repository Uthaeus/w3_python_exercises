# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

values = input("Enter some numbers(don't forget to separate with commas)\n")
user_list = values.split(',')
user_tuple = tuple(user_list)

print("Your numbers as a list:")
print(user_list)
print('Your numbers as a tuple:')
print(user_tuple)