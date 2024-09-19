text = "ciao ciao come come come stai, spero tutto vada bene bene"
words = text.split()
countWord = {}
for word in words:
    if word in countWord:
        countWord[word] += 1
    else:
        countWord[word] = 1
    

print(countWord)
