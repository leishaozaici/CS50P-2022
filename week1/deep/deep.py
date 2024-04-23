s = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything? "
).lower()
print("Yes" if "42" in s or ("forty" in s and "two" in s) else "No")
