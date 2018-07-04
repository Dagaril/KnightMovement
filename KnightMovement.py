import turtle
import datetime
#5x5 (boardSize x boardSize)
boardSize=7
startX=1;startY=7
endX=2;endY=6
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
    turtle.shape(blank)
    
def goto(x,y):
    turtle.pu()
    turtle.goto(x,y)
    turtle.pd()
    
def drto(x,y):
    turtle.goto(x,y)
    
def stampAt(c,r):
    global step
    step +=1
    goto(c*sqSize,(boardSize-r+1)*sqSize)
    turtle.write(step, False, "center", ("Arial",16,"normal"))
#    turtle.shape(pic)
#    turtle.stamp()

def clearStamp():
    global step
    step-=1
    for i in range(4):
        turtle.undo()
    
##def clearStamp(c,r):
##    global step
##    step-=1
##    goto((c-1)*100-350,350-(boardSize-r)*100)
###    turtle.shape(blank)
##    turtle.stamp()

def setDirections(arr):
    arr=[0,0,0,0,0,0,0,0] #sets all direction movement to false (will be changed to true if knight can move in any direction)
    return arr


def setMoves(x,y, arrMoves, arrDirections):
    arrDirections = setDirections(arrDirections)
    #left one, up/down two
    if x-1>0:
        if y-2>0 and (len(arrMoves)==0 or arrMoves[len(arrMoves)-1]!="ruu"):
            arrDirections[2] = 1
        if y+2<=boardSize and (len(arrMoves)==0 or arrMoves[len(arrMoves)-1]!="rdd"):
            arrDirections[0] = 1
    #right one, up/down two
    if x+1<=boardSize:
        if y-2>0 and (len(arrMoves)==0 or arrMoves[len(arrMoves)-1]!="luu"):
            arrDirections[3] = 1
        if y+2<=boardSize and (len(arrMoves)==0 or arrMoves[len(arrMoves)-1]!="ldd"):
            arrDirections[1] = 1
    #left two, up/down one
    if x-2>0:
        if y-1>0 and (len(arrMoves)==0 or arrMoves[len(arrMoves)-1]!="rru"):
            arrDirections[4] = 1
        if y+1<=boardSize and (len(arrMoves)==0 or arrMoves[len(arrMoves)-1]!="rrd"):
            arrDirections[6] = 1
    #right two, up/down one
    if x+2<=boardSize:
        if y-1>0 and (len(arrMoves)==0 or arrMoves[len(arrMoves)-1]!="llu"):
            arrDirections[5] = 1
        if y+1<=boardSize and (len(arrMoves)==0 or arrMoves[len(arrMoves)-1]!="lld"):
            arrDirections[7] = 1
    return arrDirections


def move(x,y,arrMoves, arrDirections):
    if arrDirections[2] == 1 and (len(arrMoves) == 0 or arrMoves[len(arrMoves)-1]!= "ruu"):
        arrMoves.append("ldd")
        x-=1;y-=2
    elif arrDirections[3] == 1 and (len(arrMoves) == 0 or arrMoves[len(arrMoves)-1]!= "luu"):
        arrMoves.append("rdd")
        x+=1;y-=2
    elif arrDirections[4] == 1 and (len(arrMoves) == 0 or arrMoves[len(arrMoves)-1]!= "rru"):
        arrMoves.append("lld")
        x-=2;y-=1
    elif arrDirections[5] == 1 and (len(arrMoves) == 0 or arrMoves[len(arrMoves)-1]!= "llu"):
        arrMoves.append("rrd")
        x+=2;y-=1
    elif arrDirections[0] == 1 and (len(arrMoves) == 0 or arrMoves[len(arrMoves)-1]!= "rdd"):
        arrMoves.append("luu")
        x-=1;y+=2
    elif arrDirections[1] == 1 and (len(arrMoves) == 0 or arrMoves[len(arrMoves)-1]!= "ldd"):
        arrMoves.append("ruu")
        x+=1;y+=2
    elif arrDirections[6] == 1 and (len(arrMoves) == 0 or arrMoves[len(arrMoves)-1]!= "rrd"):
        arrMoves.append("llu")
        x-=2;y+=1
    elif arrDirections[7] == 1 and (len(arrMoves) == 0 or arrMoves[len(arrMoves)-1]!= "lld"):
        arrMoves.append("rru")
        x+=2;y+=1
    directions = setMoves(x,y,arrMoves,arrDirections)
    return (x,y,arrMoves,directions)

def checkIfAllDirectionsFalse(arrDirections):
    if sum(arrDirections)==0:
        return True
    else:
        return False


def checkForRepeatLocation(x,y,xPos,yPos):
    prevX=[];prevY=[]; retBool = False
    for i in range(0,len(xPos)-1):
        if xPos[i] == x:
            prevX.append(i)
    for z in range(0,len(yPos)-1):
        if yPos[z] == y:
            prevY.append(z)
    for j in range(0,len(prevX)):
        if prevX[j] in prevY:
            retBool = True
    return retBool

def makeLastMoveFalse(arrMoves, arrDirections):
    if arrMoves[len(arrMoves)-1] == "luu":
        arrDirections[0] = 0
    elif arrMoves[len(arrMoves)-1] == "ruu":
        arrDirections[1] = 0
    elif arrMoves[len(arrMoves)-1] == "ldd":
        arrDirections[2] = 0
    elif arrMoves[len(arrMoves)-1] == "rdd":
        arrDirections[3] = 0
    elif arrMoves[len(arrMoves)-1] == "lld":
        arrDirections[4] = 0
    elif arrMoves[len(arrMoves)-1] == "rrd":
        arrDirections[5] = 0
    elif arrMoves[len(arrMoves)-1] == "llu":
        arrDirections[6] = 0
    elif arrMoves[len(arrMoves)-1] == "rru":
        arrDirections[7] = 0
    arrMoves = arrMoves [:-1]
    return (arrDirections, arrMoves)


def moveOneStepBack(x,y,xPos,yPos, directions, possMoves,moves):
    x=xPos[len(xPos)-2]
    y=yPos[len(yPos)-2]
#    print("Now at" , x , y)
    xPos = xPos[:-1]
    yPos = yPos[:-1]
    directions=possMoves[len(possMoves)-1]
    possMoves=possMoves[:-1]
    directions,moves = makeLastMoveFalse(moves,directions)
    return(x,y,xPos,yPos,directions,possMoves,moves)

def finalLocation(x, y, eX, eY, xPos):
    if x==eX and y==eY and len(xPos)==boardSize**2:
        return True
    else:
        return False

def falseFinal(x,y,eX,eY,xPos):
    if x==eX and y==eY and len(xPos)<boardSize**2:
        return True
    return False

def moveNum(x):
    return{
        'luu':0,
        'ruu':1,
        'ldd':2,
        'rdd':3,
        'lld':4,
        'rrd':5,
        'llu':6,
        'rru':7
        }[x]


def writeToFile(x,y,xPos,yPos,directions,possMoves,moves):
    file = open("log.txt",'w')
    file.write("x:" + str(x));file.write("\ny: "+ str(y))
    file.write("\ndirections: "+ str(directions))
    file.write("\nxPos: "+str(xPos))
    file.write("\nyPos: "+str(yPos))
    file.write("\nx,y:         possMoves:                 moves:")
    for i in range(0,len(possMoves)):
        file.write("\n"+str(xPos[i])+","+str(yPos[i])+"  "+str(possMoves[i])+"         "+str(moveNum(moves[i]))+"  "+str(moves[i]))
    file.write("\n"+str(xPos[len(xPos)-1])+","+str(yPos[len(yPos)-1]))
    file.close()

def noSolution(x,y,directions):
    global startX, startY
    if x==startX and y==startY and sum(directions)==0:
       return True;
    return False;

print(datetime.datetime.now())
xPos = []
yPos = []
moves = []
possMoves = []
directions = [0,0,0,0,0,0,0,0] #[luu,ruu,ldd,rdd,lld,rrd,llu,rru]

x = startX; y = startY
xPos.append(x);yPos.append(y)
directions=setMoves(x,y,moves,directions)
initTurtle()
step=0
stampAt(x,y)
while True:
    if finalLocation(x,y,endX,endY,xPos):
        break
    if noSolution(x,y,directions):
        print("NO SOLUTION")
        break
    if not checkForRepeatLocation(x,y,xPos,yPos) and not checkIfAllDirectionsFalse(directions) and not falseFinal(x,y,endX,endY,xPos):
        possMoves.append(directions)
        x,y,moves,directions = move(x,y,moves,directions)
        xPos.append(x);yPos.append(y)
#        print(x,y)
        if not checkForRepeatLocation(x,y,xPos,yPos)and not falseFinal(x,y,endX,endY,xPos):
            stampAt(x,y)
    else:
        if checkForRepeatLocation(x,y,xPos,yPos):
#            print ("\u290A Been Here Before")
            pass
        elif falseFinal(x,y,endX,endY,xPos):
#            print("-----------------------------------FALSE FINAL")
#            clearStamp()
            pass
        else:  
#            print ("Hit dead end")
            clearStamp()
        x,y,xPos,yPos,directions,possMoves,moves=moveOneStepBack(x,y,xPos,yPos, directions, possMoves, moves)
    writeToFile(x,y,xPos,yPos,directions,possMoves,moves)

print("FINISHED")
print(datetime.datetime.now())
