from sys import exit

key = ["No"]

def start():
    print "You are in a dark room. \nThere are two doors."
    print "There is a word on the door1, which says, \"Alive\"."
    print "Door2 has \"dead\" on it. \nWhich one do you take?\nType M for a Map."
    
    choice = raw_input()
    
    if choice == "1":
        alive_room()
    elif choice == "2":
        dead_room()
    elif choice == "M" or choice == "m" :
        helpme()
    else:
        dead("You can't choose the room until you starve.")

def dead(why):
    print why
    exit(0)
    
def alive_room():
    print "Here you see light come out of the room. \nThen you see a code case. "
    print "Do you know the password?"
    
    password = raw_input("Type the password or hit enter to go back \n> ")
    
    if password == "key":
        print "Congratulations! You get the key! \nWhere can we use it? \nLet's go back to find it."
        key[0] = "Yes"
        start()
    elif password == "":
        start()
    else:
        dead("Sorry, wrong password. The code case explode! Game over!")
    
def dead_room():
    print "The half of this room is a pool full of mud and water. \nWith a sign that read, \"Watch out for the crocodile!\""
    print "The other half is a warm road."
    print "Which one do you prefer to pass through?"
    
    while True:   
    
        choice = raw_input("pool or road? \n> ")

        if "pool" in choice:
            print "You are lucky that the crocodile is not there."
            choice_room()
        elif "road" in choice:
            dead("Here comes a huge fireball. You are dead.")        
        else:
            print "I have no idea what that means. Please type pool or road"

def choice_room():
    print "Here you see ten doors in front of you. \nOnly one lead to treasure room."
    
    choice = int(raw_input("Make a choice.\n> "))
    
    if choice == 3:
        print "Amazing! Let's go to the treasure room."
        treasure_room()
    else:
        dead("Sorry, Wrong number. You are dead. Please try again.")

def treasure_room():
    print "There is a locked chest. \nThe key in one room of this world."
    print "If you have the key already, type \"I have the key\". \nIf you don't, hit Enter to go back to start."
    
    while True:
        
        test = raw_input("> ")   
        
        if test == "I have the key" and key[0] == "No":
            print "Sorry. You don't have the key. Go back to start and search for it."
            start()
        elif test == "I have the key" and key[0] == "Yes":
            print "Congratulations! You win!"
            exit(0)
        elif test == "":
            start()
        else:
            print "I have no idea what that means. Please try again."
    

def helpme():
	print """
-----------------------------------------------------------------
|                  |                                            |     
|                  |                  Chest                     |                             
|                  |                                            |     
|                  |                                            |             
|                  |                                            | 
|                  |               Treasure Room                |           
|                  |------------------______---------------------
|    Code Case     |                                            |
|                  |                                            |
|                  |                                            |
|                  |               Choice Room                  |
|                  |------------------______--------------------|
|                  |                    |                       |
|                  |                    |                       |
|                  |                    |                       |
|   Alive Room     |           Pool     |   Road                |
|                  |                    |                       |
|                  |                    |                       |
|                  |                Dead ROOM                   |
------------______---______--------------------------------------
|           Alive    Dead                                       |
|                                                               |                
|                          Dark Room                            |
-----------------------------------------------------------------
                 
		  """
    	start()	
        
        
start()
