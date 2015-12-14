nice_words = 0
vowel_count = 0
vowels, double = (False, )*2
special_strings = True
vowels_list = ["a", "e", "i", "o", "u"]
string_list = ["ab", "cd", "pq", "xy"]

with open('input5.txt') as f:
    for line in f:
        vowels, double = (False, )*2
        special_strings = True
        vowel_count = 0
       
        for c in line:
            for v in vowels_list:
                if c == v:
                    vowel_count += 1

        if vowel_count >= 3:
            vowels = True

        for i in range(0, 4):
            if string_list[i] in line:
                special_strings = False

        for i in range(0, 15):
            if line[i] == line[i+1]:
                double = True

        if (vowels == True):
            if (double == True):
                if (special_strings == True):
                    nice_words +=1 

print "Total nice words: " + str(nice_words)
