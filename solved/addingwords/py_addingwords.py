import sys

def aw_define(defs, word, number):
  if word in defs:
    if defs[word] in defs:
      del defs[defs[word]]
    del defs[word]

  if number in defs:
    if defs[number] in defs:
      del defs[defs[number]]
    del defs[number]

  defs[word] = number
  defs[number] = word
  return defs

def aw_is_defined(key, defs):
  return key in defs

def aw_calculate(defs, vals):
  values = vals[0::2]
  opperators = vals[1::2]

  for v in values:
    if not aw_is_defined(v, defs):
      return 'unknown'

  total = defs[values.pop(0)]

  if(len(values) > 0):
    for i in range(len(opperators)):
      if opperators[i] == '-':
        total -= defs[values[i]]
      elif opperators[i] == '+':
        total += defs[values[i]]

  if aw_is_defined(total, defs):
    return defs[total]
  return 'unknown'


defs = {}
for line in sys.stdin.readlines():
  line = line.rstrip()

  if line.startswith('def'):
    action, word, number = line.split()
    defs = aw_define(defs, word, int(number))

  if line.startswith('calc'):
    oline = line[5:]
    vals = oline[:-2].split()
    val = aw_calculate(defs, vals)
    print('%s %s'%(oline,val))

  if line.startswith('clear'):
    defs = {}
