from graphics import *
from random import *

snake = [0]*4
size = 4
Score = 0

scoreboard = Text(Point(420,130),"Score: " + str(Score))
scoreboard.setOutline("white")
scoreboard.setSize(16)

win = GraphWin("T I N Y   S N E K", 600, 600)
win.setBackground("Black")
Border = Rectangle(Point(52,164), Point(547,554))
Border.setFill("light Green")
Border.setOutline("Dark Green")
Border.setWidth(15)
Border.draw(win)

def spawn():
    global snake
    snake = [0]*4
    size = 4
    for i in range(size):
        snake[i] = Rectangle(Point(300-(i*15), 247),Point(300-(i*15)+14, 261))
        snake[i].setFill("cyan")
        snake[i].draw(win)

def destroy():
    global size
    for i in range(size):
        snake[i].undraw()
    size =4

def difficulty():
    global speed
    diff = Text(Point(300,80),"Select difficulty:\n1. Easy\n2. Normal\n3. Hard")
    diff.setOutline("white")
    diff.setSize(16)
    diff.draw(win)
    k = win.checkKey()
    while (k!="1" or k!="2" or k!="3"):
        k = win.getKey()
        if (k=="1"):
            speed = 0.125
            break
        elif (k=="2"):
            speed = 0.1
            break
        elif (k=="3"):
            speed = 0.075
            break
    diff.undraw()

    
def move(k, win):
    max = size-1
    snake[max].undraw()
    
    while max > 0:
        snake[max] = snake[max-1]
        max = max -1
        
    snake[0] = snake[1].clone()
    if direction == 1:
        snake[0].move(15,0)
    elif direction == 2:
        snake[0].move(0,15)
    elif direction == 3:
        snake[0].move(-15,0)
    elif direction == 4:
        snake[0].move(0,-15)

    snake[0].draw(win)



def gameOver():
    global GameOver
    GameOver = Text(Point(300,50),"Game Over. \n Press 'R' to Retry or Esc to Exit.")
    GameOver.setOutline("white")
    GameOver.setSize(16)
    GameOver.draw(win)

def checkCollision():
    if (snake[0].getCenter().getX() > 545 or
        snake[0].getCenter().getX() < 60 or
        snake[0].getCenter().getY() < 175 or
        snake[0].getCenter().getY() > 545):
        return True

    elif (snake[0].getCenter().getX() == Apple.getCenter().getX() and
          snake[0].getCenter().getY() == Apple.getCenter().getY()):
        newApple()
        grow()
        score()
        
    for j in range(3, size):
        if (snake[0].getCenter().getX() == snake[j].getCenter().getX() and
            snake[0].getCenter().getY() == snake[j].getCenter().getY()):
            return True
  
    

    
def newApple():
    
    dx = (randint(0, 31))*15
    dy = (randint(0, 24))*15
    valid = True
    
    global Apple
    try :
        Apple.undraw()  
    except :
        pass  
    for i in range(size):
        if (snake[i].getP1().getX() == (60+dx) and
            snake[i].getP1().getY() == (74+dx)):
            print("Oops. Recalculating...")
            newApple()
            valid = False
    if valid==True:
        Apple = Rectangle(Point(60+dx, 172+dy),Point(74+dx, 186+dy))
        Apple.setFill("Red")
        Apple.setOutline("darkred")
        Apple.draw(win)

def grow():
    global size
    size = size +2
    snake.append(snake[size-3].clone())
    snake.append(snake[size-3].clone())

def score():
    Score = int(((size-4)/2)*10)
    scoreboard = Text(Point(420,130),"Score: " + str(Score))
    cover = Rectangle(Point(350,120), Point(480,140))
    cover.setFill("Black")
    cover.draw(win)
    scoreboard.setOutline("white")
    scoreboard.setSize(16)
    scoreboard.draw(win)

def pause():
    Pause = Text(Point(300,50), "Game Paused\nPress any key to continue...")
    Pause.setOutline("White")
    Pause.setSize(16)
    Pause.draw(win)
    p = win.getKey()
    Pause.undraw()
    
    

#def loss():

#def win():


def instructions():
    instructions = Text(Point(300,50),"Use W, A, S, D (Or arrow keys) to move \nand Escape to pause the game. Press any key to start... ")
    instructions.setOutline("white")
    instructions.setSize(16)
    instructions.draw(win)
    
    win.getKey()

    instructions.undraw()


def main():
    
    
    
    
    global lost
    lost = False
    
    global direction
    direction = 1

    spawn()
    newApple()
    score()

    difficulty()
    instructions()
    
    
    while(lost!=True):
        k = win.checkKey()
        time.sleep(speed)
        if checkCollision() == True:
            lost = True
            gameOver()
        elif ((k == "d" or k == "Right") and direction!=3):
            direction = 1
            move(k, win)
        elif ((k == "s" or k == "Down") and direction!=4):
            direction = 2
            move(k, win)
        elif ((k == "a" or k == "Left") and direction!=1):
            direction  = 3
            move(k, win)
        elif ((k == "w" or k == "Up") and direction!=2):
            direction  = 4
            move(k, win)
        elif k == "Escape":
            pause()
        
        else:
            move(k, win)

        

    
    end = win.checkKey()
    while(end!="r" or end!="Escape"):
        end = win.getKey()
        if end =="r":
            destroy()
            GameOver.undraw()
            main()
        elif end == "Escape":
            win.close()
    
main()
    
