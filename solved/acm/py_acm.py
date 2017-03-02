solved = {}

line = raw_input()
while line != '-1':
  minutes, problem, result = line.split()
  minutes = int(minutes)

  if problem in solved:
    if result == 'right':
      solved[problem]['right'] = True
      solved[problem]['time'] = minutes
    else:
      solved[problem]['wrong'] += 1

  else:
    p = {
      'right': True if result == 'right' else False,
      'wrong': 0 if result == 'right' else 1,
      'time' : minutes if result == 'right' else 0
    }
    solved[problem] = p

  line = raw_input()



s = 0
minutes = 0
for key in solved:
  problem = solved[key]
  if problem['right']:
    s += 1
    minutes += problem['time']
    minutes += problem['wrong']*20

print s, minutes
