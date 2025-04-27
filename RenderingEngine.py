import random
import time
import sys
import keyboard
import math

# Startup
Dev=input("Dev Code? (Press Enter)")
if Dev=="1":
    cheats=True
else:
    cheats=False
validate=0
if cheats==False and Dev!="2":
    for i in "Install Keyboard Commands ('pip install keyboard' in Teminal)0Controls:0A = Left0D = Right0Space = Jump0":
            if i=="0":
                print("")
            else:
                print(i, end="", flush=True)
                time.sleep(0.02)
    input("(Press Enter)")
    for i in "Fullscreen Only0Performance is IDE Dependent0Reccomended FOV is 6Ox3O0Recommended FPS is 2O0":
            if i=="0":
                print("")
            else:
                print(i, end="", flush=True)
                time.sleep(0.02)
    input("(Press Enter)")
    while validate==0:
        displayX=input("Screen Width? (10-80) ")
        displayY=input("Screen Height? (10-30) ")
        framerate=input("Frame Rate? (5-50) ")
        if displayX.isdigit() and displayY.isdigit() and framerate.isdigit():
            displayX=int(displayX)
            displayY=int(displayY)
            framerate=int(framerate)
            if displayX>80 or displayX<10 or displayY>30 or displayY<10 or framerate>50 or framerate<5:
                print("Invalid! Out of Range")
            else:
                validate=1
        else:
            print("Invalid! Enter Numbers Only")
    print(displayX*displayY*framerate,"Pixels/S")
    input("Press Enter to Start...")
else:
    displayX=60
    displayY=30
    framerate=20

# Modifiables
idle=True
gameOn=True
fakeVariable=True

# Frame Rate Calculator
frameExecute=1
time1=time.perf_counter()
def calculateFPS():
    global time3 
    global time1
    global frameExecute
    time2=time.perf_counter()
    time3=time2-time1
    if (1/framerate) <= time3:
        time1=time.perf_counter()
        frameExecute=1

# Rendering Translator
def update_render(x_coord, y_coord, pixel):
    if 0 <= x_coord < displayX and 0 <= y_coord < displayY:
        y_row = displayY - y_coord - 1
        x_col = x_coord
        output = (displayX * y_row) + x_col
        display[output][0] = pixel[0]
        display[output][1] = pixel[1]
        display[output][2] = pixel[2]

# Reverse Translator
def reverse_render(index):
    index=int(index)
    y_row = index // displayX  
    x_col = index % displayX  
    y_coord = displayY - 1 - y_row  
    x_coord = x_col  
    return (x_coord, y_coord)

# Generates Default Display
pixel=[72,111,56]
print(str(displayX)+"x"+str(displayY), "Display")
display=[]
i=0
while i<displayX*displayY:
    display.append(pixel.copy())
    i=i+1

# Rendering Engine
def Render_Frame():
    global frameExecute
    if frameExecute==1:
        sys.stdout.write("\033[2J\033[H")
        sys.stdout.flush()
        v=0
        for i in display:
            r,g,b=i[0],i[1],i[2]
            v=v+1
            print(f"\033[38;2;{r};{g};{b}m{"\u2588"}\033[0m", end="")
            print(f"\033[38;2;{r};{g};{b}m{"\u2588"}\033[0m", end="")
            if v==displayX:
                print("")
                v=0
        frameExecute=0

# Put Active Game Logic Here
while gameOn==True:

    # Generates Border
    j=0
    for i in display:
        x,y=reverse_render(j)
        if y==0 or y==displayY-1 or x==0 or x==displayX-1:
            pixel=[65,65,65]
            update_render(x,y,pixel)
        j=j+1

    # Code runs constantly, Render_Frame is only called (framerate) times a second

    # If you add physics, create a seperate constant physics FPS so that they dont speed up based on framerate

    # Call update_render(x,y,pixel) to generate a pixel at that location. Bottom left corner is 0,0. Must input
    # integers for x and y. Pixel is [r,g,b] where they are all integers. The order from top to bottom update_render
    # is called defines layer order. Furthest down update_render gets rendered on top. Reverse_render gives an x and
    # y coordinate for a given index of (display). To do movement, render pixels at a variable and then move the
    # variable to move where the pixels are rendered. 

    Render_Frame()
    calculateFPS()


