# python compound interset calculator


# princile = 0
# rate = 0
# time = 0

# while True:
#   princile = float(input("Enter the princple amount: "))
#   if princile < 0:
#     print("principle can't be less than or ecual to 0")
#   else:
#     break
# while rate <= 0:
#   rate = float(input("Enter the Interest rate: "))
#   if rate < 0:
#     print("interest rete can't be less than or ecual to 0")
# while time < 0:
#   time = float(input("Enter the time in year: "))
#   if time < 0:
#     print("time can't be less than or ecual to 0")


# print(f"principle is {time}")
# print(f"principle is {princile}")
# print(f"rate is {rate}")



# total =  princile * pow((1 + rate / 100), time)
# print(f"Balance after {time} yeard/s: ${total:.2f}")



principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Boshlang‘ich pul miqdorini kiriting: "))
    if principle < 0:
        print("Boshlang‘ich pul 0 dan kichik bo‘lishi mumkin emas")
    else:
        break

while True:
    rate = float(input("Foiz stavkasini kiriting: "))
    if rate < 0:
        print("Foiz stavkasi 0 dan kichik bo‘lishi mumkin emas")
    else:
        break

while True:
    time = float(input("Vaqtni (yilda) kiriting: "))
    if time < 0:
        print("Vaqt 0 dan kichik bo‘lishi mumkin emas")
    else:
        break

print(f"Boshlang‘ich pul: {principle}")
print(f"Foiz stavkasi: {rate}")
print(f"Vaqt: {time}")

total = principle * pow((1 + rate / 100), time)
print(f"{time} yildan keyin jami balans: ${total:.2f}")