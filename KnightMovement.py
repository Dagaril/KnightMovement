#3x3
def setDirections(arr):
    arr=[0,0,0,0,0,0,0,0] #sets all direction movement to false (will be changed to true if knight can move in any direction)
    return arr


def setMoves(x,y, arrMoves, arrDirections):
    arrDirections = setDirections(arrDirections)
    #left one, up/down two
    if x-1>0:
        if y-2>0 and (len(arrMoves)==0 or arrMoves[len(arrMoves)-1]!="ruu"):
            arrDirections[2] = 1
        if y+2<=3 and (len(arrMoves)==0 or arrMoves[len(arrMoves)-1]!="rdd"):
            arrDirections[0] = 1
    #right one, up/down two
    if x+1<=3:
        if y-2>0 and (len(arrMoves)==0 or arrMoves[len(arrMoves)-1]!="luu"):
            arrDirections[3] = 1
        if y+2<=3 and (len(arrMoves)==0 or arrMoves[len(arrMoves)-1]!="ldd"):
            arrDirections[1] = 1
    #left two, up/down one
    if x-2>0:
        if y-1>0 and (len(arrMoves)==0 or arrMoves[len(arrMoves)-1]!="rru"):
            arrDirections[4] = 1
        if y+1<=3 and (len(arrMoves)==0 or arrMoves[len(arrMoves)-1]!="rrd"):
            arrDirections[6] = 1
    #right two, up/down one
    if x+2<=3:
        if y-1>0 and (len(arrMoves)==0 or arrMoves[len(arrMoves)-1]!="llu"):
            arrDirections[5] = 1
        if y+1<=3 and (len(arrMoves)==0 or arrMoves[len(arrMoves)-1]!="lld"):
            arrDirections[7] = 1
    return arrDirections


def move(x,y,arrMoves, arrDirections):
    if arrDirections[2] == True and (len(arrMoves) == 0 or arrMoves[len(arrMoves)-1]!= "ruu"):
        arrMoves.append("ldd")
        x-=1;y-=2
    elif arrDirections[3] == True and (len(arrMoves) == 0 or arrMoves[len(arrMoves)-1]!= "luu"):
        arrMoves.append("rdd")
        x+=1;y-=2
    elif arrDirections[4] == True and (len(arrMoves) == 0 or arrMoves[len(arrMoves)-1]!= "rru"):
        arrMoves.append("lld")
        x-=2;y-=1
    elif arrDirections[5] == True and (len(arrMoves) == 0 or arrMoves[len(arrMoves)-1]!= "llu"):
        arrMoves.append("rrd")
        x+=2;y-=1
    elif arrDirections[0] == True and (len(arrMoves) == 0 or arrMoves[len(arrMoves)-1]!= "rdd"):
        arrMoves.append("luu")
        x-=1;y+=2
    elif arrDirections[1] == True and (len(arrMoves) == 0 or arrMoves[len(arrMoves)-1]!= "ldd"):
        arrMoves.append("ruu")
        x+=1;y+=2
    elif arrDirections[6] == True and (len(arrMoves) == 0 or arrMoves[len(arrMoves)-1]!= "rrd"):
        arrMoves.append("llu")
        x-=2;y+=1
    elif arrDirections[7] == True and (len(arrMoves) == 0 or arrMoves[len(arrMoves)-1]!= "lld"):
        arrMoves.append("rru")
        x+=2;y+=1
    return (x,y,arrMoves,arrDirections)

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
    print("Now at" , x , y)
    xPos = xPos[:-1]
    yPos = yPos[:-1]
    stepNum = len(moves)-1
#    print(possMoves)
    directions=possMoves[stepNum]
    possMoves=possMoves[:-1]
    directions,moves = makeLastMoveFalse(moves,directions)
    possMoves.append(directions)
    return(x,y,xPos,yPos,directions,possMoves,moves)


xPos = [];yPos=[]; moves = []; possMoves = []; directions = [0,0,0,0,0,0,0,0] #[luu,ruu,ldd,rdd,lld,rrd,llu,rru]
skipSetMoves = False
x = 2; y = 3
xPos.append(x);yPos.append(y)
directions=setMoves(x,y,moves,directions)
print(x,y)
while len(moves)!=7 or not(x==1 and y==1):
    if not checkForRepeatLocation(x,y,xPos,yPos) and not checkIfAllDirectionsFalse(directions):
        if not skipSetMoves:
            directions = setMoves(x,y,moves,directions)
            possMoves.append(directions)
        skipSetMoves = False
        x,y,moves,directions = move(x,y,moves,directions)
        xPos.append(x);yPos.append(y)
        print(x,y)
    else:
        if checkForRepeatLocation(x,y,xPos,yPos):
            print ("\u290A Been Here Before")
        else:
            print ("Hit dead end")
        x,y,xPos,yPos,directions,possMoves,moves=moveOneStepBack(x,y,xPos,yPos, directions, possMoves, moves)
        skipSetMoves = True
    possMovesLen=len(possMoves)

print("FINISHED")

"""
def makeListOfDirections():
    global luu; global ruu; global ldd;global rdd; global lld; global rrd; global llu; global rru
    list1=[]
    if luu == False:
        list1.append(0)
    else:
        list1.append(1)
    if ruu == False:
        list1.append(0)
    else:
        list1.append(1)
    if ldd == False:
        list1.append(0)
    else:
        list1.append(1)
    if rdd == False:
        list1.append(0)
    else:
        list1.append(1)
    if lld == False:
        list1.append(0)
    else:
        list1.append(1)
    if rrd == False:
        list1.append(0)
    else:
        list1.append(1)
    if llu == False:
        list1.append(0)
    else:
        list1.append(1)
    if rru == False:
        list1.append(0)
    else:
        list1.append(1)
    return list1

def readListOfDirections(stepNum):
    global luu; global ruu; global ldd; global rdd; global lld; global rrd; global llu; global rru; global possMoves
    currentPossMoves =possMoves[stepNum]
    if currentPossMoves[0] == 1:
        luu = True
    else:
        luu = False
    if currentPossMoves[1] == 1:
        ruu = True
    else:
        ruu = False
    if currentPossMoves[2] == 1:
        ldd = True
    else:
        ldd = False
    if currentPossMoves[3] == 1:
        rdd = True
    else:
        rdd = False
    if currentPossMoves[4] == 1:
        lld = True
    else:
        lld = False
    if currentPossMoves[5] == 1:
        rrd = True
    else:
        rrd = False
    if currentPossMoves[6] == 1:
        llu = True
    else:
        llu = False
    if currentPossMoves[7] == 1:
        rru = True
    else:
        rru = False
    possMoves = possMoves[:-1]
"""
