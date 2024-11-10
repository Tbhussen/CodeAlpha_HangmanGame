# -*- coding: utf-8 -*-
"""
@author: Tamim_Hussein
CodeAlpha Python Programing Internship
Task: Hangman

"""
import random

def display(mistakes):
    if mistakes == 7:
        print("""
                 (  $#*  )
                 ---   ---
              (   *     *  )    
            %(       ^      )%      
              (    _____   )
                 (       )
          
          """)
        print("Game Over! You lost...")
    elif mistakes == 6:
        print("""
                 (      )
                 ---   ---
              (   *     *  )    
            %(       ^      )%      
              (    _____   )
                 (       )
          
          """)
        print("You still have 1 life")
    elif mistakes == 5:
         print("""
                  (      )
                  ---
               (   *     *  )    
             %(       ^      )%      
               (    _____   )
                  (       )
           
           """)
         print("You still have 2 lives")
    elif mistakes == 4:
         print("""
                  (      )
                  
               (   *     *  )    
             %(       ^      )%      
               (    _____   )
                  (       )
           
           """)
         print("You still have 3 lives")
    elif mistakes == 3:
         print("""
                  (      )
                  
               (   *     *  )    
             %(       ^      )     
               (    _____   )
                  (       )
           
           """)
         print("You still have 4 lives")  
    elif mistakes == 2:
         print("""
                  (      )
                  
               (   *     *  )    
              (       ^      )      
               (    _____   )
                  (       )
           
           """)
         print("You still have 5 lives")
    elif mistakes == 1:
         print("""
                  (      )
                  
               (   *     *  )    
              (              )      
               (    _____   )
                  (       )
           
           """)
         print("You still have 6 lives")
def GameEndWinner(animal):
    print("I guess that's it you guessed the animal")
    print("The animal was:" + animal)
def GameEndLoser(animal):
    print("Unfortunatly you lost!")
    print("The animal was:" + animal)
def show_current_status(blist, length, wlist):
    for i in range (length):
        if blist[i] == True:
            print(wlist[i] + "|", end = "")
        else:
            print("-|", end = "")
    print()

# opening the file in read mode 
# change to correct path for use
my_file = open("animals.txt", "r") 
  
# reading the file 
data = my_file.read() 
  
# replacing end of line('/n') with ' ' and 
# splitting the text it further when ' ' is seen. 
data_into_list = data.replace('\n', ' ').split(" ") 
my_file.close() 

# choosing a random index
rand = random.randint(0, 971)

# generating a new animal name
animall = data_into_list[rand]
animal = animall.lower()

# defining a list of characters
wlist = list(animal)

# getting animal length
animal_length = len(wlist)

# initialize number of characters known
found_characters = 0

# boolean list to display the characters known
blist = []

# Initialize list containing used letters
used_letters = []

# Initialize the blist with False values
for i in range (animal_length):
    blist.append(False)
    
# initialize the number of mistakes
mistakes = 0

print("Welcome to animal hangman game\nyou are going to play hangman game by the guesing the secret animal name\nYou can only do 6 mistakes!")

for i in range (len(animal)):
    print("-|", end = "")
print()

# main loop
while(True):
    # initialize the number of occurences of the character in the animal word
    nloc = 0
    # initialize ispresent variable to check if the character is present
    ispresent = False
    
    print("Letters used-->", end = "")
    for i in used_letters:
        print(i, end = " ")
    print("<--")
    
    # getting input
    input_letterr = input("Enter a letter: ")
    input_letter = input_letterr.lower()
    used_letters.append(input_letter)
    for i in range(animal_length):
        if input_letter == wlist[i]:
            ispresent = True
            found_characters += 1
            nloc += 1
            blist[i] = True
    if ispresent == False:
        mistakes += 1
        display(mistakes)
        show_current_status(blist, animal_length, wlist)
    else:
        print("Well done!", input_letter, "is present in", nloc, "locations")
        print("You still have", animal_length - found_characters, "spaces to fill")
        show_current_status(blist, animal_length, wlist)
    if animal_length == found_characters:
        GameEndWinner(animal)
        break
    elif mistakes == 7:
        GameEndLoser(animal)
        break
    
