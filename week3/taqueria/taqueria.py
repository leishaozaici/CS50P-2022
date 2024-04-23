menu = {
    key.lower(): value
    for key, value in {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00,
    }.items()
}
ans = 0
while True:
    try:
        item = input("Item: ").lower()
        if item in menu:
            ans += menu[item]
            print(f"Total: ${ans:.2f}")
    except EOFError:
        break
