print "--- Original Recipe ---"
print "Enter the amount of flour (cups):" ,
flour = raw_input()
print "Enter the amount of water (cups):" ,
water = raw_input()
print "Enter the amount of salt (teaspoons):" ,
salt = raw_input()
print "Enter the amount of yeast (teaspoons):" ,
yeast = raw_input()
print "Enter the loaf adjustment factor (e.g. 2.0 equals double the size:" ,
multiplier = raw_input()
print " "
print "--- Modified Recipe ---"
flour2 = (float(flour))*(int(multiplier))
print "Breadflour: %.2f" % flour2
water2 = (float(water))*(int(multiplier))
print "Water: %.2f" % water2
salt2 = (float(salt))*(int(multiplier))
print "Salt: %.2f" % salt2
yeast2 = (float(yeast))*(int(multiplier))
print "Yeast: %.2f" % yeast2
print "Happy Baking!"