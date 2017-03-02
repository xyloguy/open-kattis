total = 0
for i in range(input()):
    line = raw_input()
    num = line[:-1]
    exp = line[-1]
    total += (int(num)**int(exp))
print total
