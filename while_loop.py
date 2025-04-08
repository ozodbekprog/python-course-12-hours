# whili loop lesson
# name = input("Enter a name: ")
# while name == "" or name == " ":
#     print("You didn't enter a name")
#     name = input("Enter a name: ")

# print(f"hello {name}")



# input age
# age = int(input("Enter your age :"))

# while age < 0 :
#   print("Age can't be negative")
#   age = int(input("Enter your age :"))

# print(f"Your age is {age}")


# food = input("Enter a food you like (q  to quit ): ")
# while not food == "q":
#   print(f"You like {food}")
#   food = input("Enter a food you like (q  to quit ): ")
# print("Goodbye")


num = int(input( "Enter a number between 1 - 10:"))
while num < 1 or num > 10:
    print("{num} is not vaild")
    num = int(input( "Enter a number between 1 - 10:"))
print(f"your namber is {num}")