amount = 0

while amount < 50:
    coin = int(input("Insert Coin: "))
    if coin in (25, 10, 5):
        amount += coin
    if amount < 50:
        print(f"Amount Due: {50 - amount}")

print(f"Change Owed: {amount - 50}")