# Andres Villasmil Ocando
# aev1@williams.edu
# Assignment #5 Hot Dog Contest

import Epic
import random
import time

# defines what qualifies as a winner in the hot dog contest. "else" is for if there's no winner.
def winner(eater1, eater2, eater3): # ties eater name with eater#
    if (eater1 > 50 and eater1 > eater2 and eater1 > eater3):
        return "Tom!"
    elif (eater2 > 50 and eater2 > eater1 and eater2 > eater3):
        return "Sally"
    elif (eater3 > 50 and eater3 > eater1 and eater3 > eater2):
        return "Fred"
    else:
        return ""
            
# this function prints the results at the end of the contest
def print_winner(guess, answer):
    print
    if guess == answer: # if their guess in the beginning is right.
        print "You guessed right, %s won!" % answer
    else:
        print "Sorry, but %s won.." % answer
        
def main():
    answer = ""
    eater1 = 0
    eater2 = 0
    eater3 = 0

    guess = Epic.userStr("Pick a winner (Tom, Sally, or Fred):")
    print "Ready.. Set.. Eat!"
    
    while answer == "": # connects back to winner function
        eater1 = eater1 + random.randrange(1, 6)
        eater2 = eater2 + random.randrange(1, 6)
        eater3 = eater3 + random.randrange(1, 6)
        print
        for x in range(0,3): # print this 3x instead of printing each one word for word
            print "chomp..",
        print
        time.sleep(1) # let 2 secs pass between.
        print
        print "Tom has eaten %s hot dogs." % eater1
        print "Sally has eaten %s hot dogs." % eater2
        print "Fred has eaten %s hot dogs." % eater3
        answer = winner(eater1, eater2, eater3)
        
    print_winner(guess, answer)
    
main()