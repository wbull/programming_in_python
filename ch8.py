'''
created on 10/26/12

wtb
'''
#Exercise 8.1

def reverse_string(st):
    length = len(st) - 1
    while length >= 0:
        print st[length]
        length = length - 1
        
#reverse_string("1asl dkjf askdjfpwijep if9")

prefixes = 'JKLMNOPQ'
suffix = 'ack'


#execise 8.2
#for letter in prefixes:
#    if 'Q' in letter or 'O' in letter:
#        print letter + "u" + suffix
#    else:
#        print letter + suffix


#exercise 8.4
def find(word, letter, index):    
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

#print find("fantastic", "s", 3)

#Exercise 8.5
def count(string, letter):
    i = 0    
    count = 0
    while i < len(string):
        if string[i] == letter:
            count = count + 1
        i = i + 1
    print count
    
#Ex 8.6
def count_with_index(string, letter, i): 
    count = 0
    while i < len(string):
        if string[i] == letter:
            count = count + 1
        i = i + 1
    print count
    
#count_with_index("asdfasdfasdf", "a", 3 )

#Exercise 8.7
#help(str.count)
#print "banana".count("a")

#Exercise 8.10
def first(word):
    return word[0]

def last(word):
    return word [-1]

def middle(word):
    return word[1:-1]
word = 'panap'
def is_palindrome(word):
    return len(word) < 2 or (word[0] == word[-1] and is_palindrome(word[1:-1]))

#print is_palindrome("ababa")

#Exercise 8.11

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
#Says whether or not a letter is lowercase 

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
#always returns true--checks on letter c
        


def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
#same as first function

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

#false

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True


#Exercise 8.12
#Exercise 8.12
def rotate_word(string, integer):
    new = ""
    j = 0
    for i in string:
        original = ord(string[j])
        if (original + integer) > 122:
            new = new + chr(((original + integer)-122) + 96)
        if (original + integer) < 97:
            new = new + chr(123 - (97-(original + integer)))
        else:
            new = new + chr(original + integer)
        j = j + 1
    return new

print rotate_word("cheer", 7)
print rotate_word("melon", -10)



                

    



