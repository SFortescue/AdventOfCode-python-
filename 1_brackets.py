
f = open('input.txt', 'r')

left_bracket = 0
right_bracket = 0

while True:
    char = f.read(1)
    if not char: break
    if char == "(":
        left_bracket += 1
    if char == ")":
        right_bracket += 1

print "Total left: %d" % left_bracket
print "Total right: %d" % right_bracket

print "Left - Right = %d" % (left_bracket - right_bracket)
