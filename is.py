# Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged

def eval(s):
  test = s[:2]
  if test == 'Is':
    result = s 
  else:
    result = 'Is ' + s 

  return result

string = input("Enter a sentence:\n")

print(eval(string))
