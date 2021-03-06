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
scoreboard.draw(win)

def spawn():
    global snake
    snake = [0]*4
    size = 4
    for i in range(size):
        snake[i] = Rectangle(Point(300-(i*15), 247),Point(300-(i*15)+14, 261))
        snake[i].setFill("cyan")
        snake[i].draw(win)
        
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
    GameOver = Text(Point(300,50),"Game Over. Press any key to exit...")
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
    for j in range(3, size):
        if (snake[0].getCenter().getX() == snake[j].getCenter().getX() and
            snake[0].getCenter().getY() == snake[j].getCenter().getY()):
            return True
  
    
def newApple():
    
    dx = (randint(0, 31))*15
    dy = (randint(0, 24))*15
    global Apple
    try :
        Apple.undraw()  
    except :
        pass  
    
    Apple = Rectangle(Point(60+dx, 172+dy),Point(74+dx, 186+dy))
    Apple.setFill("Red")
    Apple.setOutline("darkred")
    Apple.draw(win)

def grow():
    global size
    size = size +2
    snake.append(snake[size-3].clone())
    snake.append(snake[size-3].clone())
    

#def loss():

#def win():


        


def main():
    
    newApple()
        
    global lost
    lost = False
    
    global direction
    direction = 1

    spawn()

    instructions = Text(Point(300,50),"Use W, A, S, D to move \nand Escape to exit. Press any key to start... ")
    instructions.setOutline("white")
    instructions.setSize(16)
    instructions.draw(win)
    
    win.getKey()

    instructions.undraw()
    
    while(lost!=True):
        k = win.checkKey()
        time.sleep(0.15)
        if checkCollision() == True:
            lost = True
            gameOver()
        elif (k == "d" and direction!=3):
            direction = 1
            move(k, win)
        elif (k == "s" and direction!=4):
            direction = 2
            move(k, win)
        elif (k == 'a' and direction!=1):
            direction  = 3
            move(k, win)
        elif (k == 'w' and direction!=2):
            direction  = 4
            move(k, win)
        elif k == "Escape":
            lost = True
            gameOver()
        
        else:
            move(k, win)

        

    
    win.getKey()
    win.close()
    
main()
    
