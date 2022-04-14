import random,stddraw,color,math
import sys


def main():

    if(len(sys.argv)!=2):
        print("The number of arguments was not correct. N is set to 5000.")
        print("Please run the script as follows: draw_sierpinski.py 5000")
        N=5000
    else:
        N=int(sys.argv[1])

    stddraw.setXscale(-0.25,1.25)
    stddraw.setYscale(-0.25,0.25+0.5*math.sqrt(3))

    stddraw.line(0,0,1,0)
    stddraw.line(0,0,0.5,0.5*math.sqrt(3))
    stddraw.line(1, 0, 0.5, 0.5 * math.sqrt(3))

    stddraw.setPenColor(color.RED)
    stddraw.filledCircle(0,0,0.025)
    stddraw.setPenColor(color.GREEN)
    stddraw.filledCircle(0.5, 0.5*math.sqrt(3),0.025)
    stddraw.setPenColor( color.BLUE)
    stddraw.filledCircle(1, 0,0.025)

    r=random.randrange(0,3)
    x,y=0,0
    if(r==0):
        x, y = 0, 0
    elif(r==1):
        x, y = 0.5, 0.5*math.sqrt(3)
    else:
        x, y = 1, 0

    for i in range(N):
        r = random.randrange(0, 3)
        if (r == 0):
            stddraw.setPenColor(color.RED)
            x, y = (x+0)/2, (y+0)/2
        elif (r == 1):
            stddraw.setPenColor(color.GREEN)
            x, y = (x+0.5)/2, (y+0.5 * math.sqrt(3))/2
        else:
            stddraw.setPenColor(color.BLUE)
            x, y = (x+1)/2, (y+0)/2


        stddraw.filledPolygon([x-0.005, x, x+0.005], [y-0.005, y+0.01*0.5 * math.sqrt(3), y-0.005])

        # stddraw.filledCircle(x,y,0.01)
        stddraw.show(50)


if __name__=="__main__":
    main()