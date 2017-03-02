def sumints(i):
  t = 0
  for char in str(i):
    t += int(char)
  return t

L = input()
D = input()
X = input()

N = 0
for i in range(L, D+1):
  if N == 0 and sumints(i) == X:
    N = i

  if sumints(i) == X:
    M = i

print N
print M
