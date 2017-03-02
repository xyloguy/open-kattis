d1,d2 = map(int, raw_input().split())
rolls = {}
for x in range(1, d1+1):
    for y in range(1, d2+1):
        s = x+y
        if s in rolls:
            rolls[s] += 1
        else:
            rolls[s] = 1
    
most = 0
for roll in rolls:
    if rolls[roll] > most:
        most = rolls[roll]
        
vals = []
for roll in rolls:
    if rolls[roll] == most:
        vals.append(roll)
vals.sort()

for roll in vals:
    print roll
