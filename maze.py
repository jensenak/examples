import sys

class InputError(Exception):
    pass

stateMap = [
    {"dead": False, "win": False, "words": "Keep going"},
    {"dead": False, "win": True, "words": "You are the winner of the Universe!"},
    {"dead": True, "win": False, "words": "You just became tasty lunch for a goblin"},
    {"dead": True, "win": False, "words": "Your face melted ... IN A POOL OF LAVA"},
    {"dead": True, "win": False, "words": "You are now a smudge on the bottom of a large boulder"},
    {"dead": True, "win": False, "words": "You have been dissolved in acid"},
    {"dead": True, "win": False, "words": "Oh look, you've been impaled"},
]

level = [[2,2,2,2,2,2],
         [3,0,3,2,2,2],
         [4,0,0,4,2,2],
         [5,0,5,0,1,2],
         [6,0,0,0,5,2],
         [2,6,2,3,4,2]]

location = {"x": 1, "y": 1}

def getFirstCharacter(s):
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
    return level[location["y"]][location["x"]]

while True:
    try:
        dir = parseInput(input("North, South, East, or West (q to quit)? "))
        state = move(dir)
        print(stateMap[state]["words"])
        if stateMap[state]["dead"]:
            location['x'] = 1
            location['y'] = 1
            print("------- start over -------")
            continue
        if stateMap[state]["win"]:
            break
    except InputError:
        print("That's not a valid direction")

input("Press Enter to continue")
