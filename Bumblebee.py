import pgzrun, random
WIDTH=500
HEIGHT=400
TITLE="BEE COLLECTOR"
score=0
bee=Actor("bee")
bee.x=200
bee.y=100
flower=Actor("flower")
flower.x=random.randint(70,WIDTH-70)
flower.y=random.randint(70,HEIGHT-70)
def draw():
    screen.clear()
    screen.blit("background",(0,0))
    flower.draw()
    bee.draw()

def update():
    if keyboard.left:
        bee.x = bee.x-2
        if bee.x < 0:
            bee.x=10   
    if keyboard.right:
        bee.x = bee.x+2
        if bee.x > WIDTH:
            bee.x=10
    if keyboard.up:
        bee.y -= 2
        if bee.y < 0:
            bee.y = 10
    if keyboard.down:
        bee.y = bee.y+2
        if bee.y > HEIGHT:
            bee.y = 10 
    


pgzrun.go()