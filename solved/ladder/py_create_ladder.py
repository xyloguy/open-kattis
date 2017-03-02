import random, sys

if(len(sys.argv) == 2):
  N = int(sys.argv[1])
else:
  N = random.randint(1,1000)
  
if N > 1000:
  N = 1000
elif N < 1:
  N = 1

print(N)
for _ in range(N):
  h = random.randint(1,10000)
  a = random.randint(1,89)
  print('%d %d'%(h,a))
