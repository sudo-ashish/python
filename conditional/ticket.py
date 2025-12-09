age = int(input("Enter your age here to verify and buy: "))
day = str(input("Enter the day you are buying the tkt: "))

# if day == "wednesday":
#     if age < 18:
#         print("Your ticket price is $6")
#     elif age >= 18:
#         print("Your ticket price is $10")
# else:
#     if age < 18:
#         print("Your ticket price is $8")
#     elif age >= 18:
#         print("Your ticket price is $12")

price = 12 if age >= 18 else 8
if day == "wednesday":
    price = price - 2

print("your ticket price is $", price)
