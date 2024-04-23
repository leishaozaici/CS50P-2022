import random

while True:
    try:
        n = int(input("Level: "))
        t = random.randint(1,n)
    except ValueError:
        pass
    else:
        break

while True:
    try:
        temp = int(input("Guess: "))
        if temp <= 0:
            continue
        if temp > t:
            print("Too large!")
            continue
        if temp < t:
            print("Too small!")
            continue
        else:
            print("Just right!")
            break
    except ValueError:
        pass


