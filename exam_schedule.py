# Write a Python program to display the examination schedule. (extract the date from exam_st_date)

exam_st_date = (11, 12, 2014)

d, m, y = exam_st_date

result = f"The examination will start from : {d}/{m}/{y}"

result_two = "The examination will start from : %i/%i/%i"%exam_st_date

print(result)
print(result_two)

