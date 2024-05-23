# calculate_discount.py

# Prices of the shirts
shirt1 = 423
shirt2 = 320
shirt3 = 270
shirt4 = 680
shirt5 = 520

# Calculating the discounts
d1 = shirt1 * 15 / 100
d2 = shirt2 * 15 / 100
d3 = shirt3 * 15 / 100
d4 = shirt4 * 15 / 100
d5 = shirt5 * 15 / 100

# Calculating the prices after discount
dp1 = shirt1 - d1
dp2 = shirt2 - d2
dp3 = shirt3 - d3
dp4 = shirt4 - d4
dp5 = shirt5 - d5

print("ITEMS AND DISCOUNTED PRICE OF THEM\n")
print(f"Original price of shirt 1 is {shirt1:.0f}")
print(f"Discount is {d1:.2f}")
print(f"Price after discount is {dp1:.2f}\n")

print(f"Original price of shirt 2 is {shirt2:.0f}")
print(f"Discount is {d2:.2f}")
print(f"Price after discount is {dp2:.2f}\n")

print(f"Original price of shirt 3 is {shirt3:.0f}")
print(f"Discount is {d3:.2f}")
print(f"Price after discount is {dp3:.2f}\n")

print(f"Original price of shirt 4 is {shirt4:.0f}")
print(f"Discount is {d4:.2f}")
print(f"Price after discount is {dp4:.2f}\n")

print(f"Original price of shirt 5 is {shirt5:.0f}")
print(f"Discount is {d5:.2f}")
print(f"Price after discount is {dp5:.2f}\n")

# Calculating the totals
op = shirt1 + shirt2 + shirt3 + shirt4 + shirt5
d = d1 + d2 + d3 + d4 + d5
dp = dp1 + dp2 + dp3 + dp4 + dp5

print("YOUR BILL:\n")
print(f"TOTAL BILL: {op:.0f}")
print(f"DISCOUNT: {d:.2f}")
print(f"PRICE AFTER DISCOUNT: {dp:.2f}\n")

# Payment prompt
p = input("PAY (Y or N): ")
if p.lower() == 'y':
    print("PAYMENT HAS BEEN SUCCESSFUL\nTHANKS FOR SHOPPING!")
else:
    print("PAYMENT DID NOT SUCCEED")
