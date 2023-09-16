my_list = ['alex', 'freddy', 'sofia', 'alexandra', 'angalena']

new_list = [name.upper() for name in my_list if len(name) > 4]

print(new_list)

# with open("file1.txt") as file1:
#     file1_nums = [int(num.strip()) for num in file1.readlines()]
# with open("file2.txt") as file2:
#     file2_nums = [int(num.strip()) for num in file2.readlines()]
#
# result = [num for num in file1_nums if num in file2_nums]
#
# # Write your code above 👆
#
# print(result)


