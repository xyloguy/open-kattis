d = {
  'A':11,
  'K':4,
  'Q':3,
  'J':20,
  'T':10,
  '9':14,
  '8':0,
  '7':0
}

n = {
  'A':11,
  'K':4,
  'Q':3,
  'J':2,
  'T':10,
  '9':0,
  '8':0,
  '7':0
}

N,B = raw_input().split()
N = int(N)

total = 0

for i in range(4*N):
  c = raw_input()
  if c[1] == B:
    total += d[c[0]]
  else:
    total += n[c[0]]

print total
