# Write a Python program to create a histogram from a given list of integers.

def histrogram(l):

  for x in l:
    output = '*' * x

    print(output)

u_list = [2, 3, 6, 0, 1]

histrogram(u_list)