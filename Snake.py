from graphics import *
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
    
        
#def newApple():

#def grow():

#def loss():

#def win():


        


def main():

    START = Rectangle(Point(60, 170),Point(74, 186))
    START.setFill("Red")
    START.setOutline("red")
    START.draw(win)
    
    global lost
    lost = False
    
    global direction
    direction = 1

    spawn()

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
    
