vals = {}
v = list(range(1,20001))
for i in range(1,10001):
  a = sum(v[:i])
  b = sum(v[:i*2:2])
  c = sum(v[1:i*2+1:2])
  vals[i] = (a,b,c)
v = []
for _ in range(input()):
  a,b = map(int, raw_input().split())
  s1,s2,s3 = vals[b]
  print a,s1,s2,s3
