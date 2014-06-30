

# First python program. 
# python 3.4

import string
import random
import time

print ("\tHangman")
time.sleep(.5)

def play():
     random.shuffle(difficulty)
     random.shuffle(difficulty)
     word = difficulty[0]# first word in shuffle
     print (word)
     for i in range (0, len(word)):
         print(" __ ",end=" ")#end=" " prints it on one line
     print ("\npick a letter")
     print (len(word))   
     lives = 6
     Used_letter = list()
     Correct_letter = list()
     Correct = 0
     print ("\nlives remaining:",lives)
     while lives > 0:
        count = 0
        Play_input = input("Player: ").lower()
        for a in range (0,len(Used_letter)):
            if Play_input == Used_letter[a]:
                print ("You already guessed that letter")
                break
        
        for i in range (0, len(word)):
            count = count + 1
            print (len(word[i]))
            if (Play_input == word[i]): 
                Correct_letter.append(word[i])
                Used_letter.append(word[i])
                break
            elif count == len(word): 
                lives = lives - 1
                Used_letter.append(Play_input)
                print ("lives remaining:",lives)
        print ("Letters guessed: ",Used_letter)
        for char in word:
             if char in Correct_letter:
                  print (char,end=" ")
                  Correct= Correct+1
                  print (Correct)
             else:
                  print ("__",end=" ")
        if  (len(Correct_letter)) == len(word):#it won't recogonize Bubbles b's as 3 b but 1 b. thus the count is wrong.
             print ("Congradualations, You Win!!!")
             break
     if lives == 0:
        print ("You lose, The correct word was: ",word," \n\t Game over")

def options():
        print("""
               press "E" for Easy
               press "N" for  Normal
               press "H" for Hard
             """)
        Option_input = input("Player: ").lower()
        if Option_input == "e":
            Easy = ["bubbles"]#,"spin","happy","class","pain","bear"
            difficulty = Easy
            return difficulty
        elif Option_input == "n":
            Normal = ["mountain","teacher","police","monster"]
            difficulty = Normal
            return difficulty
        elif Option_input == "h":
            Hard = ["dermatologist","interview","sphinx","depreciate","indecisive","bandwagon","gazebo","comprehension"]
            difficulty = Hard
            return difficulty
        else:
            print ("invalid choice")

Normal = ["mountain","teacher","police"]
difficulty = Normal #default difficulty
Main_input = True
while Main_input:
    print("""
    press "P" to play
    press "O" for options
    press "Q" to quit
    """)
    Main_input = input("Player: ")
    if Main_input.lower() == "p":
        play()
    elif Main_input.lower() == "o":
        difficulty = options() # how to pass difficulty to main function
    elif Main_input.lower() == "q":
        break
    else:
        print ("invalid choice")
K = input("Press Enter")

