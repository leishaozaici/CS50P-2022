s = input("Greeting: ").lower()
if "hello" in s:
    print("$0")
elif s.startswith("h"):
    print("$20")
else:
    print("$100")
