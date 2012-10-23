'''
created on 10/16/12

wtb
'''

#Exercise 5.3 Check fermat



def check_fermat(a,b,c,n):
    a = a**n
    b = b**n
    c = c**n
    if a + b == c:
        print "Holy smokes, Fermat was wrong!"
        #print "a^", n + "b^",n,"is equal to ", "c^",n
    else:
        print "No, that doesn't work."

#check_fermat(2,3,4,3)


def get_fermat_numbers():
    a = raw_input("Please input a\n")
    b = raw_input("Please input b\n")
    c = raw_input("Please input c\n")
    n = raw_input("Please input n\n")
    a = int(a)
    b = int(b)
    c = int(c)
    n = int(n)
    check_fermat(a,b,c,n)

#get_fermat_numbers()



############################
#Exercise 4

def is_triangle():
    a = raw_input("Input side one please...\n")
    b = raw_input("Input side two please...\n")
    c = raw_input("Input side three please...\n")
    a =int(a)
    b=int(b)
    c=int(c)
    if (a > b + c):
        print "This cannot be a triangle, side a is longer than b + c."
    elif(b > (a + c)):
        print "This cannot be a triangle, side b is longer than a + c."
    elif(c > a + b):
        print "This cannot be a triangle, side c is longer than a + b."
    else:
        print"You can make a triangle with these sides!"

#is_triangle()

###################################
#Exercise 5
from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
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
#Pass in a turtle, a lenght, and n.
#If n is 0, dont' do anything
#Otherwise...take n steps that are length long
#Then take a left turn
#Call draw again
##if n is zero peace out.
##Other 


#draw(bob,5,5)
bob.delay = .001

#Exercise 5.6
#draw koch curve

def koch(t,length):
    if length < 3:
        fd(t,length)
        return
    koch(t,length/3.0)
    lt(t,60)
    koch(t,length/3.0)
    rt(t,120)
    koch(t,length/3.0)
    lt(t,60)
    koch(t,length/3.0)
 
#koch(bob,1800)

def snowflake(t,length):
    for i in range(3):
        koch(t,length)
        rt(t,120)

snowflake(bob,250)


