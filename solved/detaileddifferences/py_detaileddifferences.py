for _ in range(input()):
  a = raw_input()
  b = raw_input()
  s = ''
  for i in range(len(a)):
    if a[i] == b[i]:
      s += '.'
    else:
      s += '*'
  print a
  print b
  print s
  print
