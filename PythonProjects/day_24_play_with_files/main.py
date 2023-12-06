# Open and read a file - 1

# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()


# Open and read a file - 2

with open("../../../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

# Write something into a file
# "w" - write ; "a" - append

# with open("my_file.txt", mode="a") as file:
#     file.write("\nHello again")
#     print(file.read())

