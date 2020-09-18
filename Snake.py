from graphics import *
snake = [0]*4
size = 4
win = GraphWin("T I N Y   S N E K", 600, 500)
win.setBackground("lightblue")

def spawn():
    global snake
    snake = [0]*4
    size = 4
    for i in range(size):
        snake[i] = Rectangle(Point(300-(i*5), 252),Point(300-(i*5)+4, 248))
        snake[i].setFill("black")
        snake[i].draw(win)
        
def move(k, win):
    max = size-1
    snake[max].undraw()
    
    while max > 0:
        snake[max] = snake[max-1]
        max = max -1
        
    snake[0] = snake[1].clone()
    if direction == 1:
        snake[0].move(5,0)
    elif direction == 2:
        snake[0].move(0,5)
    elif direction == 3:
        snake[0].move(-5,0)
    elif direction == 4:
        snake[0].move(0,-5)

    snake[0].draw(win)



def gameOver():
    GameOver = Text(Point(300,50),"Game Over. Press any key to exit...")
    GameOver.setOutline("white")
    GameOver.setSize(16)
    GameOver.draw(win)

def checkCollision():
    if (snake[0].getCenter().getX() > 600 or
        snake[0].getCenter().getX() < 0 or
        snake[0].getCenter().getY() < 0 or
        snake[0].getCenter().getY() > 500):
        return True
    
        
#def newApple():

#def grow():

#def loss():

#def win():


        


def main():

    START = Rectangle(Point(295, 252),Point(299, 248))
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
        time.sleep(0.1)
        if (k == "d" and direction!=3):
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
        elif checkCollision() == True:
            lost = True
            gameOver()
        else:
            move(k, win)

        

    
    win.getKey()
    win.close()
    
main()
    
