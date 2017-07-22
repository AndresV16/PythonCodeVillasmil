# Andres Villasmil Ocando
# aev1@williams.edu
# Temperature Analytics Assignment

# read temp file and make a list from numbers
def readTemp():
    file = open("temp.txt")
    temps = []
    for line in file:
        temps.append(float(line))
    return temps

# calulate avg number between start and stop
def calculateAve(temps, start, stop):
    index = 0
    total = 0.0 # can't use "0" bc invalid syntax. change to "0.0" to make a floating num.
    for temp in temps:
        if (index >= start and index < stop):
            total = total + temp
        index = index + 1
    return total/(start-stop)

# count all numbers w positive deviation between start and stop
def count(temps, start, stop):
    index = 0
    c = 0
    for temp in temps:
        if (index >= start and index < stop):
            if temp > 0:
                c = c + 1
        index = index + 1
    return c
    
# main function
# data downloaded from NASA Climate site
# data represents deviations in global surface temp

def main():
    temps = readTemp()
    block1 = int(len(temps)*.70) # first block is integer value of where the first 70% of the data is. Will read as "during the first 'block1' years..""
    avg1 = calculateAve(temps, 0, block1) # average dev. between first value and 70% value
    dev1 = count(temps, 0, block1) # counting all value w positive deviation between first and 70% value
    avg2 = calculateAve(temps, block1, len(temps))
    dev2 = count(temps, block1, len(temps))
    print "During the first %s years, average deviation from temperature anomaly is %s." % (block1, avg1)
    print "During the first %s years, %s of them had a positive deviation." % (block1, dev1)
    print "During the last %s years, average deviation from temperature anomaly is %s." % (len(temps)-block1, avg2)
    # len(temps) - block1 = integer value of total - block1
    print "During the last %s years, %s of them had a positive deviation." % (len(temps)-block1, dev2)
    
main()