def a(l):
  if l == 1:
    l = 2
  elif l == 2:
    l = 1
  return l

def b(l):
  if l == 2:
    l = 3
  elif l == 3:
    l = 2
  return l

def c(l):
  if l == 1:
    l = 3
  elif l == 3:
    l = 1
  return l

l = 1
for char in raw_input():
  if char == 'A':
    l = a(l)
  elif char == 'B':
    l = b(l)
  elif char == 'C':
    l = c(l)
print l
