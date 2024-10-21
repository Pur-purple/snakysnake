import turtle, random, time

#config
gametime = 0
preffps = 12
step = 50
maxapples = 2
score = 1

fullsnake = []
allapples = []

ahandler = turtle.Turtle()
thandler = turtle.Turtle()
shandler = turtle.Turtle()

turtle.tracer(0)

ahandler.shape("circle")
ahandler.color("red")
ahandler.shapesize(2)
ahandler.pu()
ahandler.ht()

thandler.shape("square")
thandler.color("green")
thandler.shapesize(2)
thandler.pu()
thandler.ht()

shandler.shape("turtle")
shandler.color("black")
shandler.shapesize(2)
shandler.pu()
shandler.ht()

class Snake:
    def __init__(self, x, y, rot):
        self.x = x
        self.y = y
        self.rot = rot
    def goup(self):
        self.y += step
    def godown(self):
        self.y -= step
    def goright(self):
        self.x += step
    def goleft(self):
        self.x -= step

class Apple:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def render():
    global fullsnake
    global gametime
    global score               
    #adding everything
    if len(allapples) < maxapples:
        allapples.append(Apple(random.randrange(-450, 450, step), random.randrange(-350, 350, step)))
    try:        
        if len(fullsnake) < score:
            if i.rot == "up":
                fullsnake.append(Snake(fullsnake[-1].x, fullsnake[-1].y - step, fullsnake[-1].rot))
            if i.rot == "down":
                fullsnake.append(Snake(fullsnake[-1].x, fullsnake[-1].y + step, fullsnake[-1].rot))
            if i.rot == "right":
                fullsnake.append(Snake(fullsnake[-1].x - step, fullsnake[-1].y, fullsnake[-1].rot))
            if i.rot == "left":
                fullsnake.append(Snake(fullsnake[-1].x + step, fullsnake[-1].y, fullsnake[-1].rot))
    except:
        fullsnake.append(Snake(0, 0, "up"))
    for i in reversed(range(1, len(fullsnake))):
        fullsnake[i].x = fullsnake[i-1].x
        fullsnake[i].y = fullsnake[i-1].y
    #eating mech
    for i in allapples:
        if i.x == fullsnake[0].x and i.y == fullsnake[0].y:
            allapples.pop(allapples.index(i))
            score += 1          
    #controlls
    if fullsnake[0].rot == "up":
        fullsnake[0].goup()
    if fullsnake[0].rot == "down":
        fullsnake[0].godown()
    if fullsnake[0].rot == "right":
        fullsnake[0].goright()
    if fullsnake[0].rot == "left":
        fullsnake[0].goleft()
    #checking for death
    if fullsnake[0].x > 450 or fullsnake[0].x < -450 or fullsnake[0].y > 400 or fullsnake[0].y < -400:
        turtle.bye()
    for i in reversed(range(1, len(fullsnake))):
        if fullsnake[0].x == fullsnake[i].x and fullsnake[0].y == fullsnake[i].y:
            turtle.bye()
    gametime += 1

def update():
    thandler.clearstamps()
    ahandler.clearstamps()
    shandler.clear()
    for i in allapples:
        ahandler.goto(i.x, i.y)
        ahandler.stamp()
    for i in fullsnake:
        thandler.goto(i.x, i.y)
        thandler.stamp()
    shandler.goto(-450, 350)
    shandler.write(score, "right", font=("Arial", 30))
    turtle.update()

#controlls
def u():
    if fullsnake[0].rot != "down":
        fullsnake[0].rot = "up"
def d():
    if fullsnake[0].rot != "up":
        fullsnake[0].rot = "down"
def r():
    if fullsnake[0].rot != "left":
        fullsnake[0].rot = "right"
def l():
    if fullsnake[0].rot != "right":
        fullsnake[0].rot = "left"

turtle.onkey(u, "Up")
turtle.onkey(d, "Down")
turtle.onkey(r, "Right")
turtle.onkey(l, "Left")
turtle.listen()

while True:
    render()
    update()
    time.sleep(1/preffps)
