import turtle, random, time, math

turtle.title("Snakysnake")
turtle.tracer(0)


#config

#gameplay config
gtime = 1 #start time
prefps = 90#preffered fps
size = 2
step = 10
score = 2 #start score
hb = 17 * size #player hitbox
br = 700 #border radius
maxapples = 10
dstep = 2 #how many frames it takes to do the step
optimizationmode = True
optimizationrate = 3
nspeed = 0

#game customization
snakecolor = "green" #paste hex like that: "#285078"
snakeshape = "square" # "square" "circle" "arrow" "classic"
applecolor = "red" #paste hex like that: "#285078"
appleshape = "circle" # "square" "circle" "arrow" "classic" 


#game code

canmove = True

shand = turtle.Turtle()
ahand = turtle.Turtle()
bhand = turtle.Turtle()
scorehand = turtle.Turtle()
mhand = turtle.Turtle()

shand.pu()
shand.ht()
shand.shapesize(size)
shand.color(snakecolor)
shand.shape(snakeshape)
ahand.pu()
ahand.ht()
ahand.shapesize(size)
ahand.color(applecolor)
ahand.shape(appleshape)
bhand.pu()
bhand.ht()
bhand.goto(br, br)
scorehand.pu()
scorehand.ht()
mhand.ht()
mhand.pu()

#controlls
def u():
    global playerrot
    global canmove
    if game.playerrot != 3 and canmove:
        canmove = False
        game.playerrot = 1
def d():
    global playerrot
    global canmove
    if game.playerrot != 1 and canmove:
        canmove = False
        game.playerrot = 3
def r():
    global playerrot
    global canmove
    if game.playerrot != 2 and canmove:
        canmove = False
        game.playerrot = 0
def l():
    global playerrot
    global canmove
    if game.playerrot != 0 and canmove:
        canmove = False
        game.playerrot = 2

class Menu:
    def __init__(self):
        global game
        game = Game(gtime, prefps, size, step, score, hb, br, maxapples, dstep, optimizationmode, optimizationrate, nspeed)
        for i in range(0, 24):
            game.render()
        game.update()
        mhand.goto(-100, 0)
        mhand.write("Game will start in: 3", "center", font=("Arial", 30))
        turtle.update()
        time.sleep(1)
        mhand.clear()
        mhand.goto(-100, 0)
        mhand.write("Game will start in: 2", "center", font=("Arial", 30))
        turtle.update()
        time.sleep(1)
        mhand.clear()
        mhand.goto(-100, 0)
        mhand.write("Game will start in: 1", "center", font=("Arial", 30))
        turtle.update()
        time.sleep(1)
        mhand.clear()
        turtle.update()
 
class Game:
    def __init__(self, gtime, prefps, size, step, score, hb, br, maxapples, dstep, omod, orate, nspeed):
        self.gtime = gtime
        self.prefps = prefps
        self.size = size
        self.step = step
        self.score = score
        self.hb = hb
        self.br = br
        self.maxapples = maxapples
        self.dstep = dstep
        self.omod = omod
        self.orate = orate
        self.nspeed = nspeed
        
        self.snake = []
        self.snake.append(self.Snake(random.randrange(-400, 400, step), random.randrange(-400, 400, step)))
        self.allapples = []
        self.playercamxy = [0, 0]
        self.playerrot = random.randrange(1, 4, 1)

        self.timestamp = time.time()
        
        turtle.onkeypress(u, "Up")
        turtle.onkeypress(d, "Down")
        turtle.onkeypress(r, "Right")
        turtle.onkeypress(l, "Left")

        turtle.listen()
        
    class Snake:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    class Apple:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
    def render(self):
        global gtime
        global camxy
        global score
        global dstep
        global prefps
        global timestamp
        global canmove
        
        #timestamp of render 
        self.timestamp = time.time()
        
        #camera shenenigans
        if self.snake[0].x - self.playercamxy[0] < -50:
            self.playercamxy[0] -= 1
        if self.snake[0].x - self.playercamxy[0] > 50:
            self.playercamxy[0] += 1
        if self.snake[0].y- self.playercamxy[1] < -50:
            self.playercamxy[1] -= 1
        if self.snake[0].y - self.playercamxy[1] > 50:
            self.playercamxy[1] += 1
            
        if self.snake[0].x - self.playercamxy[0] < -150:
            self.playercamxy[0] -= 3
        if self.snake[0].x - self.playercamxy[0] > 150:
            self.playercamxy[0] += 3
        if self.snake[0].y- self.playercamxy[1] < -150:
            self.playercamxy[1] -= 3
        if self.snake[0].y - self.playercamxy[1] > 150:
            self.playercamxy[1] += 3
            
        if self.snake[0].x - self.playercamxy[0] < -300:
            self.playercamxy[0] -= 5
        if self.snake[0].x - self.playercamxy[0] > 300:
            self.playercamxy[0] += 5
        if self.snake[0].y- self.playercamxy[1] < -300:
            self.playercamxy[1] -= 5
        if self.snake[0].y - self.playercamxy[1] > 300:
            self.playercamxy[1] += 5
        #adding things
        while self.maxapples > len(self.allapples):
            tempx = random.randrange(-br+25, br-25, step)
            tempy = random.randrange(-br+25, br-25, step)
            for i in self.snake:
                while i.x == tempx and i.y == tempy:
                    tempx = random.randrange(-br+25, br-25, step)
                    tempy = random.randrange(-br+25, br-25, step)
            self.allapples.append(self.Apple(tempx, tempy))
            
        while self.score > len(self.snake):
            if self.playerrot == 0:
                self.snake.append(self.Snake(self.snake[0].x + self.step, self.snake[0].y))
            if self.playerrot == 1:
                self.snake.append(self.Snake(self.snake[0].x, self.snake[0].y + self.step))
            if self.playerrot == 2:
                self.snake.append(self.Snake(self.snake[0].x - self.step, self.snake[0].y))
            if self.playerrot == 3:
                self.snake.append(self.Snake(self.snake[0].x, self.snake[0].y - self.step))
                
        if  gtime == dstep:
            #eating
            for i in self.allapples:
                if abs(i.x - self.snake[0].x) < hb and abs(i.y - self.snake[0].y) < hb:
                    self.allapples.pop(self.allapples.index(i))
                    self.score += 1
                    self.prefps += self.nspeed
                    
            #moving 2.0
            for i in reversed(range(1, len(self.snake))):
                self.snake[i].x = self.snake[i-1].x
                self.snake[i].y = self.snake[i-1].y
            #moving
            if self.playerrot == 0:
                 self.snake[0].x += self.step
            if self.playerrot == 1:
                 self.snake[0].y += self.step
            if self.playerrot == 2:
               self.snake[0].x -= self.step
            if self.playerrot == 3:
                self.snake[0].y -= self.step
            gtime = 1
        else:
            gtime += 1
        #death
        if self.snake[0].x > self.br or self.snake[0].x < -self.br or self.snake[0].y > self.br or self.snake[0].y < -self.br:
            turtle.textinput('Snakymenu', "You died")
            menu = Menu()
                
        for i in reversed(range(1, len(self.snake))):
            if self.snake[0].x == self.snake[i].x and self.snake[0].y == self.snake[i].y:
                turtle.textinput('Snakymenu', "You died")
                menu = Menu()

        #cant change diractions twice per frame
        canmove = True
        
    def update(self):
        shand.clearstamps()
        ahand.clearstamps()
        bhand.clear()

        if self.omod:
            for i in range(0, len(self.snake), self.orate):
                shand.goto(self.snake[i].x-self.playercamxy[0], self.snake[i].y-self.playercamxy[1])
                shand.stamp()
            for i in range(len(self.snake)-1, len(self.snake)):
                shand.goto(self.snake[i].x-self.playercamxy[0], self.snake[i].y-self.playercamxy[1])
                shand.stamp()
        else:
            for i in range(0, len(self.snake)):
                shand.goto(self.snake[i].x-self.playercamxy[0], self.snake[i].y-self.playercamxy[1])
                shand.stamp()
            for i in range(len(self.snake), len(self.snake)):
                shand.goto(self.snake[i].x-self.playercamxy[0], self.snake[i].y-self.playercamxy[1])
                shand.stamp()
                
        for i in self.allapples:
            ahand.goto(i.x-self.playercamxy[0], i.y-self.playercamxy[1])
            ahand.stamp()
        bhand.pd()
        bhand.goto(br - self.playercamxy[0], -br - self.playercamxy[1])
        bhand.goto(-br - self.playercamxy[0], -br - self.playercamxy[1])
        bhand.goto(-br - self.playercamxy[0], br - self.playercamxy[1])
        bhand.goto(br- self.playercamxy[0], br - self.playercamxy[1])
        scorehand.goto(-350, 350)
        scorehand.clear()
        scorehand.write(self.score-1, "left", font=("Arial", 30))
        turtle.update()

    def run(self):
        self.render()
        self.update()
        try:
            time.sleep(1/self.prefps - (time.time() - self.timestamp))
        except:
            None
            
menu = Menu()

while True:
    game.run()
