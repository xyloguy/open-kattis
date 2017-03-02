try:
  raw_input
except:
  raw_input = input
  
A,B,C,D = map(int, raw_input().split())
arrive = map(int, raw_input().split())

dogs = {k:0 for k in range(1,1000)}
for i in range(1,1000,A+B):
  for j in range(A):
    if i+j in dogs:
      dogs[i+j] += 1

for i in range(1,1000,C+D):
  for j in range(C):
    if i+j in dogs:
      dogs[i+j] += 1

for minute in arrive:
  if dogs[minute] == 2:
    print ('both')
  elif dogs[minute] == 1:
    print ('one')
  else:
    print ('none')
