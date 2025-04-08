# logical operator : or , and , not

#  or logical perator

# temp = 20
# is_raining  = True



# if temp > 35 or temp < 0 or is_raining:
#   print("The out door event is canclled")
# else:
#   print("The outdoor event is still scheduled")



# and logical operator

temp = 20
is_sunny = True

if temp >= 28 and is_sunny:
  print("It is hot 🥵")
  print("It is SUNNY ☀️")
elif temp <= 0 and is_sunny:
  print("It is cold outside 🥶")
  print("It is SUNNY ☀️")
elif temp < 28 and temp > 0 and is_sunny:
  print("It is WARM outside 😊 ")
  print("It is SUNNY ☀️")
elif temp >= 28 and is_sunny:
  print("It is hot 🥵")
  print("It is SUNNY ☀️")
elif temp <= 0 and is_sunny:
  print("It is cold outside 🥶")
  print("It is SUNNY ☀️")
elif temp < 28 and temp > 0 and is_sunny:
  print("It is WARM outside 😊 ")
  print("It is SUNNY ☀️")
