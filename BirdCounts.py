# Andres Villasmil Ocando
# aev1@williams.edu
# Assignment 4: Bird Counts

# going to use user string after prompt
import Epic

# make an open dictionary
d = {}
for line in open("birds.txt"):
    temp = line.split(",") # split by a comma
    birds = temp[0].strip()
    sightings = int(temp[1].strip()) # integer value of sightings
    if birds in d:
        d[birds] = d[birds] + sightings # add number of sightings if it already exists
    else:
        d[birds] = sightings # make that number the number of sightings

n = Epic.userStr("Enter a bird name:") # entering user's prompt

# what the user wants to read.
if n in d:
    print "I've seen that bird %s time(s)." % d[n]
else:
    print "I've seen that bird 0 time(s)."