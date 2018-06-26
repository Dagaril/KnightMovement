import turtle
#5x5 (boardSize x boardSize)
boardSize=5
startX=1;startY=5
endX=3;endY=3
pic="unicorn.gif"
blank ="square.gif"
#turtle formula: goto(c*sqSize+30,30);drto(c*sqSize+30,boardSize*sqSize+30)

def initTurtle():
    global sqSize
    turtle.setup(1000,1000,0,0)
    winH=turtle.window_height()-30;winW=turtle.window_width()-30
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

def clearStamp():
    global step
    step-=1
    turtle.undo()
    turtle.undo()
    turtle.undo()
    turtle.undo()
    
def stampAt(c,r):
    global step
    step +=1
    goto(c*sqSize,(boardSize-r+1)*sqSize)
    turtle.write(step, False, "center", ("Arial",16,"normal"))
#    turtle.shape(pic)
#    turtle.stamp()

##def clearStamp(c,r):
##    global step
##    step-=1
##    goto((c-1)*100-350,350-(boardSize-r)*100)
###    turtle.shape(blank)
##    turtle.stamp()
