# slightly faster than v1, uses less memory
# submission size smaller as well.
# The only difference is I only kept a single
# equation for each valid solution.
d = {0: '4 / 4 * 4 - 4 = 0', 1: '4 / 4 - 4 + 4 = 1', 2: '4 / 4 + 4 / 4 = 2', 4: '4 - 4 / 4 / 4 = 4', 7: '4 - 4 / 4 + 4 = 7', 8: '4 / 4 * 4 + 4 = 8', 9: '4 / 4 + 4 + 4 = 9', 256: '4 * 4 * 4 * 4 = 256', 15: '4 * 4 - 4 / 4 = 15', 16: '4 * 4 * 4 / 4 = 16', 17: '4 / 4 + 4 * 4 = 17', 24: '4 * 4 + 4 + 4 = 24', 68: '4 * 4 * 4 + 4 = 68', 32: '4 * 4 + 4 * 4 = 32', 60: '4 * 4 * 4 - 4 = 60', -60: '4 - 4 * 4 * 4 = -60', -16: '4 - 4 - 4 * 4 = -16', -15: '4 / 4 - 4 * 4 = -15', -8: '4 + 4 - 4 * 4 = -8', -7: '4 / 4 - 4 - 4 = -7', -4: '4 / 4 / 4 - 4 = -4', -1: '4 - 4 / 4 - 4 = -1'}
for _ in range(input()):
  e = input()
  print d[e] if e in d else 'no solution'
