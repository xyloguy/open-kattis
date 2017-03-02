xlist = []
ylist = []
for i in range(3):
  x,y = map(int, raw_input().split())
  xlist.append(x)
  ylist.append(y)

for x in xlist:
  if xlist.count(x) == 1:
    break

for y in ylist:
  if ylist.count(y) == 1:
    break

print x,y
