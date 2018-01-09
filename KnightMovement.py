luu= False;ruu= False;ldd= False;rdd= False;lld= False;rrd= False;llu= False;rru = False

xPos = [];yPos=[]; moves = []; possMoves = []

def setDirections():
    global luu; global ruu; global ldd; global rdd; global lld; global rrd; global llu; global rru
    luu= False;ruu= False;ldd= False;rdd= False;lld= False;rrd= False;llu= False;rru = False #sets all direction movement to false (will be changed to true if knight can move in any direction)



def setMoves(x,y):
    global luu; global ruu; global ldd;global rdd; global lld; global rrd; global llu; global rru 
    setDirections()
    #left one, up/down two
    if x-1>0:
        if y-2>0:
            ldd = True
        if y+2<=8:
            luu = True
    #right one, up/down two
    if x+1<=8:
        if y-2>0:
            rdd = True
        if y+2<=8:
            ruu = True
    #left two, up/down one
    if x-2>0:
        if y-1>0:
            lld = True
        if y+1<=8:
            llu = True
    #right two, up/down one
    if x+2<=8:
        if y-1>0:
            rrd = True
        if y+1<=8:
            rru = True
'''
def checkNumMoves(x,y):                                 #UNNECESSARY CODE?
    m=0
    #left one, up/down two
    if x-1>0:
        if y-2>0:
            m=m+1
        if y+2<=8:
            m=m+1
    #right one, up/down two
    if x+1<8:
        if y-2>0:
            m=m+1
        if y+2<=8:
            m=m+1
    #left two, up/down one
    if x-2>0:
        if y-1>0:
            m=m+1
        if y+1<=8:
            m=m+1
    #right two, up/down one
    if x+2<=8:
        if y-1>0:
            m=m+1
        if y+1<=8:
            m=m+1
    return m
'''
def move():
    global x; global y; global moves
    if ldd == True and (len(moves) == 0 or moves[len(moves)-1]!= "ruu"):
        moves.append("ldd")
        x-=1;y-=2
    elif rdd == True and (len(moves) == 0 or moves[len(moves)-1]!= "luu"):
        moves.append("rdd")
        x+=1;y-=2
    elif lld == True and (len(moves) == 0 or moves[len(moves)-1]!= "rru"):
        moves.append("lld")
        x-=2;y-=1
    elif rrd == True and (len(moves) == 0 or moves[len(moves)-1]!= "llu"):
        moves.append("rrd")
        x+=2;y-=1
    elif luu == True and (len(moves) == 0 or moves[len(moves)-1]!= "rdd"):
        moves.append("luu")
        x-=1;y+=2
    elif ruu == True and (len(moves) == 0 or moves[len(moves)-1]!= "ldd"):
        moves.append("ruu")
        x+=1;y+=2
    elif llu == True and (len(moves) == 0 or moves[len(moves)-1]!= "rrd"):
        moves.append("llu")
        x-=2;y+=1
    elif rru == True and (len(moves) == 0 or moves[len(moves)-1]!= "lld"):
        moves.append("rru")
        x+=2;y+=1
        
def makeLastMoveFalse():
    global luu; global ruu; global ldd;global rdd; global lld; global rrd; global llu; global rru; global moves
    if moves[len(moves)-1] == "ldd":
        ldd = False
    elif moves[len(moves)-1] == "rdd":
        rdd = False
    elif moves[len(moves)-1] == "lld":
        lld = False
    elif moves[len(moves)-1] == "rrd":
        rrd = False
    elif moves[len(moves)-1] == "luu":
        luu = False
    elif moves[len(moves)-1] == "ruu":
        ruu = False
    elif moves[len(moves)-1] == "llu":
        llu = False
    elif moves[len(moves)-1] == "rru":
        rru = False
    moves = moves [:-1]

def checkIfAllDirectionsFalse():
    global luu; global ruu; global ldd;global rdd; global lld; global rrd; global llu; global rru
    if luu==False and ruu==False and ldd==False and rdd==False and lld==False and rrd==False and llu==False and rru==False:
        return True
    else:
        return False

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
    if possMoves[stepNum][0] == 1:
        luu = True
    else:
        luu = False
    if possMoves[stepNum][1] == 1:
        ruu = True
    else:
        ruu = False
    if possMoves[stepNum][2] == 1:
        ldd = True
    else:
        ldd = False
    if possMoves[stepNum][3] == 1:
        rdd = True
    else:
        rdd = False
    if possMoves[stepNum][4] == 1:
        lld = True
    else:
        lld = False
    if possMoves[stepNum][5] == 1:
        rrd = True
    else:
        rrd = False
    if possMoves[stepNum][6] == 1:
        llu = True
    else:
        llu = False
    if possMoves[stepNum][7] == 1:
        rru = True
    else:
        rru = False
    possMoves = possMoves[:-1]

def checkForRepeatLocation(x,y):
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

def moveOneStepBack():
    global x; global y; global xPos; global yPos
    x=xPos[len(xPos)-2]
    y=yPos[len(yPos)-2]
    xPos = xPos[:-1]
    yPos = yPos[:-1]
    stepNum = len(xPos)
    readListOfDirections(stepNum)
    makeLastMoveFalse()
    possMoves.append(makeListOfDirections())

    

skipSetMoves = False
origX = 4; origY = 5
x=origX; y=origY
setMoves(x,y)
possMoves.append(makeListOfDirections())
move()
xPos.append(x)
yPos.append(y)
setDirections()
setMoves(x,y)

    
while x!=origX or y!=origY:
    while not checkForRepeatLocation(x,y) and not checkIfAllDirectionsFalse():
        if not skipSetMoves:
            setMoves(x,y)
            possMoves.append(makeListOfDirections())
        skipSetMoves = False
        move()
        xPos.append(x)
        yPos.append(y)
        print(x,y)

    if checkForRepeatLocation(x,y):
        print ("\u290A Been Here Before")
    else:
        print ("Hit dead end")
    moveOneStepBack()        
    skipSetMoves = True

'''        
skipSetMoves = False
origX = 4; origY = 5
x=origX+1; y=origY+1
setMoves(x,y)
while x!=origX or y!=origY:
    if checkIfAllDirectionsFalse():
        x=xPos[len(xPos)-1]
        y=yPos[len(yPos)-1]
        xPos=xPos[:-1]
        yPos=yPos[:-1]
    if not skipSetMoves:
        setMoves(x,y)
    skipSetMoves=False
    move()
    if not checkForRepeatLocation(x,y):
        xPos.append(x);yPos.append(y)
        setDirections()
        print(x,y)

    else:
        makeLastMoveFalse()
        skipSetMoves = True
        x=xPos[len(xPos)-1]
        y=yPos[len(yPos)-1]
'''        
