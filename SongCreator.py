import Epic


song = [];

verse1 = Epic.userStr("Enter the first verse here:")
verse2 = Epic.userStr("Enter the second verse here:")
verse3 = Epic.userStr("Enter the third verse here:")
verse4 = Epic.userStr("Enter the fourth verse here:")

chorus = Epic.userStr("Enter the chorus:")
chorusrep = Epic.userInt("Enter the chourus repeat:")
print

v = [verse1, verse2, verse3, verse4]
for x in v:
    song.append(x)
    song.append(chorus*chorusrep)
song.append(chorus) 

song = (song*2)
song.insert(8,"...one more time!...")

print song
print

for line in song:
    print line