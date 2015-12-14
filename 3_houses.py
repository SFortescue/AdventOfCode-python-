total = 0
vert = 0
horiz = 0
position = [
        '0, 0',
]

with open('input3.txt') as f:
    while True:
        c = f.read(1)
        if not c:
            break
        if c == '\n':
            break
        if c == '^':
            vert += 1
        if c == 'v':
            vert -= 1
        if c == '>':
            horiz += 1
        if c == '<':
            horiz -= 1
        string = str(horiz) + "," + str(vert)
        position.append(string)
       
print len(set(position))
