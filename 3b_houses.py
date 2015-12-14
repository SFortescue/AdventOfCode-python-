total = 0
santa_vert = 0
santa_horiz = 0
robo_vert = 0
robo_horiz = 0
position = [
        '0, 0',
]

robo_position = [
        '0, 0',
]

robo_or_real = True

with open('input3.txt') as f:
    while True:
        c = f.read(1)
        if not c:
            break
        if c == '\n':
            break
    
        if robo_or_real == True:
            if c == '^':
                santa_vert += 1
            if c == 'v':
                santa_vert -= 1
            if c == '>':
                santa_horiz += 1
            if c == '<':
                santa_horiz -= 1
            string = str(santa_horiz) + "," + str(santa_vert)
            position.append(string)

        else:
            if c == '^':
                robo_vert += 1
            if c == 'v':
                robo_vert -= 1
            if c == '>':
                robo_horiz += 1
            if c == '<':
                robo_horiz -= 1
            string = str(robo_horiz) + "," + str(robo_vert)
            robo_position.append(string)

        robo_or_real = not robo_or_real

mergedlist = position + robo_position

print len(set(mergedlist)) - 1 ##off by one error appears somewhere!

