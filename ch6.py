'''
created on 10/22/12

wtb
'''
#Exercise 6.4

def b(z):
    prod = a(z,z)
    print z, prod
    return prod

def a(x,y):
    x = x + 1
    return x * y

def c(x,y,z):
    total = x + y +z
    square = b(total)**2
    return square
x = 1
y = x + 1
#print c(x, y+3,x+y)

'''
c(1,5,3)
total = 9
b(9) = 90
a(9,9) = 90
90

prints:
9,90
90*90

correct!

'''

def ack(m,n):
    if m == 0:
        return (n + 1)
    if n == 0:
        return ack(m-1,1)
    return ack(m-1,ack(m,n-1))

#number = ack(3,4)
#print number

#Ex 6.6
def first(word,i):
    return word[i]

def last(word,i):
    return word [i]

def middle(word,i):
    return word[i:-i]

#print first("asdf",0)
#print last("qwerty",-1)
#print middle("asb",1)

def is_palindrome(word):
    i = 0
    j = -1
    while i < len(word)/2.0:        
        if(first(word,i) == last(word,j)):
            #print "Compare", first(word,i), " to ", last(word,j)
            i = i + 1
            j = j - 1
    if i == len(word)/2.0:
        return True
    elif(first(word,i) == last(word,j)):
        return True
    else:
        return False
#result = is_palindrome("aibohphobia")
#print result
        
        
#Exercise6.7
'''A number, a, is a power of b if it is divisible by b and a/b is a power of b.
 Write a function called is_power that takes parameters a and b and returns True if a is a power of b. Note: you will have to think about the base case.'''
   
def is_power(a,b):
    if a % b == 0:
        return True
   
i = 0 
def factorial(n):
    i = 0 
    if n == 0:
        return 1
    else:
        i = i + 1
        print i 
        print "n is ", n
        return n * factorial(n-1)
#print factorial(3) 
