# temperature  converter program
#  my second projact
unit =  input(" Is this temparature in Calsius or Feranheit (C/F) ")
if unit == "C" or unit == "F":
  temp = float(input("Enter the temperature:  "))
  if unit == "C":
    temp = round((9 * temp) / 5 + 32)
    print(f" The tmeperature in Feranheit is {temp}°F ")
  elif unit == "F":
    temp = round((temp - 32 ) * 5 / 9)
    print(f" The tmeperature in Calsius is {temp}°C ")
else:
  print(f"{unit} is an invild unint of Mesesurement")
