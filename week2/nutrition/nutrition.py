fruit = {"Apple":130,"Avocado":50,"banana":110,"Cantaloupe":50,"Grapefruit":60,
         "Honeydew":50,"Kiwifruit":90,"Lemon":15,"Lime":20,"Nectarine":60,"Orange":80,"Peach":60,
         "Pear":100,"Pineapple":50,"Plums":70,"Strawberries":50,"Sweet Cherries":100}
s = input("Item: ")
if s in fruit:
    print(fruit[s])
elif s.capitalize() in fruit:
    print(fruit[s.capitalize()])
