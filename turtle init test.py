import turtle
#5x5 (boardSize x boardSize)
boardSize=8
startX=1;startY=5
endX=3;endY=3
pic="unicorn.gif"
blank ="square.gif"
#turtle formula: goto(col*100-350,row*100+350)

def initTurtle():
    global sqSize
    turtle.setup(1000,1000,0,0)
    winH=turtle.window_height()-20;winW=turtle.window_width()-20
    turtle.title("Knight's Tour")
    turtle.setworldcoordinates(0,1000,1000,0)
    turtle.ht()
    turtle.pen(pencolor="black")
    turtle.pen(pensize=3)
    turtle.speed(0)
    if(winW<winH):
        sqSize=winW/(boardSize+1)
    else:
        sqSize=winH/(boardSize+1)
    for r in range(0,boardSize+1): #draw horizontal rows
        goto(30,r*sqSize+30)
        drto(boardSize*sqSize+30,r*sqSize+30)
    
    for c in range(0,boardSize+1): #draw vertical columns
        goto((c)*sqSize+30,30)
        drto(c*sqSize+30,boardSize*sqSize+30)
    turtle.Screen().addshape("unicorn.gif")
    turtle.Screen().addshape("square.gif")
    turtle.shape(pic)
    
def goto(x,y):
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    
def drto(x,y):
    turtle.goto(x,y)

def stampAt(c,r):
    goto((c-1)*sqSize+80,(boardSize-r+1)*sqSize-30)
    turtle.shape(pic)
    turtle.stamp()

def clearStamp(c,r):
    goto((c-1)*sqSize+80,(boardSize-r+1)*sqSize-30)
    turtle.shape(blank)
    turtle.stamp()
    
def clr():
    turtle.undo()



initTurtle()
stampAt(1,1)
stampAt(2,2)
stampAt(1,5)
stampAt(5,1)
stampAt(8,8)
stampAt(8,2)
clearStamp(1,1)
while True:
    clr()













