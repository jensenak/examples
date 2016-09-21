import sys

class InputError(Exception):
    pass

map = [[0,0,0,0,0,0,0,0,0,0],
       [0,1,1,4,0,0,0,0,0,0],
       [0,3,1,4,3,3,6,5,0,0],
       [0,1,1,3,1,1,1,1,0,0],
       [0,1,6,5,1,5,6,1,0,0],
       [0,1,1,1,1,6,6,1,4,0],
       [0,6,6,3,4,0,4,1,1,0],
       [0,0,0,0,0,0,0,5,1,0],
       [0,0,0,0,0,0,2,1,1,0],
       [0,0,0,0,0,0,0,0,0,0]]

location = {"x": 1, "y": 1}
def parseInput(s):
    if len(s) == 0:
        raise InputError()
    s = s.lower()[0]
    if s in ['n','s','e','w']:
        return s
    if s == "q":
        sys.exit()
    raise InputError()

def move(dir):
    if dir == "n":
        location["y"] -= 1
    if dir == "s":
        location["y"] += 1
    if dir == "e":
        location["x"] += 1
    if dir == "w":
        location["x"] -= 1
    return test()

def test():
    return map[location["y"]][location["x"]]

def fate(state):
    if state == 1:
        print("Still alive... keep going.")
        return False # still in maze
    if state == 0:
        print("You fell in a really big hole!")
    if state == 2:
        print("You are the winner of the universe!")
    if state == 3:
        print("You just became tasty lunch for a goblin")
    if state == 4:
        print("Your face melted ... IN A POOL OF LAVA")
    if state == 5:
        print("You are now a smudge on the bottom of a large boulder")
    if state == 6:
        print("You have been dissolved in acid")

while True:
    try:
        dir = parseInput(input("North, South, East, or West?"))
        state = move(dir)
        if fate(state):
            location["x"] = 1
            location["y"] = 1
            print()
            break
    except InputError:
        print("That's not a valid direction")

input("Press Enter to continue")
