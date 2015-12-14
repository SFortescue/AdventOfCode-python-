
total = 0

with open('input2.txt') as f:
    for line in f:
        if line == '\n':
            break
        line = line.rstrip()
        num = line.split("x")
        num = [int(i) for i in num]
        num.sort()
        total += (2*num[0]*num[1] + 2*num[1]*num[2] + 2*num[0]*num[2] + num[0]*num[1])

print total
