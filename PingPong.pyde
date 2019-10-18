point_PING=point_PONG=0

def setup():
    fullScreen()
    initGame()
    
def draw():
    global x_PALLA,x_DIR,y_PALLA,y_DIR,SPEED,STEP,point_PING,point_PONG
    background(0,255,0)
    fill(255)

    rect(x_PING,0,100,30)
    rect(x_PONG,height-30,100,30)
    fill(255,0,0)
    textSize(18)
    text(str(point_PING),x_PING+30,20)
    text(str(point_PONG),x_PONG+30,height-10)

    
    x_PALLA+=x_DIR*SPEED
    y_PALLA+=y_DIR*SPEED
 
    if (x_PALLA>width):
        x_DIR=-1
    elif (x_PALLA<0):
        x_DIR=1
        
    if ((x_PALLA-x_PING)<100
            and (y_PALLA-10)<=30):
        y_DIR=1
        SPEED+=0.1
        STEP+=0.1
    elif ((x_PALLA-x_PONG)<100 
              and (y_PALLA+10)>=(height-30)):
        y_DIR=-1
        SPEED+=0.1
        STEP+=0.1
        
    ellipse(x_PALLA,y_PALLA,20,20)

    if (y_PALLA<0):
        point_PONG+=1
        initGame()        
    elif (y_PALLA>height):
        point_PING+=1
        initGame()


def keyPressed():
    global x_PING,x_PONG
    
    if (key=="q"):
        x_PING=max(0,x_PING-STEP)
    elif (key=="w"):
        x_PING=min(x_PING+STEP, width)
    elif (key=="o"):
        x_PONG=max(0,x_PONG-STEP)
    elif (key=="p"):
        x_PONG=min(x_PONG+STEP, width)
        
        
def initGame():
    global x_PING,x_PONG,x_PALLA,y_PALLA,STEP,SPEED,x_DIR,y_DIR,point_PING,point_PONG

    x_PING=x_PONG=0
    x_PALLA=y_PALLA=100
    STEP=10
    SPEED=1
    x_DIR=y_DIR=1
    
