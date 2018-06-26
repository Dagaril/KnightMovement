import turtle
#5x5 (boardSize x boardSize)
boardSize=5
startX=1;startY=5
endX=3;endY=3
pic="unicorn.gif"
blank ="square.gif"
#turtle formula: goto(col*100-350,row*100+350)

def initTurtle():
    turtle.setup(1000,1000)
    turtle.ht()
    turtle.pen(pencolor="black")
    turtle.pen(pensize=3)
    turtle.speed(500)
    goto(-400,400)
    for r in range(0,boardSize+1): #draw horizontal rows
        goto(-400,-r*100+400)
        
        drto(boardSize*100-400,-r*100+400)
    goto(-400,400)
    for c in range(0,boardSize+1): #draw vertical columns
        goto((c)*100-400,400)
        drto(c*100-400,-boardSize*100+400)
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
    goto((c-1)*100-350,350-(boardSize-r)*100)
    turtle.shape(pic)
    turtle.stamp()

def clearStamp(c,r):
    goto((c-1)*100-350,350-(boardSize-r)*100)
    turtle.shape(blank)
    turtle.stamp()




initTurtle()
stampAt(1,1)
stampAt(2,2)
stampAt(1,5)
stampAt(5,1)
stampAt(8,8)
stampAt(8,2)
clearStamp(1,1)















