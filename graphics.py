import pygame
import time

vectors = {
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1),
    pygame.K_RIGHT: (1, 0),
    pygame.K_LEFT: (-1, 0)
}

win = pygame.display.set_mode((200,200))

bg = pygame.color.Color(0,0,0)
fg = pygame.color.Color(255,0,0)
x = 10
y = 10

win.fill(bg)
win.set_at((x, y), fg)
pygame.display.flip()

class player():
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.tail = [(x,y)]
        self.length = 16 
        self.dir = (0, 1)
    
    def turn(self, key):
        self.dir = vectors[key]

    def trim(self):
        if len(self.tail) <= self.length:
            return
        cut = len(self.tail) - self.length
        for px, py in self.tail[:cut]:
            win.set_at((px, py), bg)
        self.tail = self.tail[cut:]
    
    def grow(self, n):
        self.length += n

    def update(self):
        dx, dy = self.dir
        self.x += dx
        self.y += dy 
        self.tail.append((self.x, self.y))
        win.set_at((self.x, self.y), fg)
        self.trim()

p = player("bob", 10, 10)
ticker = lambda: int(round(time.time() * 1000))
delay = 50
timer = ticker() + delay
print(timer)
running = True
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYUP:
        p.turn(event.key) 
    if timer < ticker():
        timer = ticker() + delay 
        p.update()
        pygame.display.flip() 
