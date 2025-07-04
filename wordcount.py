Paragraph = "hi how are you how old are you how are you doing" 
count = input("Enter a word to count in the paragraph: ")

wordsToCount= Paragraph.split()   
#print(wordsToCount[0])
word_count = 0  
for word in wordsToCount:
    if word == count: 
    
        word_count = word_count + 1 
else:
    print ("the word is not present")
print(word_count)