nice_words = 0
letter_repeat = False
letter_between = False

with open('input5.txt') as f:
    for line in f:
        letter_repeat = False
        letter_between = False
        
        for i in range(0, 15):
            if line.count(line[i]) >= 2:
                j = line.find(line[i:i+2], i+2)
                if j == -1:
                    continue
                else:
                    letter_repeat = True
        
        for i in range(0, 14):
            if line.count(line[i]) >= 2:
                if line[i] == line[i+2]:
                    letter_between = True

        if letter_repeat == True:
            if letter_between == True:
                nice_words +=1 

print "Total nice words: " + str(nice_words)
