A,B,C = map(int, raw_input().split())

if A+B==C:
  O = '+'
  print '%s+%s=%s' % (A,B,C)

elif A==B+C:
  O = '+'
  print '%s=%s+%s' % (A,B,C)

elif A-B==C:
  O = '-'
  print '%s-%s=%s' % (A,B,C)

elif A==B-C:
  O = '-'
  print '%s=%s-%s' % (A,B,C)

elif A*B==C:
  O = '*'
  print '%s*%s=%s' % (A,B,C)

elif A==B*C:
  O = '*'
  print '%s=%s*%s' % (A,B,C)

elif A/B==C:
  O = '/'
  print '%s/%s=%s' % (A,B,C)

elif A==B/C:
  O = '/'
  print '%s=%s/%s' % (A,B,C)
