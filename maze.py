class InvalidDirection(Exception):
    pass

def parseDirection(s):
    s = s.lower()
    if s == "l":
        return s
    if s == "left":
        return "l" 
    if s == "r":
        return s 
    if s == "right":
        return "r"
    if s == "s":
        return s
    if s == "straight":
        return "s"
    raise InvalidDirection("Expected l[eft], r[ight], or s[traight]. Got {}".format(s))

print("Left, right or straight")
try:
    choice = parseDirection(input())
    
    if choice == "l":
        print("You fell in a hole")
    
    if choice == "r":
        print("You got eaten by a monster")
    
    if choice == "s":
        print("You win!")

except InvalidDirection as e:
    print(e)
