#from curses import wrapper
import sys

class InputError(Exception):
    pass


class Dungeon():
    def __init__(self, src, states):
        self.level = src
        self.states = states

    def fate(self, user):
        state = self.level[user.y][user.x]
        print(self.states[state]["words"])
        if self.states[state]["dead"]:
            user.respawn()
        if self.states[state]["win"]:
            sys.exit()


class Player():
    def __init__(self, name, spawn):
        self.name = name
        self.spawn = spawn
        self.respawn()

    def respawn(self):
        print()
        self.x = self.spawn['x']
        self.y = self.spawn['y']

    def move(self, dir):
        if dir == "n":
            self.y -= 1
        if dir == "s":
            self.y += 1
        if dir == "e":
            self.x += 1
        if dir == "w":
            self.x -= 1


def parseInput(s):
    if len(s) == 0:
        raise InputError()
    s = s.lower()[0]
    if s in ['n','s','e','w']:
        return s
    if s == "q":
        sys.exit()
    raise InputError()

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

def main():
    p = Player(input("What is your name? "), {"x": 1, "y": 1})
    d = Dungeon(level, stateMap)

    while True:
        try:
            dir = parseInput(input("North, South, East, or West (q to quit)? "))
            p.move(dir)
            d.fate(p)
        except InputError:
            print("That's not a valid direction")

main()
