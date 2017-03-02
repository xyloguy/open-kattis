l = []
for i in range(input()):
  line = raw_input().split()
  try:
    radius = int(line[0])/2
    color = line[1]
  except:
    radius = int(line[1])
    color = line[0]
  l.append((radius,color))
l.sort()
for cup in l:
  print cup[1]
