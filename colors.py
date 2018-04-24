# Write a Python program to display the first and last colors from the following list.

color_list = ["Red","Green","White" ,"Black"]

first, *second, last = color_list

print(first, last)

print("%s %s"%(color_list[0], color_list[-1]))