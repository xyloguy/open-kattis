i = input()
while i != -1:
  total = 0
  thours = 0
  for _ in range(i):
    miles, hours = map(int, raw_input().split())
    total += miles*(hours-thours)
    thours += hours-thours
  print total, 'miles'
  i = input()
