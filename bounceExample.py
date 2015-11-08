import pygame
 
pygame.init()
 
window = pygame.display.set_mode((900,650))
 
pygame.display.set_caption("Collision Detection")
 
grey = (32,32,32)
green = (0,250,154)
purple = (138,43,226)

clock = pygame.time.Clock()
 
def detectCollisions(x11, y11, x12, y12, w1, x21, y21, x22, y22, w2):
 
    # if (x2+w2>=x1>=x2 and y2+h2>=y1>=y2):
    #     return True
    #
    # elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1>=y2):
    #     return True
    #
    # elif (x2+w2>=x1>=x2 and y2+h2>=y1+h1>=y2):
    #     return True
    #
    # elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1+h1>=y2):
    #     return True
 
    # else:
        return False
 
class Sprite:
 
    def __init__(self, x1, y1, x2, y2, width):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.width=width
 
    def render(self,collision):
        if (collision==True):
            pygame.draw.line(window, purple, [self.x1, self.y1], [self.x2,self.y2], self.width)

        else:
            pygame.draw.line(window, purple, [self.x1, self.y1], [self.x2,self.y2], self.width)
 
north=Sprite(350, 45, 200, 305, 20)
nEast=Sprite(800, 305, 650, 565, 20)
sEast=Sprite(650, 45, 800, 305, 20)
south=Sprite(350, 45, 650, 45, 20)
sWest=Sprite(350, 565, 650, 565, 20)
nWest=Sprite(200, 305, 350, 565, 20)

bouncy = Sprite(500, 535, 505, 535, 5)
 
moveX,moveY=0,0
 
gameLoop=True
while gameLoop:
 
    for event in pygame.event.get():
 
        if (event.type==pygame.QUIT):
            gameLoop=False
 
        if (event.type==pygame.KEYDOWN):
            if (event.key==pygame.K_LEFT):
                moveX = -4
 
            if (event.key==pygame.K_RIGHT):
                moveX = 4
 
            if (event.key==pygame.K_UP):
                moveY = -4
 
            if (event.key==pygame.K_DOWN):
                moveY = 4
 
        if (event.type==pygame.KEYUP):
 
            if (event.key==pygame.K_LEFT):
                moveX=0
 
            if (event.key==pygame.K_RIGHT):
                moveX=0

            if (event.key==pygame.K_UP):
                moveY=0
 
            if (event.key==pygame.K_DOWN):
                moveY=0
 
    window.fill(grey)
 
    north.x1+=moveX
    north.y1+=moveY
 
    collisions=detectCollisions(north.x1, north.y1, north.x2, north.y2, north.width, nEast.x1, nEast.y1, nEast.x2, nEast.y2, nEast.width)

    north.render(collisions)
    nEast.render(False)
    sEast.render(False)
    south.render(False)
    sWest.render(False)
    nWest.render(False)
    bouncy.render(False)
 
    pygame.display.flip()
 
    clock.tick(50)
 
pygame.quit()