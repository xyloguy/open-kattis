import sys
modulo = set()
for line in sys.stdin:
  line = int(line.rstrip())
  modulo.add(line%42)
print len(modulo)
