# topic : validatee user input exercise\


username = input("Enter a username : ")


if len(username) > 12:
  print("Your user name can't be mor tha 12 characters")
elif not username.find(" ") == -1:
  print("Your user name can't contain spaces")
elif not username.isalpha():
  print("Your username can't contain numbers")
else:
  print(f'Welcome {username}')