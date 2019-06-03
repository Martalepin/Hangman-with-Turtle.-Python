import random, turtle

lepin = turtle.Turtle()
lepin.color('red')
lepin.pensize(5)
lepin.shape('turtle')


name = "WELCOME TO HANGMAN"
name1 = "THE END"
name2 = "YOU ARE A WINNER"
width = 75

print ("+"*width)
print ("+",name.center(width-4),"+")
print ("+"*width)

select = ["GALILEO", "DAVINCI", "NEWTON", "KEPLER", "HAWKING", "CURIE", "LOVELACE",] #creates an array of options to guess 

word = random.choice(select) #chose a word from "select" to start the game 
alphabet = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z") # to later exclude numbers
letters_in_word = list(word) #makes the letters in "word" as a list

#print (letters_in_word)

current = "*"*len(word) #it creates asterisks with the length of the guessing word
current_list = list(current) 
letters_used = list() # stores and makes the letters used in word as a list

#print ("this is the word to guess", word)

print ("LET US SEE IF YOU CAN GUESS OUR FAVORITE SCIENTIST!!!", current)

lepin.forward(50)
lepin.left(90)
lepin.forward(200)
lepin.right(90)
lepin.forward(150)
lepin.right(90)
lepin.forward(50)

print (" ")

def hangman(lepin): # creates a funtion called hangman

    count = 0
    incorrect = 0
    while count <10: #to give the user ten tries
        x = input("enter your letter: ").upper() #Take user input and make it to upper case always
        count = count + 1 #to control the counting
        guess = x # stores the input of the user

        if guess in word:
            letters_used.append(guess) #attached the letters entered by the user to "letters_used" variable
            

            for position,char in enumerate(letters_in_word):
                if char == guess: 
                    current_list[position] = guess 

            print (current_list) 

        elif (guess not in alphabet):  # to restrict the use of numbers and characters
            print("just letters please")
            incorrect = incorrect + 1
            drawHangman(lepin,incorrect)

        elif (guess not in word): # for letters that are not in the word to guess
            print("Opps! this letter is not in the guessing word")
            incorrect = incorrect + 1
            drawHangman(lepin,incorrect)
          
 
        if (current_list == letters_in_word):  #once the user guess the word
                print("CONGRATS! YOU GET IT!")
                print ("+"*width)
                print ("+",name2.center(width-4),"+")
                print ("+"*width)
                break
            
           
    else:
        print("No more tries!") #message when the user exced the number of tries established on while
        print("Game Over!")
        print ("+"*width)
        print ("+",name1.center(width-4),"+")
        print ("+"*width)
        
def drawHangman(lepin,incorrect):
    
    if incorrect == 1: #head
        lepin.circle(10)
        lepin.penup()
        lepin.forward(10)
        lepin.pendown()
        
    elif incorrect == 2: #body
        lepin.forward(100)
        lepin.penup()
        lepin.right(180)
        lepin.forward(100)
        lepin.pendown()
      

    elif incorrect == 3: #arm
        lepin.left(90)
        lepin.forward(30)
        lepin.penup()
        lepin.right(180)
        lepin.forward(30)
        lepin.pendown()

    elif incorrect == 4: #arm
        lepin.forward(30)
        lepin.penup()
        lepin.left(180)
        lepin.forward(30)
        #coming down for legs
        lepin.left(90)
        lepin.forward(100)
        lepin.left(90)

    elif incorrect == 5: #leg
        lepin.pendown()
        lepin.forward(30)
        lepin.penup()
        lepin.left(180)
        lepin.forward(30)

    elif incorrect == 6: #leg
        lepin.pendown()
        lepin.forward(30)
        print("GAME OVER")
        print ("+"*width)
        print ("+",name1.center(width-4),"+")
        print ("+"*width)
        exit()
         
        
hangman(lepin)
