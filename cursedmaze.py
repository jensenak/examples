import curses
import sys

class InputError(Exception):
    pass


class Dungeon():
    def __init__(self, scr, src, states):
        self.scr = scr
        self.level = src
        self.states = states

    def fate(self, user):
        state = self.level[user.y][user.x]
        self.scr.addstr(0, 0, self.states[state]["words"], curses.color_pair(self.states[state]["color"]))
        if self.states[state]["dead"]:
            self.scr.addstr(user.y, user.x, "X", curses.color_pair(2))
            user.respawn()
        if self.states[state]["win"]:
            self.scr.getkey()
            sys.exit()


class Player():
    def __init__(self, scr, spawn):
        self.scr = scr
        self.px = spawn["x"]
        self.py = spawn["y"]
        self.respawn()

    def respawn(self):
        self.x = self.px
        self.y = self.py

    def move(self, dir):
        self.scr.addstr(self.y, self.x, "#")
        self.px = self.x
        self.py = self.y
        if dir == "KEY_UP":
            self.y -= 1
        if dir == "KEY_DOWN":
            self.y += 1
        if dir == "KEY_RIGHT":
            self.x += 1
        if dir == "KEY_LEFT":
            self.x -= 1


stateMap = [
    {"dead": False, "win": False, "words": "                                                     ", "color":0},
    {"dead": False, "win": True, "words": "You are the winner of the Universe!                  ", "color":3},
    {"dead": True, "win": False, "words": "You just became tasty lunch for a goblin             ", "color":2},
    {"dead": True, "win": False, "words": "Your face melted ... IN A POOL OF LAVA               ", "color":2},
    {"dead": True, "win": False, "words": "You are now a smudge on the bottom of a large boulder", "color":2},
    {"dead": True, "win": False, "words": "You have been dissolved in acid                      ", "color":2},
    {"dead": True, "win": False, "words": "Oh look, you've been impaled                         ", "color":2},
]
# level = [[2,2,2,2,2,2],
#          [3,0,3,2,2,2],
#          [4,0,0,4,2,2],
#          [5,0,5,0,1,2],
#          [6,0,0,0,5,2],
#          [2,6,2,3,4,2]]
level = [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [2,0,2,2,2,2,0,0,0,0,0,0,0,2,2,2],
        [2,0,2,2,2,2,2,2,2,0,2,2,0,2,2,2],
        [2,0,0,0,2,0,0,0,0,0,2,2,0,2,2,2],
        [2,0,2,0,2,0,2,2,0,2,2,2,0,2,2,2],
        [2,0,2,0,2,0,2,2,0,2,2,2,0,2,2,2],
        [2,0,0,0,0,0,2,2,0,2,2,2,0,2,2,2],
        [2,2,2,2,2,2,2,2,0,2,2,2,0,0,2,2],
        [2,2,2,2,2,0,0,0,0,2,2,2,2,0,2,2],
        [2,2,2,2,2,0,0,0,0,0,0,0,0,0,2,2],
        [2,1,0,0,2,0,0,0,0,2,2,0,2,2,2,2],
        [2,2,2,0,2,2,0,2,2,2,2,0,2,2,2,2],
        [2,2,2,0,2,2,0,2,2,2,2,0,2,2,2,2],
        [2,2,0,0,0,0,0,2,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]


def main(scr):
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)
    scr.clear()
    p = Player(scr, {"x": 1, "y": 1})
    d = Dungeon(scr, level, stateMap)

    while True:
        try:
            scr.addstr(p.y, p.x, "*", curses.color_pair(3))
            scr.refresh()
            k = scr.getkey()
            p.move(k)
            d.fate(p)
        except InputError:
            scr.addstr(11, 0, "That's not a valid direction")

curses.wrapper(main)
