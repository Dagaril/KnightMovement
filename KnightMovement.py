import turtle
import datetime
#5x5 (boardSize x boardSize)
boardSize=5
startX=4;startY=3
#turtle formula: goto(c*sqSize,(boardSize-r+1)*sqSize)

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

def clearStamp():
    global step
    step-=1
    for i in range(4):
        turtle.undo()

def setDirections(arr):
    arr=[0,0,0,0,0,0,0,0] #sets all direction movement to false (will be changed to true if knight can move in any direction)
    return arr


def setMoves(x,y, arrMoves, arrDirections,prevX,prevY):
    arrDirections = setDirections(arrDirections)
    #left one, up/down two
    if x-1>0:
        if y-2>0 and (len(arrMoves)==0 or arrMoves[len(arrMoves)-1]!="ruu")and not (x-1==prevX and y-2==prevY):
            arrDirections[2] = 1
        if y+2<=boardSize and (len(arrMoves)==0 or arrMoves[len(arrMoves)-1]!="rdd")and not (x-1==prevX and y+2==prevY):
            arrDirections[0] = 1
    #right one, up/down two
    if x+1<=boardSize:
        if y-2>0 and (len(arrMoves)==0 or arrMoves[len(arrMoves)-1]!="luu")and not (x+1==prevX and y-2==prevY):
            arrDirections[3] = 1
        if y+2<=boardSize and (len(arrMoves)==0 or arrMoves[len(arrMoves)-1]!="ldd")and not (x+1==prevX and y+2==prevY):
            arrDirections[1] = 1
    #left two, up/down one
    if x-2>0:
        if y-1>0 and (len(arrMoves)==0 or arrMoves[len(arrMoves)-1]!="rru")and not (x-2==prevX and y-1==prevY):
            arrDirections[4] = 1
        if y+1<=boardSize and (len(arrMoves)==0 or arrMoves[len(arrMoves)-1]!="rrd")and not (x-2==prevX and y+1==prevY):
            arrDirections[6] = 1

    #right two, up/down one
    if x+2<=boardSize:
        if y-1>0 and (len(arrMoves)==0 or arrMoves[len(arrMoves)-1]!="llu")and not (x+2==prevX and y-1==prevY):
            arrDirections[5] = 1
        if y+1<=boardSize and (len(arrMoves)==0 or arrMoves[len(arrMoves)-1]!="lld")and not (x+2==prevX and y+1==prevY):
            arrDirections[7] = 1
    return arrDirections

def directionsDict(index,x,y):
    if(index==0):
        return x-1,y+2
    elif(index==1):
        return x+1,y+2
    elif(index==2):
        return x-1,y-2
    elif(index==3):
        return x+1,y-2
    elif(index==4):
        return x-2,y-1
    elif(index==5):
        return x+2,y-1
    elif(index==6):
        return x-2,y+1
    elif(index==7):
        return x+2,y+1

def indexToMove(x):
    return{
        0:'luu',
        1:'ruu',
        2:'ldd',
        3:'rdd',
        4:'lld',
        5:'rrd',
        6:'llu',
        7:'rru'
        }[x]

def move(x,y,arrMoves, arrDirections,prevX,prevY):
    if(sum(arrDirections)==1):
        x,y=directionsDict(arrDirections.index(1),x,y)
        arrMoves.append(indexToMove(arrDirections.index(1)))
        directions = setMoves(x,y,arrMoves,arrDirections,prevX,prevY)
        return (x,y,arrMoves,directions)
    numMovesInDir=[0,0,0,0,0,0,0,0]
    for i in range(len(arrDirections)):
        if(arrDirections[i]==1):
            tempX,tempY=directionsDict(i,x,y)
            numMovesInDir[i]=sum(setMoves(tempX,tempY,arrMoves,arrDirections,x,y))
    minI=numMovesInDir.index(min(x for x in numMovesInDir if x > 0))
    x,y=directionsDict(minI,x,y)
    arrMoves.append(indexToMove(minI))
    directions = setMoves(x,y,arrMoves,arrDirections,prevX,prevY)
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
    xPos = xPos[:-1]
    yPos = yPos[:-1]
    directions=possMoves[len(possMoves)-1]
    possMoves=possMoves[:-1]
    directions,moves = makeLastMoveFalse(moves,directions)
    return(x,y,xPos,yPos,directions,possMoves,moves)

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
directions=setMoves(x,y,moves,directions,60,60)
initTurtle()
step=0
stampAt(x,y)
while True:
    if step==boardSize**2:
        break
    if noSolution(x,y,directions):
        print("NO SOLUTION")
        break
    if not checkForRepeatLocation(x,y,xPos,yPos) and not checkIfAllDirectionsFalse(directions):
        possMoves.append(directions)
        x,y,moves,directions = move(x,y,moves,directions,xPos[len(xPos)-1],yPos[len(yPos)-1])
        xPos.append(x);yPos.append(y)
        if not checkForRepeatLocation(x,y,xPos,yPos):
            stampAt(x,y)
    else:
        if not checkForRepeatLocation(x,y,xPos,yPos):
            clearStamp()
        x,y,xPos,yPos,directions,possMoves,moves=moveOneStepBack(x,y,xPos,yPos, directions, possMoves, moves)
    writeToFile(x,y,xPos,yPos,directions,possMoves,moves)

print("FINISHED")
print(datetime.datetime.now())
