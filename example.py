waysToGo = ['l', 'r', 'r', 's']

def checkDirection(step, dir):
    dir = dir.lower()[0]
    if dir == step:
        return True

    print("you died")
    return False

winner = False

while not winner:
    for step in waysToGo:
        dir = input("Which way ")
        if not checkDirection(step, dir):
            break
    winner = True

print("you win!")
