
menu= ["espresso", "mocha", "latte", "cappuccino", "cortado", "americano" ]

def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee

map_coffee = map( find_coffee, menu )
print(map_coffee)

for x in map_coffee:
    print(x)



