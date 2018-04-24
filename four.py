# Write a Python program to count the number 4 in a given list.

def four(l):
  count = 0

  for x in l:
    if int(x) == 4:
      count += 1

  if count > 0:
    result = "The number 4 was counted " + str(count) + " times."
  else:
    result = "There are no 4's in your list."

  return result

user_list = input("Enter some numbers:\n").split(',')


print(four(user_list))
