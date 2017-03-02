from random import choice, shuffle, randint



def makeword(n):
  letters = 'abcdefghijklmnopqrstuvwxyz'
  s = ''
  for _ in range(n):
    s += choice(letters)
  return s

words = []
for _ in range(randint(10,100)):
  words.append(makeword(randint(1,30)))

commands = randint(1,2000)
types = ['def']*6  +  ['calc']*4 + ['clear']


defs = []
for _ in range(commands):
  t = choice(types)
  if t == 'def':
    word = choice(words)
    print('def', word, randint(-1000,1000))
    defs.append(word)

  if t == 'calc':
    parts = ['calc']
    parts.append(choice(words))
    for i in range(randint(0,15)):
      parts.append(choice(['-','+']))
      if(randint(1,5)==1 or len(defs)==0):
        parts.append(choice(words))
      else:
        parts.append(choice(defs))
    parts.append('=')
    print(' '.join(parts))

  if t == 'clear':
    print('clear')
    defs = []
