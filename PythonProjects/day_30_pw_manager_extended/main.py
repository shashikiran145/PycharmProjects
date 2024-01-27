# # Types of error catching codes
# try:
#     file = open("a.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a.txt", "w")
#     file.write("Hello")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")


height = float(input("Enter your height"))
weight = int(input("Enter your weight"))

if height > 3:
    raise ValueError("Human height should not exceed 3 meters")

bmi = weight / height ** 2

print(bmi)


# password manager code is modified in the original file. Refer that
