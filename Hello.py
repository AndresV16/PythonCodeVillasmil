import Epic

sentence = Epic.userStr("Please enter a sentence:")
words = sentence.split(' ')
lgWords = []
smWords = []

for word in words:
    if len(word) > 3:
        lgWords.append(word)
    else: smWords.append(word)

print words
print
print smWords
print
print lgWords