import pygame
import time
import random

class Player():
    def __init__(self, name, color, vectors):
        self.name = name
        self.color = color
        self.score = 0
        self.reset(False)
        self.vectors = vectors

    def reset(self, win):
        if win:
            self.score += 1
        self.x = random.randint(25, width - 25)
        self.y = random.randint(25, height - 25) 
        self.tail = [(self.x, self.y)]
        self.length = 16 
        self.dx = 0
        self.dy = -1
    
    def trim(self):
        if len(self.tail) <= self.length:
            return
        cut = len(self.tail) - self.length
        for px, py in self.tail[:cut]:
            point(px, py, bg)
        self.tail = self.tail[cut:]
    
    def turn(self, key):
        self.dx, self.dy = self.vectors[key]

    def grow(self, n):
        self.length += n

    def update(self):
        self.x += self.dx
        self.y += self.dy 
        if collision(self, self.x, self.y):
            return False
        self.tail.append((self.x, self.y))
        point(self.x, self.y, self.color)
        self.trim()
        return True

def point(x, y, c):
    win.set_at((x, y), c)
    pygame.display.update(pygame.rect.Rect(x, y, 1, 1))
    return

def coin():
    cx = random.randint(10, width - 10)
    cy = random.randint(10, height - 10)
    point(cx, cy, cg)
    
width = 400 #int(input("Enter width "))
height = 300 #int(input("Enter height "))

vectors = [{
    pygame.K_w: (0, -1),
    pygame.K_s: (0, 1),
    pygame.K_d: (1, 0),
    pygame.K_a: (-1, 0)
    }, {
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1),
    pygame.K_RIGHT: (1, 0),
    pygame.K_LEFT: (-1, 0)
}]

players = []
for i in range(2):
    n = "p{}".format(i) #input("Enter player {} name ".format(i))
    cr = 255 - (i*255) #int(input("Enter player {} red ".format(i)))
    cg = 0 #int(input("Enter player {} green ".format(i)))
    cb = i*255 #int(input("Enter player {} blue ".format(i)))
    players.append(Player(n, pygame.color.Color(cr, cg, cb), vectors[i]))

win = pygame.display.set_mode((width, height))
bg = pygame.color.Color(0,0,0,255)
cg = pygame.color.Color(255,255,255,255)

def init():
    win.fill(pygame.color.Color(255,255,0,255))
    win.fill(bg, rect=pygame.Rect((2, 2, width-4, height-4)))
    pygame.display.flip()


def collision(p, x, y):
    c = win.get_at((x, y))
    if c == cg:
        p.grow(4)
        return False
    if c != bg:
        return True
        

def run():
    init()
    running = True
    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            if event.key in vectors[0].keys():
                players[0].turn(event.key)
            elif event.key in vectors[1].keys():
                players[1].turn(event.key)
    
        if random.randint(1, 20) == 1:
            coin()
        if not players[0].update():
            players[0].reset(False)
            players[1].reset(True)
            init()
        if not players[1].update():
            players[1].reset(False)
            players[0].reset(True)
            init()

run()
