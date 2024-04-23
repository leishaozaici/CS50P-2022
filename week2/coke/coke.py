amount = 50
while amount > 0:
    print(f"Amount Due: {amount}")
    coin = input("Insert Coin: ")
    if coin in ["5", "10", "25"]:
        amount -= int(coin)

print(f"Change Owed: {abs(amount)}")
