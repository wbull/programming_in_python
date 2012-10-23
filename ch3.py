'''
Created on Oct 13, 2012

@author: wtb
'''
#Exercise 3.3

def right_justify(string):
    for i in range(70):
        string = " " + string
    print string
    
right_justify('allen') 
'''
#Exercise 3.4 
def print_spam():
    print 'spam'

def do_twice(f, arg):
    f(arg)
    f(arg)
    
def print_twice(string):
    print string
    print string
       
do_twice(print_twice, "spam")

def do_four(f,value):
    for i in range(4):
        f(value)
    
do_four(print_twice,"spam")

#Execise 3.5
print "Execise 3.5, Number 1"
def top_mid_bot():
    print "+ - - - - + - - - - +"
def body():
    print "|         |         |"
top_mid_bot()
for i in range(4):
    body()
top_mid_bot()
for i in range(4):
    body()
top_mid_bot()

print "Execise 3.5, Number 2"
def top_mid_bot2():
    print "+ - - - - + - - - - + - - - - + - - - - +"
def body2():
    print "|         |         |         |         |"
top_mid_bot2()
for i in range(4):
    body2()
top_mid_bot2()
for i in range(4):
    body2()
top_mid_bot2()
for i in range(4):
    body2()
top_mid_bot2()
for i in range(4):
    body2()
top_mid_bot2()
'''
    
def make_top(columns):
    for i in range(columns):
        for i in range(9):
            if i == 0:
                print "+",
            if i % 2 == 0 and i !=8:
                print "-",
    print "+"
    
def make_middle(columns):
    for i in range(4):
        for i in range(columns):
            print "|        ",
        print "|"

def make_squares(rows,columns):
    """make_squares takes in the number of rows and columns that you want created in squares.  
    For example if you pass in (4,4) you'll get 4 squares by 4 squares"""
    for i in range(rows):        
        make_top(columns)
        make_middle(columns)            
    make_top(columns)

#print help(make_squares)        
make_squares(4,4)