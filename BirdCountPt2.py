# Andres Villasmil Ocando
# aev1@williams.edu
# Assignment 4: Bird Counts

# going to ask user for a string
import Epic

# ------------------------------------------------------------
# Reads the specified file (filename) and returns a dictionary 
# whose keys are bird names and whose values are the number of 
# times the bird has been seen.
# ------------------------------------------------------------
def countBirds():
    d = {}
    for line in open("birds.txt"):
        temp = line.split(",")
        bird = temp[0].strip()
        sightings = int(temp[1].strip())
        if bird in d:
            d[bird] = d[bird] + sightings
        else:
            d[bird] = sightings
            
    print "%s -> %s" % (d.keys(), d.values())

# ------------------------------------------------------------
# Asks the user to enter a bird name and then looks up 
# the sighting count for that bird in the specified 
# dictionary (d).
# ------------------------------------------------------------
def askUser():
    d = {}
    for line in open("birds.txt"):
        temp = line.split(",")
        bird = temp[0].strip()
        sightings = int(temp[1].strip())
        if bird in d:
            d[bird] = d[bird] + sightings
        else:
            d[bird] = sightings
            
    bird = Epic.userStr("Enter a bird name:")
    if bird in d:
        return d[bird]
        
def main():
    print countBirds()
    print
    print askUser()
    
main()