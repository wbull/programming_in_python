'''
created on 10/27/12

wtb
'''
#Exercise 9.1
fin = open("words.txt")

def twenty_char_words():
    fin = open("words.txt")
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print word
        
#twenty_char_words()




#Exercise 9.2

#exercise 9.2

def has_no_e(word):
    for i in word:
        if ord(i) == ord("e"):
            #there is an e
            return False        
    return True

#print has_no_e("asdfe")

def words_file_has_e():
    fin = open("words.txt")
    total = 0
    count = 0 
    for line in fin:        
        total = total + 1
        word = line.strip()        
        if has_no_e(word):
            count = count + 1             
    print ((float(count)/total) * 100)

#words_file_has_e()

#Exercise 9.3
def avoids(word, forbid):
    for char in word:
        j = 0
        while j < len(forbid):               
            if forbid[j] == char:
                return False
            j = j + 1
    return True

print avoids("aa","qwera")



def avoids2(word):
    forbid = raw_input("Input forbidden letters and press enter: ")
    j = 0
    length = len(forbid)
    while j <= length: 
        for i in word:        
            if forbid[j] == word[j]:
                return False
        j = j + 1
    return True

#print avoids("asdf","qwer")


#print avoids2("asff")

def check_words_for_forbidden_strings():
    fin = open("words.txt")
    total = 0
    count = 0 
    forbid = raw_input("Input your string of letters to avoid: ")
    for line in fin:        
        total = total + 1
        word = line.strip()
        #print word
        if avoids(word, forbid):
            count = count + 1
            print word
            
    print count

#print check_words_for_forbidden_strings()
 #       
        
        
        
        
        


def is_triple_double(word):
    """Tests if a word contains three consecutive double letters."""
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            count = 0
            i = i + 1
    return False


def find_triple_double():
    """Reads a word list and prints words with triple double letters."""
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print word


#print 'Here are all the words in the list that have'
#print 'three consecutive double letters.'
#find_triple_double()
#print ''

def is_palindrome(word):
    return len(word) < 2 or (word[0] == word[-1] and is_palindrome(word[1:-1]))


def find_ct_number():
    i = 100000
    while i < 1000000:
        #check to see if last 4 digits are palindrome
        string = str(i)
        if is_palindrome(string[2:6]):
            i = i + 1
            string1 = str(i)
            if is_palindrome(string1[1:6]):
                i = i + 1
                string2 = str(i)
                if is_palindrome(string2):
                    print string
        i = i + 1

print find_ct_number()
