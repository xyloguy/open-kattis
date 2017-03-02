import math
try:
  raw_input
except:
  raw_input = input
for _ in range(int(raw_input())):
  opposite,angle = map(int, raw_input().split())
  angle = math.radians(angle)
  sine = math.sin(angle)
  hypotenuse = opposite/sine
  print(int(math.ceil(hypotenuse)))
