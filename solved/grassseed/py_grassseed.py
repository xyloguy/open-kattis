C = input()
total = 0.0
for _ in range(input()):
  w,l = map(float, raw_input().split())
  total += w*l*C
print '%.7f'%total
