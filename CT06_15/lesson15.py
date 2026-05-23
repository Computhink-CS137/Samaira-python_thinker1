import turtle 
## drawing libbrary = turtle
## to draw must connect to other platforms
window = turtle.Screen()
#window.setup(1920, 1080)
##measuered in pixels, 1920 & 1080 are the standerd full screen sizes(so, these generally = full screen)
# creating turtle(drawing)
#functions have empty barcets at the end
#turtle = pen(mouse on screen)
# just like scratch pen function(pen up/ pen down)
t = turtle.Turtle()
t.seth(0)
# the exact starting direction
# seth = direction(like point in direction (-) in scratch
# ) 0 degrees is the right side, go up = 90 degrees, go left = 180 degrees, 
# go down = 270 degrees
# start at seth 0 so going towards the right
t.pendown()
t.speed(0)
#10 = fastest and 1 = slowest
# 0 speed = bounus (actual fastest)
#t.color("#16e3b091")
#for j in range(36):
    # 36 and the turn right ten, all multiply to 360, thats why it ends up in a circular pattern,
    # can use and 2 multiple factors of 360
    #for i in range(4):
        #t.forward(90)
        #t.left(90)
    #t.right(10) 
 
    # to make a shape ; interior angle - 180(total on a staright line)
# turn 90 degrees left
# for circle ; a circle has infanite sides but since 360 degrees, assume 360
# sides, and turn 1 degree eacg time.
# NESTED LOOPS = LOOPS INSIDE LOOPS 
# STAR = 5, 144
# turn 144 degrees each time, and 5 sided star
colours = ["red", "purple", "blue", "green", "yellow", "orange"]
length = 5
for i in range(30):
    for colour in colours:
        t.color(colour)
        t.forward(length)
        t.right(145)
        # inside turn right is the angle of your shape eg.(star ; 144) then + 1 to put the whole figure tilted slighly
        length += 3
turtle.done()