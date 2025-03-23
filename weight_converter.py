#  weight converter

weight = float(input("Enter your weight"))
unit = input("Kilograms  or Pounds (K/L): ")
if unit == "K" or unit == " L":
  if unit == "K":
    weight *= 2.205
    unit = "Lbs."
  elif unit == "L":
    weight /= 2.205
    unit = "Kgs."
  print(f"Your weight is : {round(weight, 3)} {unit} ")
else:
  print(f"{unit} was not valied ")