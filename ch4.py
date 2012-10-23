'''
created on 10/16/12

wtb
'''

from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
#Exercise 1
def square(t):
    for i in range(4):
        fd(t,100)
        lt(t)
        
#square(bob)


def square_and_length(t, length):
     for i in range(4):
        fd(t,length)
        lt(t)
        
#square_and_length(bob, 55)

def polygon(t, n, length):
    """Polygon takes three arguments, turtle, sides, and length.  It then uses a pen-wielding turtle to draw a polygon with n sides."""
    angle = 360.0/n
    for i in range(n):
        fd(t,length)
        lt(t,angle)

bob.delay = (0.001)
#polygon(bob,100,3)
import math

bob.delay = (0.01)
def circle(t,r):
    """"The function circle takes a turtle and a radius and has the turtle draw a circle with radius r."""
    circum = 2 * math.pi * r
    n = int(circum/3)+1
    length = circum / n
    polygon(t,n,length)

#circle(bob, 12)

def arc(t,r,angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length/3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    
    for i in range(n):
        fd(t, step_length)
        lt(t,step_angle)
            
#arc(bob,12,90)

def polyline(t, n, length, angle):
    for i in range(n):
        fd(t,length)
        lt(t,angle)

def polygon2(t,n,length):
    angle = 360 / n
    polyline(t,n,length,angle)
 
#polygon2(bob,6,45)

def arc2(t,r,angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3)
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t,n, step_length, step_angle)
    
#arc2(bob,60,180) 

def circle2(t,r):
    arc2(t,r,360)

#circle2(bob,80)

#Exercise 4.2
#Create functions to draw flowers...
def petal(t,r,angle):
    for i in range(2):
        arc2(t,r,angle)
        lt(t,180-angle)
#petal(bob,80,60)
def flower1(t,length,petals):
    for i in range(petals):
        petal(bob,length,360.0/petals)
        lt(t, 360.0/petals)
#flower1(bob,80, 7)

def flower2(t,length,petals):
    flower1(t,length ,5)
    lt(t, 360/(petals/2))
    flower1(t, length,5)

#flower2(bob, 80,5)
#flower 3 just calls flower1 20x
#flower1(bob,240,20)        

def polypie(t, n, r):
    """Draws a pie divided into radial segments.

    t: Turtle
    n: number of segments
    r: length of the radial spokes
    """
    angle = 360.0 / n
    for i in range(n):
        isosceles(t, r, angle/2)
        lt(t, angle)


def isosceles(t, r, angle):
    """Draws an icosceles triangle.

    The turtle starts and ends at the peak, facing the middle of the base.

    t: Turtle
    r: length of the equal legs
    angle: peak angle in degrees
    """
    y = r * math.sin(angle * math.pi / 180)

    rt(t, angle)
    fd(t, r)
    lt(t, 90+angle)
    fd(t, 2*y)
    lt(t, 90+angle)
    fd(t, r)
    lt(t, 180-angle)


#polypie(bob,5,55)   
#polypie(bob,7,55)      

        
def pie2(t,slices):
    lt(t,90)
    for i in range(slices):
        polygon(t,3,45)
        lt(t,360/slices)
#pie2(bob,6)


def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)
    
draw(bob,5,7)


wait_for_user() 