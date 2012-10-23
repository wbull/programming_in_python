'''
created on 10/16/12

wtb
'''

from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
def draw_a(t):
    lt(t,90)
    fd(t,10)
    rt(t,90)
    fd(t,5)
    rt(t,90)
    fd(t,10)
    lt(t,180)
    fd(t,5)
    lt(t,90)
    fd(t,5)
    
draw_a(bob)




wait_for_user()