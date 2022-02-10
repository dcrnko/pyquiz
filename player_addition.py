from sleep_function import *
pActual = 1
pIndex = 0
while True:
    try:
        pTotal = int(input("Please enter the number of players: "))
    except ValueError:
        print("Wrong input type, please use numbers only!")
        print("\n")
        continue
    else:
        break
pList = []
def player_addition_func():
    global pActual
    global pIndex
    global pList
    global pTotal
    print("\n")
    while pIndex < pTotal:
        convertedpIndex = str(pIndex)
        convertedpActual = str(pActual)
        pIndex = pIndex+1 
        pName = input(str("Please enter the name of player number "+ convertedpActual + ": " ))
        print("\n")
        pList.append(pName)
        print(pName + " registered.")
        print("\n")
        pActual = pActual+1
        print("\n")
    print("Total number of registered players: " + convertedpActual)    
    print("Here is the list of registered players: ")
    for i in range(len(pList)):
        print("- " + pList[i])
    twosecfunc()
    
