import turtle, random, time, math

turtle.title("Snakysnake")
turtle.tracer(0)

gtime = 1 #start time
prefps = 120 #preffered fps
size = 2
step = 40
score = 2 #start score
hb = 35 #player hitbox; 37 for 2
br = 700 #border radius
maxapples = 10
dstep = 6 #how many frames it takes to do the step

shand = turtle.Turtle()
ahand = turtle.Turtle()
bhand = turtle.Turtle()
scorehand = turtle.Turtle()
mhand = turtle.Turtle()

shand.pu()
shand.ht()
shand.shapesize(size)
shand.color("green")
shand.shape("square")
ahand.pu()
ahand.ht()
ahand.shapesize(size)
ahand.color("red")
ahand.shape("circle")
bhand.pu()
bhand.ht()
bhand.goto(br, br)
scorehand.pu()
scorehand.ht()
mhand.ht()
mhand.pu()

class Menu:
    def __init__(self):
        wannaplay = turtle.textinput('Snakymenu', "Wanna play? (y/n)")
        if wannaplay == "y":
            mhand.goto(-100, 0)
            mhand.write("Game will start in: 3", "center", font=("Arial", 30))
            turtle.update()
            time.sleep(1)
            mhand.clear()
            mhand.goto(-100, 0)
            mhand.write("Game will start in: 2", "center", font=("Arial", 30))
            turtle.update()
            mhand.clear()
            mhand.goto(-100, 0)
            time.sleep(1)
            mhand.write("Game will start in: 1", "center", font=("Arial", 30))
            turtle.update()
            mhand.clear()
            time.sleep(1)
            turtle.update()
        else:
            turtle.bye()
 
class Game:
    def __init__(self, gtime, prefps, size, step, score, hb, br, maxapples, dstep):
        self.gtime = gtime
        self.prefps = prefps
        self.size = size
        self.step = step
        self.score = score
        self.hb = hb
        self.br = br
        self.maxapples = maxapples
        self.dstep = dstep
        
        self.snake = []
        self.snake.append(self.Snake(0, 0))
        self.allapples = []
        self.playercamxy = [0, 0]
        self.playerrot = 1

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
            self.allapples.append(self.Apple(random.randrange(-br+25, br-25, step), random.randrange(-br+25, br-25, step)))
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
            turtle.bye()
        for i in reversed(range(1, len(self.snake))):
            if self.snake[0].x == self.snake[i].x and self.snake[0].y == self.snake[i].y:
                turtle.bye()
            
    def update(self):
        shand.clearstamps()
        ahand.clearstamps()
        bhand.clear()
        
        for i in self.snake:
            shand.goto(i.x-self.playercamxy[0], i.y-self.playercamxy[1])
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

menu = Menu()

game = Game(gtime, prefps, size, step, score, hb, br, maxapples, dstep)

#controlls
def u():
    global playerrot
    if game.playerrot != 3:
        game.playerrot = 1
def d():
    global playerrot
    if game.playerrot != 1:
        game.playerrot = 3
def r():
    global playerrot
    if game.playerrot != 2:
        game.playerrot = 0
def l():
    global playerrot
    if game.playerrot != 0:
        game.playerrot = 2

turtle.onkey(u, "Up")
turtle.onkey(d, "Down")
turtle.onkey(r, "Right")
turtle.onkey(l, "Left")

turtle.listen()

while True:
    game.render()
    game.update()
    time.sleep(1/prefps)
