import pgzrun, random

TITLE="Shooting Star"
WIDTH=370
HEIGHT=370

star=Actor("star")
star.pos=300,200
score=0

def draw():
    global score
    screen.fill("lightblue")
    star.draw()
    screen.draw.text("Score:"+str(score), center=(300,100), fontsize=30, color="white")


def on_mouse_down(pos):
    global score
    if star.collidepoint(pos):
        placestar()
        score+=1

def placestar():
    star.x=random.randint(50,350)
    star.y=random.randint(50,350)


pgzrun.go()