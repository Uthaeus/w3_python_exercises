# Write a Python program to check whether a specified value is contained in a group of values

def included(l, n):
  return n in l

nums = [1, 2, 3, 4, 5]

num = int(input("Enter a number: "))

print(included(nums, num))