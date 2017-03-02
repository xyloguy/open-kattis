## STEP 1 (too slow) determine order of operators.
## This could be done by hand, but I was lazy :)
# import itertools
# pos = set()
# for perm in itertools.permutations(['*']*3 + ['+']*3 + ['-']*3 + ['/']*3):
#   p = (perm[0],perm[1],perm[2])
#   pos.add(p)
# print list(pos)



## STEP 2 (still slow) get solution to equations map.
## You can store a single equation, but I decided to keep them all
# pos = [('+', '*', '/'), ('-', '*', '-'), ('/', '/', '*'), ('+', '-', '/'), ('-', '*', '/'), ('-', '*', '+'), ('/', '-', '*'), ('/', '*', '/'), ('-', '*', '*'), ('+', '/', '+'), ('-', '+', '-'), ('+', '+', '*'), ('*', '-', '+'), ('-', '/', '*'), ('+', '+', '+'), ('*', '-', '*'), ('+', '*', '+'), ('-', '+', '/'), ('+', '*', '*'), ('*', '+', '/'), ('-', '-', '/'), ('*', '/', '/'), ('-', '/', '-'), ('/', '/', '+'), ('*', '+', '*'), ('/', '/', '-'), ('-', '+', '*'), ('+', '+', '/'), ('-', '-', '-'), ('*', '/', '-'), ('+', '/', '-'), ('-', '-', '*'), ('/', '+', '/'), ('+', '+', '-'), ('-', '-', '+'), ('*', '/', '+'), ('/', '-', '-'), ('*', '/', '*'), ('/', '+', '-'), ('+', '/', '/'), ('*', '+', '-'), ('/', '+', '*'), ('/', '-', '/'), ('*', '*', '*'), ('/', '+', '+'), ('*', '*', '+'), ('+', '-', '*'), ('/', '/', '/'), ('-', '+', '+'), ('+', '/', '*'), ('+', '-', '+'), ('*', '-', '-'), ('-', '/', '/'), ('*', '*', '-'), ('/', '*', '+'), ('+', '*', '-'), ('/', '-', '+'), ('+', '-', '-'), ('/', '*', '*'), ('*', '-', '/'), ('-', '/', '+'), ('*', '*', '/'), ('*', '+', '+'), ('/', '*', '-')]
# d = {}
# for p in pos:
#   e = '4 '
#   for x in p:
#     e += x
#     e += ' 4 '
#   if eval(e) in d:
#     d[eval(e)].append('%s= %d'%(e,eval(e)))
#   else:
#     d[eval(e)] = ['%s= %d'%(e,eval(e))]
# print d



# STEP 3, The actual solution. (fast)
# check if the number is in the dictionary.
#   - if it is, print the first equation (any counts)
#   - if it is not, print "no solution"
d = {0: ['4 / 4 / 4 * 4 = 0', '4 - 4 * 4 / 4 = 0', '4 - 4 + 4 - 4 = 0', '4 - 4 / 4 * 4 = 0', '4 * 4 - 4 * 4 = 0', '4 * 4 / 4 - 4 = 0', '4 - 4 - 4 + 4 = 0', '4 / 4 - 4 / 4 = 0', '4 / 4 / 4 / 4 = 0', '4 + 4 - 4 - 4 = 0', '4 / 4 * 4 - 4 = 0'], 1: ['4 / 4 * 4 / 4 = 1', '4 - 4 + 4 / 4 = 1', '4 * 4 / 4 / 4 = 1', '4 + 4 / 4 - 4 = 1', '4 / 4 + 4 - 4 = 1', '4 / 4 - 4 + 4 = 1'], 2: ['4 / 4 + 4 / 4 = 2'], 4: ['4 / 4 / 4 + 4 = 4', '4 + 4 / 4 / 4 = 4', '4 - 4 / 4 / 4 = 4'], 7: ['4 + 4 - 4 / 4 = 7', '4 - 4 / 4 + 4 = 7'], 8: ['4 + 4 * 4 / 4 = 8', '4 + 4 + 4 - 4 = 8', '4 * 4 / 4 + 4 = 8', '4 - 4 + 4 + 4 = 8', '4 + 4 / 4 * 4 = 8', '4 + 4 - 4 + 4 = 8', '4 * 4 - 4 - 4 = 8', '4 / 4 * 4 + 4 = 8'], 9: ['4 + 4 / 4 + 4 = 9', '4 + 4 + 4 / 4 = 9', '4 / 4 + 4 + 4 = 9'], 256: ['4 * 4 * 4 * 4 = 256'], 15: ['4 * 4 - 4 / 4 = 15'], 16: ['4 * 4 - 4 + 4 = 16', '4 + 4 + 4 + 4 = 16', '4 - 4 + 4 * 4 = 16', '4 * 4 / 4 * 4 = 16', '4 * 4 + 4 - 4 = 16', '4 + 4 * 4 - 4 = 16', '4 / 4 * 4 * 4 = 16', '4 * 4 * 4 / 4 = 16'], 17: ['4 * 4 + 4 / 4 = 17', '4 / 4 + 4 * 4 = 17'], 24: ['4 + 4 + 4 * 4 = 24', '4 + 4 * 4 + 4 = 24', '4 * 4 + 4 + 4 = 24'], 68: ['4 + 4 * 4 * 4 = 68', '4 * 4 * 4 + 4 = 68'], 32: ['4 * 4 + 4 * 4 = 32'], 60: ['4 * 4 * 4 - 4 = 60'], -60: ['4 - 4 * 4 * 4 = -60'], -16: ['4 - 4 * 4 - 4 = -16', '4 - 4 - 4 * 4 = -16'], -15: ['4 / 4 - 4 * 4 = -15'], -8: ['4 - 4 * 4 + 4 = -8', '4 - 4 - 4 - 4 = -8', '4 + 4 - 4 * 4 = -8'], -7: ['4 / 4 - 4 - 4 = -7'], -4: ['4 / 4 / 4 - 4 = -4'], -1: ['4 - 4 - 4 / 4 = -1', '4 - 4 / 4 - 4 = -1']}

for _ in range(input()):
  e = input()
  print d[e][0] if e in d else 'no solution'

