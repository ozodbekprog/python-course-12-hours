# Shopping card progaram



foods = []
prices = []
total = 0

while True:
   food = input("Enter a food to but (q, Q to quit): ")
   if food.lower() == "q":
      print("Thank you for shopping")
      break
   else:
      price = float(input(f"Enter the price of {food}: "))
      foods.append(food)
      prices.append(price)
print("----- Shopping Card -----")
for x in foods:
   print(x, end=" ")
for n in prices:
   total += n

print()
print(f"Your total is ${total} ")