def findslope():
    slopeon = True
    while slopeon == True:
        print("")
        reset = input("Press enter to start the slope calculator ").lower()
        if reset == "end":
            nothingloop()
            slopeon = False
        print("")
        try:
            x1 = int(input("Enter in the x1 "))
            y1 = int(input("Enter in the y1 "))
            print("(" + str(x1) + "," + str(y1) + ")")
            x2 = int(input("Enter in the x2 "))
            y2 = int(input("Enter in the y2 "))
            print("(" + str(x1) + "," + str(y1) + ")")
            print("")
            toppart = y2 - y1
            bottompart = x2 - x1
            print("slope is " + str(toppart) + " over " + str(bottompart))
        except ValueError:
            print("")
            print("That is not an integer start again")
            findslope()
        
def nothingloop():
    print("Welcome to the calculator menu please select from [calculator] [binary] [slope]")
    nothing = True
    while nothing == True:
         testforslope = input("").lower()
         if testforslope == "slope":
             findslope()
             nothing = False
         elif testforslope == "binary":
             dectobin()
             nothing = False
         elif testforslope == "calculator":
             wcloop()
def dectobin():
    dectobinactivated = True
    while dectobinactivated == True:
        askstartofbin = input("Press enter to start dec to bin ")
        if askstartofbin == "end":
            nothingloop()
            dectobinactivated = False
        print("")
        try: 
            askdec = int(input("Hello please put in number you would like converted to binary "))
            printbin = print(bin(askdec)[2:])
        except ValueError:
            print("That is not a integer")
def wcloop():
    loop = True
    while loop == True:
        print("")
        askstart = input("Hello would you like to use this calculator ").lower()
        if askstart == "yes":
            calculator()
            loop == False
        elif askstart == "no":
            print("")
            print("Well why would you not want to, Ill ask you again")
            wcloop()
        elif askstart == "end":
            nothingloop()
            loop = False
        else:
            print("")
            print("That is not a awnser")
            wcloop()
def calculator():
    ask = input("do you want to times(*) divide(/) add(+) or subtract(-) please use symbol next to the one u want ")
    if ask == "*":
        try: number1 = int(input("First number: "))
        except ValueError:
            print("thats not a number")
            calculator()
        try: number2 = int(input("Second Number: "))
        except ValueError:
            print("thats not a number")
            calculator()
    elif ask == "/":
        try: number1 = int(input("First number: "))
        except ValueError:
            print("thats not a number")
            calculator()
        try: number2 = int(input("Second Number"))
        except ValueError:
            print("thats not a number")
            calculator()
    elif ask == "+":
        try: number1 = int(input("First number: "))
        except ValueError:
            print("thats not a number")
            calculator()
        try: number2 = int(input("Second Number"))
        except ValueError:
            print("thats not a number")
            calculator()
    elif ask == "-":
        try: number1 = int(input("First number: "))
        except ValueError:
            print("thats not a number")
            calculator()
        try: number2 = int(input("Second Number"))
        except ValueError:
            print("thats not a number")
            calculator()
    elif ask == "end":
        nothingloop()
    else:
        print("Not a valid symbol")
        calculator()
    if("*" in ask):
        print(number1, ask, number2, "=", number1 * number2)
    elif("/" in ask):
        print(number1, ask, number2, "=", number1 / number2)
    elif("+" in ask):
        print(number1, ask, number2, "=", number1 + number2)
    elif("-" in ask):
        print(number1, ask, number2, "=", number1 - number2)
    else:
        print("not a valid function")
        wcloop()

#end of functions
nothingloop()
