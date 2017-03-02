cards = raw_input()

T = cards.count('T')
C = cards.count('C')
G = cards.count('G')

total = T**2+C**2+G**2
while T > 0 and C > 0 and G > 0:
  total += 7
  T -= 1
  C -= 1
  G -= 1
print total
