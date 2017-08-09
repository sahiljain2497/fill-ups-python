print "Welcome to my first quiz"
print
#this fucntion helps the user to select the data required for the selected input
def selection(level):
    paragraph = game_data[level]['paragraph']
    answers = game_data[level]['answers']
    return paragraph,answers
#finds words that match in the paragraph
def word_in_pos(word, parts_changed):
    for pos in parts_changed:
        if pos in word:
            return pos
    return None 
#asks users to enter the answer and makes replacement accordingly
#split function returns the list of all the words used in the string    
#replace function used replaced the string we need to change
#append function stored the new word in the string
def game(paragraph, parts_changed,answers):    
    print
    print paragraph
    print
    i=0
    edited = paragraph
    count=0
    limit=5
    replaced = []
    paragraph = paragraph.split()
    for word in paragraph:
        replacement = word_in_pos(word, parts_changed)
        if replacement != None:
            while i<limit:
                user_input = raw_input("Type in: " + replacement + " ")
                if user_input!=answers[count]:
                    i=i+1
                    print "try again"    
                else:
                    paragraph = str(paragraph)
                    edited = edited.replace(replacement, user_input)    
                    print edited                                    
                    break
            count+=1
            word = word.replace(replacement, user_input)
            replaced.append(word)
        else:
            replaced.append(word)
    if i==limit:
        print "You failed"
    else:
        replaced = " ".join(replaced)
        print
        print "Ok, lets see your results."
        print       
        print replaced

while True:
    #List of words to be replaced
    parts_changed = ["_Word1_", "_Word2_", "_Word3_", "_Word4_"]

    #DATA FOR THE QUESTIONS AND THEIR ANSWERS
    game_data={
        'easy':{
        'paragraph':"HTML is short for _Word1_ Markup Language. HTML is used to create electronic documents called _Word2_ that are displayed on the World Wide Web. Each page contains a series of connections to other pages called _Word3_.HTML provides a structure of the page, upon which _Word4_ Style Sheets are used to change its appearance.",
        'answers':['hypertext','webpages','hyperlinks','cascading']
                },
        'medium':{
        'paragraph':"Java is a general purpose, high-level programming language developed by _Word1_ Java was originally called _Word2_ and was designed for handheld devices .Java is an _Word3_ language similar to C++. Java source code files are compiled into a format called _Word4_ (.class extension).",
        'answers':['sun microsystems','OAK','object-oriented','bytecodes']
                 },
        'hard':{
        'paragraph':" This type of loop will continue to run as long as it is true: _Word1_. When using a comparison this is used to say not equal to : _Word2_ .Creating a _Word3_ also creates certain methods inside it. When creating a function you may have to pass : _Word4_",
        'answers':['while','!','class','argument']   
               }    
        }
    level= raw_input("Which difficulty level would you like? Type EASY, MEDIUM or HARD to continue? ")
    while level.lower()!="easy" and level.lower()!="medium" and level.lower()!="hard":
        print "Sorry wrong choice!try again."
        level= raw_input("Which difficulty level would you like? Type EASY, MEDIUM or HARD to continue? ")
    paragraph,answers = selection(level.lower())
    game(paragraph, parts_changed,answers)
    print
    choice=raw_input("If you don't want to play again press N else press Enter")
    if choice.upper()=="N":
        break
