import md5

found = False
puzzle_input = "yzbqklnj"

for i in range(1, 999999):
    input = puzzle_input + str(i)
    m = md5.new(input).hexdigest()
                                    ##For Part 2, increase range
    if ("00000" in m[:5]):          ##add extra zero, increment 5 to 6 here
        print "Found!"
        print "Hex Digest: " + m
        print "Input: " + input
        found = True

if (found == False):
    print "No matches found!"
