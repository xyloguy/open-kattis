def sumDigits(N):
  s = 0
  for char in str(N):
    s += int(char)
  return s

N = input()
while N != 0:
  s = sumDigits(N)
  p = 11
  while sumDigits(N*p) != s:
    p += 1
  print p
  N = input()
