n = input()
count = 1
while n != 0:
  l = [raw_input() for i in range(n)]
  i = l[::2]
  j = l[1::2][::-1]
  print 'SET',count
  print '\n'.join(i+j)
  count+=1
  n = input()
