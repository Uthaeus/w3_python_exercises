# Write a Python program to concatenate all elements in a list into a string and return it.

def concat(l):
  result = ''

  for x in l:
    result += str(x)

  return result

li = ['myself', 'you', 'them', 'us', 'they', 1]

print(concat(li))