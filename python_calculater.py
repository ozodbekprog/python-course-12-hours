#  python calculater
#  my first projact in python

operator = input("Enter an Opaerator (+ - * /):")
if operator == "*" or operator == "/" or operator == "+" or operator == "-":
  num1 =  float(input("Enter  the 1st number: "))
  num2 =  float(input("Enter  the 2nd number: "))
  if operator == "+":
    result = num1 + num2
  elif operator == "/":
    result = num1 / num2
  elif  operator == "-":
    result = num1 - num2
  elif operator == "*":
    result = num1 * num2
  print(f"your answer {num1} {operator} {abs(num2)} = {round(result, 3)}  >>>{result}<<<")
else:
  print(f"{operator} is not a vaild operator")
