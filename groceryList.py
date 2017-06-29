groceryList = ["wheat bread", "ham", "avacado"]
keepShopping = True
def addGrocery():
    print("What would you like to add to your grocery list?")
    grocery1 = input()
    groceryList.append(grocery1)
    print("Here is your grocery list.")
    
for x in groceryList:
    print(x)
while keepShopping == True:
    addGrocery()
    print("Anything else? (yes/no)")
    answer = input()
    if answer == ("yes"):
        keepShopping = True
    if answer == ("no"):
        keepShopping = False

if keepShopping == False:
    print("Okay! Here's your completed grocery list!.")
    for x in groceryList:
        print(x)
    exit()

