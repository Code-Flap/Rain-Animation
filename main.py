import pygame
import random


pygame.init()

Width, Height = 800, 600

Size = (Width,Height)
win = pygame.display.set_mode(Size)
pygame.display.set_caption("Rain Animation")

class RainDrop:
    def __init__(self):
        self.x = random.randint(15,Width-15)
        self.y =  random.randint(-1500,-400)
        self.width = random.randint(2,7)
        self.height = random.randint(25,33)
        self.gravity = random.randint(1,3)
        self.rect = (self.x,self.y,self.width,self.height)
    def draw(self):
        self.raindrop = pygame.draw.rect(win,(0,0,190),rect=self.rect)

    def fall(self):
        self.y+=self.gravity
        self.rect = (self.x,self.y,self.width,self.height)

        if self.y > Height:
            self.y =  random.randint(-300,-100)

drops = []
amount = random.randint(50,400)
print(amount)
for i in range(amount):
    drops.append(RainDrop())
run = True
while run:
    win.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for drop in drops:
        drop.draw()
        drop.fall()
    pygame.display.update()
