print("You have come upon a time machine.")
print("Do you use it?")

timeMachine = True
timeMachine1 = False
while timeMachine == True:
    answer = input()
    if (answer == "Yes"):
        timeMachine = False

    elif (answer == "No"):
        print("GAME OVER.")
        print("maybe you should rethink that decision...")
        exit()

    else:
        print("Please type 'Yes' or 'No'.")
    
while timeMachine == False:
    print("You have the choice to go into the Past or the Future. (Past/Future)")
    print("Which one?")
    timePeriod = input()
    
    if timePeriod == "Past":
        timeMachine = True
        print("You have landed in")
        print("Los Angeles, California.")
        print("Date: February 20, 2010")
        print(" As you walk out the time machine, there is  a piece of paper on the ground.")
        print(" Do you pick it up and recycle it or leave it on the ground? (Recycle/Leave it)")
        
        
    elif timePeriod == "Future":
        timeMachine = True
        timeMachine1 = True
        print("You have landed in")
        print("Los Angeles, California.")
        print("Date: February 20, 2020")
        print(" As you walk out of the time machine, you see your future-self.")
        print(" Do you greet your future-self or hide? (Greet/Hide)")
        
    else:
        print("Please type in 'Past' or 'Future'.")
        
while timeMachine1 == True:
    answer3 = input()
    if answer3 == "Greet":
        print("You created a paradox. The time machine is sending you back.")
        exit()

    elif answer3 == "Hide":
        print("Wise choice! You are now able to explore your future.")
        print("After you explored, you are sent back by the time machine.")
        exit()
    else:
        print("Please type 'Greet' or 'Hide'.")
        
        
while timeMachine == True:
    answer2 = input()
    if answer2 == "Recycle":
        timeMachine = False
        print("You inspired a little kid who was watching you while recycling that piece of paper.")
        print("He grew up to become an environmental activist")
        print("who helped others improve the environment.")
        print("Thanks for improving the future!")
        print("The time machine will send you back, now.")
        exit()

    elif answer2 == "Leave it":
        print(" A little kid who was watching you followed your example")
        print(" and contributed to a 400 pounds of trash to the landfill every year.")
        print(" You have negatively influenced the future.")
        print("The time machine will now take you back to prevent you from")
        print(" doing more harm")
        exit()
        
    else:
        print("Please type 'Recycle' or ' Leave it'. ")

   
       
        
        
              
